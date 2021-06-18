from __future__ import annotations

from dataclasses import dataclass, field
from ..digitaloceanapi.actions import Actions
from ..common.cloudapiexceptions import *
import json
import threading
import time
import sys


@dataclass
class ActionAttributes:
    id: int = None
    status: str = None
    type: str = None
    started_at: str = None
    completed_at: str = None
    resource_id: int = None
    resource_type: str = None
    region: object = None
    region_slug: str = None


class ActionManager:
    def __init__(self):
        self.actionapi = Actions()

    def retrieve_all_actions(self):
        """
        Returns an array of Droplet objects, one for each droplet in digitalocean account.

        Returns:
            [type]: [description]
        """

        # Build list of droplets from api, but take in to account possible pagination.
        action_list = []
        page, per_page = 1, 10
        response = self.actionapi.list_all_actions(page=page, per_page=per_page)
        content = json.loads(response.content.decode("utf-8"))
        action_list.extend(content["actions"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                # if page % 10 == 0:
                #    print(page)
                response = self.actionapi.list_all_actions(page=page, per_page=per_page)
                content = json.loads(response.content.decode("utf-8"))
                action_list.extend(content["actions"])
                sys.stdout.flush()
        except KeyError:
            pass

        # Build and return that Droplet object array.
        action_objects = []
        for action_item in action_list:
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_item)
            action_objects.append(newaction)
        return action_objects

    def retrieve_paginated_actions(self, start_page, end_page, per_page=10):
        """
        Returns an array of Droplet objects, one for each droplet in digitalocean account.

        Returns:
            [type]: [description]
        """

        # Build list of droplets from api, but take in to account possible pagination.
        action_list = []
        page = start_page
        response = self.actionapi.list_all_actions(page=page, per_page=per_page)
        content = json.loads(response.content.decode("utf-8"))
        action_list.extend(content["actions"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.actionapi.list_all_actions(page=page, per_page=per_page)
                content = json.loads(response.content.decode("utf-8"))
                action_list.extend(content["actions"])
                sys.stdout.flush()
                if page >= end_page:
                    break
        except KeyError:
            pass

        # Build and return that Droplet object array.
        action_objects = []
        for action_item in action_list:
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_item)
            action_objects.append(newaction)
        return action_objects

    def does_action_exist_id(self, action_id):
        start_page, end_page = 1, 10
        actions = self.retrieve_paginated_actions(
            start_page=start_page, end_page=end_page
        )
        for action in actions:
            if action.attributes.id == action_id:
                return True
        full_result_count = len(actions)
        while True:
            start_page, end_page = start_page + 10, end_page + 10
            actions = self.retrieve_paginated_actions(
                start_page=start_page, end_page=end_page
            )
            for action in actions:
                if action.attributes.id == action_id:
                    print(action.attributes)
                    return True
            if len(actions) < full_result_count:
                break
        return False

    def retrive_action(self, action_id, check_if_exists=True):
        if check_if_exists:
            if not self.does_action_exist_id(action_id):
                raise ErrorActionDoesNotExists(
                    f"action with id:{action_id} does not exist"
                )
        response = self.actionapi.retrieve_existing_action(action_id)
        content = json.loads(response.content.decode("utf-8"))
        action = Action()
        action.attributes = ActionAttributes(**content["action"])
        return action

    def wait_for_action_completion(self, action: Action):
        while not action.attributes.status in ["completed", "errored"]:
            time.sleep(5)
        if action.attributes.status == "errored":
            raise ErrorActionFailed(
                f"Action {self.attributes.id},{self.attributes.type} failed"
            )


class Action:
    def __init__(self, action_attributes: ActionAttributes):
        self.attributes = action_attributes
        self.actionapi = Actions()
        self.update_on_active_action()

    def update_action_action(self):
        """
        Updates the Droplet lastaction data class with the latest droplet action information at digital ocean.
        """
        response = self.actionapi.retrieve_existing_action(self.attributes.id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            self.attributes = ActionAttributes(**action_data)

    def update_on_active_action(self):
        def update_action():
            # On creating a blank action it's id is None before a user defines an action.
            if self.attributes.id == None:
                pass
            while (self.attributes.status == None) or (
                self.attributes.status == "in-progress"
            ):
                if not self.attributes.status in ["completed", "errored"]:
                    time.sleep(10)
                    self.update_action_action()
                else:
                    break
                if self.attributes.status == "errored":
                    raise ErrorActionFailed(
                        f"Action {self.attributes.id},{self.attributes.type} failed"
                    )

        thread = threading.Thread(target=update_action, args=())
        thread.start()
