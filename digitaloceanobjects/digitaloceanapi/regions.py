from .digitaloceanapiconnection import DigitalOceanAPIConnection
import os
import time
import queue
import threading
import datetime
import random
import json


class Regions(DigitalOceanAPIConnection):
    def __init__(self):
        DigitalOceanAPIConnection.__init__(self)
        self.endpoint = "/v2/regions"

    def list_all_regions(self):
        return self.get_request(self.endpoint, headers=self.headers)
