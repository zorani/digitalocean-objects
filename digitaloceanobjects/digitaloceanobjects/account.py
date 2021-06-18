from __future__ import annotations

from dataclasses import dataclass, field

from requests.models import Response
from ..digitaloceanapi.accounts import Accounts
from ..common.cloudapiexceptions import *
import json
import threading
import time
import re


@dataclass
class AccountAttributes:
    droplet_limit: int = None
    floating_ip_limit: int = None
    volume_limit: int = None
    email: str = None
    uuid: str = None
    email_verified: bool = None
    status: str = None
    status_message: str = None


class AccountManager:
    def __init__(self):
        self.accountapi = Accounts()

    def retrieve_account_details(self):
        response = self.accountapi.list_account_information()
        if response:
            content = json.loads(response.content.decode("utf-8"))
            account_data = content["account"]
            newaccount = Account()
            newaccount.attributes = AccountAttributes(**account_data)
            return newaccount

    def droplet_limit(self):
        return self.retrieve_account_details().attributes.droplet_limit

    def floating_ip_limit(self):
        return self.retrieve_account_details().attributes.floating_ip_limit
        

    def volume_limit(self):
        return self.retrieve_account_details().attributes.volume_limit

    def email(self):
        return self.retrieve_account_details().attributes.email

    def uuid(self):
        return self.retrieve_account_details().attributes.uuid

    def email_verified(self):
        return self.retrieve_account_details().attributes.email_verified

    def status(self):
        return self.retrieve_account_details().attributes.status

    def status_message(self):
        return self.retrieve_account_details().attributes.status_message


class Account:
    def __init__(self, status=None):
        self.attributes = AccountAttributes()
