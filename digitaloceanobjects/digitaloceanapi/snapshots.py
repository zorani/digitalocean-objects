from .digitaloceanapiconnection import DigitalOceanAPIConnection
import os
import time
import queue
import threading
import datetime
import random
import json


class Snapshots(DigitalOceanAPIConnection):
    def __init__(self):
        DigitalOceanAPIConnection.__init__(self)
        self.endpoint = "/v2/snapshots"

    def list_all_snapshots(self, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments

        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def list_all_droplet_snapshots(self, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        arguments["resource_type"] = "droplet"
        # params must be set from a dictionary not a json dump
        params = arguments

        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def list_all_volume_snapshots(self):
        arguments = locals()
        del arguments["self"]
        arguments["resource_type"] = "volume"
        # params must be set from a dictionary not a json dump
        params = arguments

        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def retrieve_snapshot_by_id(self, id):
        return self.get_request(f"{self.endpoint}/{id}", headers=self.headers)

    def delete_snapshot_id(self, id):
        return self.delete_request(f"{self.endpoint}/{id}", headers=self.headers)
