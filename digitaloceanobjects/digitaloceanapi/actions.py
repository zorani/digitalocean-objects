from .digitaloceanapiconnection import DigitalOceanAPIConnection
import os
import time
import queue
import threading
import datetime
import random
import json


class Actions(DigitalOceanAPIConnection):
    def __init__(self):
        DigitalOceanAPIConnection.__init__(self)
        self.endpoint = "/v2/actions"

    def list_all_actions(self, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments

        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def retrieve_existing_action(self, action_id):

        return self.get_request(f"{self.endpoint}/{action_id}", headers=self.headers)
