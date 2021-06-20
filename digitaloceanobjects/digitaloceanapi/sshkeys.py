from .digitaloceanapiconnection import DigitalOceanAPIConnection
import os
import time
import queue
import threading
import datetime
import random
import json


class SSHKeys(DigitalOceanAPIConnection):
    def __init__(self):
        DigitalOceanAPIConnection.__init__(self)
        self.endpoint = "/v2/account/keys"

    def list_all_keys(self):
        return self.get_request(self.endpoint, headers=self.headers)

    def create_new_key(self, name, public_key):
        data_dict = {}
        data_dict["name"] = name
        data_dict["public_key"] = public_key
        data = json.dumps(data_dict)

        return self.post_request(self.endpoint, headers=self.headers, data=data)

    def update_name(self, id, name):
        data_dict = {}
        data_dict["name"] = name
        data = json.dumps(data_dict)

        return self.put_request(
            f"{self.endpoint}/{id}", headers=self.headers, data=data
        )

    def delete_sshkey(self, identifier):
        # identifier could be the sshkey id or the sshkey fingerprint
        self.delete_request(f"{self.endpoint}/{identifier}")
