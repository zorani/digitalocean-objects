from __future__ import annotations

from dataclasses import dataclass, field
from ..digitaloceanapi.sizes import Sizes
from ..common.cloudapiexceptions import *
import json
import threading
import time
import sys


@dataclass
class SizeAttributes:
    slug: str = None
    available: bool = None
    transfer: float = None
    price_monthly: float = None
    price_hourly: float = None
    memory: int = None
    vcpus: int = None
    disk: int = None
    regions: list = field(default_factory=list)
    description: str = None


class SizeManager:
    def __init__(self):
        self.sizeapi = Sizes()

    def retrieve_sizes(self):
        response = self.sizeapi.list_all_sizes()
        size_list = []
        return_sizes = []
        if response:
            content = json.loads(response.content.decode("utf-8"))
            size_list = content["sizes"]
        for size_data in size_list:
            newsize = Size()
            newsize.attributes = SizeAttributes(**size_data)
            return_sizes.append(newsize)
        return return_sizes

    def retrieve_size(self, slug):
        sizes = self.retrieve_sizes()
        for size in sizes:
            if size.attributes.slug == slug:
                return size
        raise ErrorDropletSlugSizeNotFound(f'"{slug}" not found')


class Size:
    def __init__(self):
        self.attributes = SizeAttributes()
