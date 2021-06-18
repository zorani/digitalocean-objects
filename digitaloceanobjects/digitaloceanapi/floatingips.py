from .digitaloceanapiconnection import DigitalOceanAPIConnection
import os
import time
import queue
import threading
import datetime
import random
import json


class FloatingIPs(DigitalOceanAPIConnection):
    def __init__(self):
        DigitalOceanAPIConnection.__init__(self)
        self.endpoint = "/v2/floating_ips"

    def list_all_floating_ips(self, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments
        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def create_new_floating_ip(self, droplet_id):
        data_dict = {}
        data_dict["droplet_id"] = droplet_id
        data = json.dumps(data_dict)

        return self.post_request(self.endpoint, headers=self.headers, data=data)

    def reserve_ip_for_region(self, region):
        data_dict = {}
        data_dict["region"] = region
        data = json.dumps(data_dict)

        return self.post_request(self.endpoint, headers=self.headers, data=data)

    def delete_floating_ip(self, ip):
        self.delete_request(f"{self.endpoint}/{ip}")

    def assign_floating_ip_to_droplet(self, ip, droplet_id):
        data_dict = {}
        data_dict["type"] = "assign"
        data_dict["droplet_id"] = droplet_id

        data = json.dumps(data_dict)

        return self.post_request(
            f"{self.endpoint}/{ip}/actions", headers=self.headers, data=data
        )

    def unassign_floating_ip(self, ip):
        data_dict = {}
        data_dict["type"] = "unassign"

        data = json.dumps(data_dict)

        return self.post_request(
            f"{self.endpoint}/{ip}/actions", headers=self.headers, data=data
        )

    def list_all_actions(self, ip, page=0, per_page=0):
        # params must be set from a dictionary not a json dump
        params = {}
        params["page"] = page
        params["per_page"] = per_page

        return self.get_request(
            f"{self.endpoint}/{ip}/actions", headers=self.headers, params=params
        )
