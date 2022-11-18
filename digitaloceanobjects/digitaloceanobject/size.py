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
        sizes_list = []
        page, per_page = 1, 10
        response = self.sizeapi.list_all_sizes(page=page, per_page=per_page)
        content = json.loads(response.content.decode("utf-8"))
        sizes_list.extend(content["sizes"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.sizeapi.list_all_sizes(page=page, per_page=per_page)
                content = json.loads(response.content.decode("utf-8"))
                sizes_list.extend(content["sizes"])
                sys.stdout.flush()
        except KeyError:
            pass

        sizes_objects = []
        for sizes_data in sizes_list:
            newsize = Size()
            newsize.attributes = SizeAttributes(**sizes_data)
            sizes_objects.append(newsize)
        return sizes_objects

    def retrieve_size(self, slug):
        sizes = self.retrieve_sizes()
        for size in sizes:
            if size.attributes.slug == slug:
                return size
        raise ErrorDropletSlugSizeNotFound(f'"{slug}" not found')


class Size:
    def __init__(self):
        self.attributes = SizeAttributes()
