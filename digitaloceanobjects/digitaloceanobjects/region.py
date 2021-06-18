from __future__ import annotations

from dataclasses import dataclass, field
from ..digitaloceanapi.regions import Regions

from ..common.cloudapiexceptions import *
import json
import threading
import time
import re


@dataclass
class RegionAttributes:
    slug: str = None
    name: str = None
    sizes: list = field(default_factory=list)
    available: bool = None
    features: list = field(default_factory=list)


class RegionManager:
    def __init__(self):
        self.regionapi = Regions()

    def retrieve_all_regions(self):
        region_objects = []
        response = self.regionapi.list_all_regions()
        if response:
            content = json.loads(response.content.decode("utf-8"))
            region_datas = content["regions"]
            for region_data in region_datas:
                newregion = Region()
                newregion.attributes = RegionAttributes(**region_data)
                region_objects.append(newregion)
            return region_objects

    def does_region_exist(self, region_slug):
        digital_ocean_regions = self.retrieve_all_regions()
        for digital_ocean_region in digital_ocean_regions:
            if digital_ocean_region.attributes.slug == region_slug:
                return True
        return False


class Region:
    def __init__(self):
        self.attributes = RegionAttributes()
