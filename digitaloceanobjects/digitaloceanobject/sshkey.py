from __future__ import annotations

from dataclasses import dataclass, field
from ..digitaloceanapi.sshkeys import SSHKeys
from ..common.cloudapiexceptions import *
import json
import threading
import time
import re


@dataclass
class SSHKeyAttributes:
    id: str = None
    fingerprint: str = None
    public_key: str = None
    name: str = None


class SSHKeyManager:
    def __init__(self):
        self.sshkeyapi = SSHKeys()

    def retrieve_all_sshkeys(self):
        sshkey_objects = []
        response = self.sshkeyapi.list_all_keys()
        if response:
            content = json.loads(response.content.decode("utf-8"))
            sshkey_datas = content["ssh_keys"]
            for sshkey_data in sshkey_datas:
                newsshkey = SSHKey()
                newsshkey.attributes = SSHKeyAttributes(**sshkey_data)
                sshkey_objects.append(newsshkey)
        return sshkey_objects

    def create_new_key(self, name, public_key):
        newsshkey = SSHKey()
        response = self.sshkeyapi.create_new_key(name, public_key)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            sshkey_data = content["ssh_key"]
            newsshkey = SSHKey()
            newsshkey.attributes = SSHKeyAttributes(**sshkey_data)
            return newsshkey

    def retrieve_sshkey_with_id(self, id):
        sshkey_objects = self.retrieve_all_sshkeys()
        for sshkey in sshkey_objects:
            if sshkey.attributes.id == id:
                return sshkey
        raise ErrorSSHkeyDoesNotExists(f"SSHkey with id {id} could not be found.")

    def does_sshkey_exist_id(self, id):
        sshkey_objects = self.retrieve_all_sshkeys()
        for sshkey in sshkey_objects:
            if sshkey.attributes.id == id:
                return True
        return False


class SSHKey:
    def __init__(self):
        self.attributes = SSHKeyAttributes()
        self.sshkeyapi = SSHKeys()
        self.sshkey_manager = SSHKeyManager()

    def update_name(self, name):
        if self.sshkey_manager.does_sshkey_exist_id(self.attributes):
            response = self.sshkeyapi.update_name(self.attributes.id, name)
            if response:
                content = json.loads(response.content.decode("utf-8"))
                sshkey_data = content["ssh_key"]
                self.attributes = SSHKeyAttributes(**sshkey_data)
        raise ErrorSSHkeyDoesNotExists(
            f"SSHkey with id {self.attributes.id} could not be found."
        )

    def delete(self):
        if self.sshkey_manager.does_sshkey_exist_id(self.attributes):
            self.sshkeyapi.delete_sshkey(self.attributes.id)
