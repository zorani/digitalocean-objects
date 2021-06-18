from __future__ import annotations

from dataclasses import dataclass, field
from ..digitaloceanapi.droplets import Droplets
from ..digitaloceanapi.floatingips import FloatingIPs
from .action import *
from .droplet import *
from .region import *
from .account import *
from ..common.cloudapiexceptions import *
import json
import threading
import time
import re


@dataclass
class FloatingIPAttributes:
    ip: str = None
    region: object = None
    droplet: object = None
    locked: bool = None


class FloatingIPManager:
    def __init__(self):
        self.floatingipapi = FloatingIPs()
        self.action_manager = ActionManager()
        self.region_manager = RegionManager()
        self.account_manager = AccountManager()

    def check_limit(self):
        floating_ip_limit = self.account_manager.floating_ip_limit()
        if not len(self.retrieve_all_floating_ips()) < floating_ip_limit:
            raise ErrorAccountFloatingIPLimitReached(
                f"You have reached your floating ip limit of {floating_ip_limit}"
            )

    def retrieve_all_floating_ips(self):
        floating_ip_list = []
        page, per_page = 1, 10
        response = self.floatingipapi.list_all_floating_ips(
            page=page, per_page=per_page
        )
        content = json.loads(response.content.decode("utf-8"))
        floating_ip_list.extend(content["floating_ips"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.floatingipapi.list_all_floating_ips(
                    page=page, per_page=per_page
                )
                content = json.loads(response.content.decode("utf-8"))
                floating_ip_list.extend(content["floating_ips"])
        except KeyError:
            pass

        floating_ip_objects = []
        for floating_ip in floating_ip_list:
            newfloatingip = FloatingIP()
            newfloatingip.attributes = FloatingIPAttributes(**floating_ip)
            floating_ip_objects.append(newfloatingip)
        return floating_ip_objects

    def create_new_floating_ip(self, droplet: Droplet):
        self.check_limit()
        floatingip = self.check_droplet_for_floating_ip(droplet)
        if not floatingip == None:
            raise ErrorDropletAlreadyHasFloatingIP(
                f"Droplet id:{droplet.attributes.id} already has a private ip: {floatingip.attributes.ip}"
            )

        response = self.floatingipapi.create_new_floating_ip(droplet.attributes.id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            floating_ip_data = content["floating_ip"]
            newfloatingip = FloatingIP()
            newfloatingip.attributes = FloatingIPAttributes(**floating_ip_data)
            return newfloatingip

    def check_droplet_for_floating_ip(self, droplet: Droplet):
        floating_ips = self.retrieve_all_floating_ips()
        for floating_ip in floating_ips:
            if not floating_ip.attributes.droplet == None:
                if floating_ip.attributes.droplet["id"] == droplet.attributes.id:
                    return floating_ip
        return None

    def reserve_ip_for_region(self, region_slug):
        self.check_limit()
        if self.region_manager.does_region_exist(region_slug):
            response = self.floatingipapi.reserve_ip_for_region(region_slug)
            if response:
                content = json.loads(response.content.decode("utf-8"))
                floating_ip_data = content["floating_ip"]
                newfloatingip = FloatingIP()
                newfloatingip.attributes = FloatingIPAttributes(**floating_ip_data)
                return newfloatingip
        else:
            raise ErrorRegionDoesNotExist(f'"{region_slug}" not a valid region')

    def retrieve_floating_ip(self, ip):
        floatingips = self.retrieve_all_floating_ips()
        for floatingip in floatingips:
            if floatingip.attributes.ip == ip:
                return floatingip
        raise ErrorFloatingIPDoesNotExists(
            f"Could not find ip:{ip} associated with your account"
        )


class FloatingIP:
    def __init__(self):
        self.attributes = FloatingIPAttributes()
        self.lastaction: Action = None
        self.floatingipapi = FloatingIPs()
        self.floatingip_manager = FloatingIPManager()
        self.action_manager = ActionManager()

    def delete(self):
        self.floatingipapi.delete_floating_ip(self.attributes.ip)

    def unassign(self):
        newaction = Action()
        response = self.floatingipapi.unassign_floating_ip(self.attributes.ip)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            newaction.attributes = ActionAttributes(content["action"])
            self.action_manager.wait_for_action_completion(newaction)

    def attach_to_droplet(self, droplet: Droplet):
        if not self.floatingip_manager.check_droplet_for_floating_ip(droplet) == None:
            self.unassign()
        newaction = Action()
        response = self.floatingipapi.assign_floating_ip_to_droplet(
            self.attributes.ip, droplet.attributes.id
        )
        if response:
            content = json.loads(response.content.decode("utf-8"))
            newaction.attributes = ActionAttributes(content["action"])
            self.action_manager.wait_for_action_completion(newaction)

    def retrieve_all_actions(self):
        action_list = []
        page, per_page = 1, 10
        response = self.floatingipapi.list_all_actions(page=page, per_page=per_page)
        content = json.loads(response.content.decode("utf-8"))
        action_list.extend(content["actions"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.floatingipapi.list_all_actions(
                    page=page, per_page=per_page
                )
                content = json.loads(response.content.decode("utf-8"))
                action_list.extend(content["actions"])
        except KeyError:
            pass

        # Build and return that Droplet object array.
        action_objects = []
        for action_item in action_list:
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_item)
            action_objects.append(newaction)
        return action_objects

    def retrieve_existing_action(self, action_id):
        floatingip_actions = self.retrieve_existing_action()
        for floatingip_action in floatingip_actions:
            if floatingip_action.attributes.id == action_id:
                return floatingip_action
        raise ErrorActionDoesNotExists(
            f"floating ip:{self.attributes.ip} does not have associated actions"
        )
