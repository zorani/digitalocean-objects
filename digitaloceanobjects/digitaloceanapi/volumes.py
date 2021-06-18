from .digitaloceanapiconnection import DigitalOceanAPIConnection
import os
import time
import queue
import threading
import datetime
import random
import json


class Volumes(DigitalOceanAPIConnection):
    """[summary]

    Args:
        DigitalOceanAPIConnection ([type]): [description]
    API Returns Volume Attributes:
        id(str):                The unique identifier for the block storage volume.
        region(object):         The region that the block storage volume is located in. When setting a region, the value should be the slug identifier for the region. When you query a block storage volume, the entire region object will be returned.
        droplet_ids([]):        An array containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet.
        name(str):	            A human-readable name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters. The name must begin with a letter.
        description(str):	    An optional free-form text field to describe a block storage volume.
        size_gigabytes(int):	The size of the block storage volume in GiB (1024^3).
        created_at(str):	    A time value given in ISO8601 combined date and time format that represents when the block storage volume was created.
        filesystem_type(str):	The type of filesystem currently in-use on the volume.
        filesystem_label(str)   The label currently applied to the filesystem.
        tags([]):               An array of tags the volume has been tagged with

    """

    def __init__(self):
        DigitalOceanAPIConnection.__init__(self)
        self.endpoint = "/v2/volumes"

    def list_all_volumes(self, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments

        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def list_all_volumes_by_name(self, name, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments

        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def create_new_volume(
        self,
        size_gigabytes: int,
        name: str,
        region: str,
        description: str = None,
        snapshot_id: str = None,
        filesystem_type: str = None,
        filesystem_label: str = None,
        tags: list = None,
    ):

        """[summary]

        Returns:
            [type]: [description]
        API Expects:
                size_gigabytes(int):	REQUIRED The size of the block storage volume in GiB (1024^3).
                name(str):	            REQUIRED A human-readable name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters.
                region(str):	        REQUIRED The region where the block storage volume will be created. When setting a region, the value should be the slug identifier for the region. When you query a block storage volume, the entire region object will be returned.
                description(str):	    string	An optional free-form text field to describe a block storage volume.
                snapshot_id(str):       The unique identifier for the volume snapshot from which to create the volume. Should not be specified with a region_id.
                filesystem_type(str):	The name of the filesystem type to be used on the volume. When provided, the volume will automatically be formatted to the specified filesystem type. Currently, the available options are "ext4" and "xfs". Pre-formatted volumes are automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted volumes to other Droplets is not recommended.
                filesystem_label(str):	The label to be applied to the filesystem. Labels for ext4 type filesystems may contain 16 characters while lables for xfs type filesystems are limited to 12 characters. May only be used in conjunction with filesystem_type.
                tags([]):   	        A flat array of tag names as strings to apply to the Volume after it is created. Tag names can either be existing or new tags.


        API data example:


        """
        arguments = locals()
        del arguments["self"]
        data = json.dumps(arguments)
        return self.post_request(f"{self.endpoint}", headers=self.headers, data=data)

    def retrieve_volume_by_id(self, id):
        return self.get_request(f"{self.endpoint}/{id}", headers=self.headers)

    def retrieve_volume_name_region(self, name, region):
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments
        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def delete_volume_id(self, id):
        return self.delete_request(f"{self.endpoint}/{id}", headers=self.headers)

    def delete_volume_name_region(self, name, region):
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments
        return self.delete_request(self.endpoint, headers=self.headers, params=params)

    def create_snapshot_from_volume(self, id, name, tags=[]):
        data_dict = {}
        data_dict["name"] = name
        data_dict["tags"] = tags
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{id}/snapshots", headers=self.headers, data=data
        )

    def list_snapshots_for_volume(self, id, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        del arguments["id"]
        # params must be set from a dictionary not a json dump
        params = arguments
        return self.get_request(
            f"{self.endpoint}/{id}/snapshots", headers=self.headers, params=params
        )

    def attach_volume_to_droplet(self, volume_id, droplet_id, region, tags=[]):
        data_dict = {}
        data_dict["type"] = "attach"
        data_dict["droplet_id"] = droplet_id
        data_dict["region"] = str(region)
        data_dict["tags"] = tags
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{volume_id}/actions", headers=self.headers, data=data
        )

    def detach_volume_from_droplet(self, volume_id, droplet_id, region=None):
        data_dict = {}
        data_dict["type"] = "detach"
        data_dict["droplet_id"] = droplet_id
        if not region == None:
            data_dict["region"] = region
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{volume_id}/actions", headers=self.headers, data=data
        )

    def retrieve_volume_action(self, volume_id, action_id):

        return self.get_request(
            f"{self.endpoint}/{volume_id}/actions/{action_id}", headers=self.headers
        )

    def resize_volume(self, volume_id, size, region=None):
        # size from 1GB to max 16,384GB
        data_dict = []
        data_dict["type"] = "resize"
        data_dict["size_gigabytes"] = size
        if not region == None:
            data_dict["region"] = region
        data = json.dumps(data_dict)

        return self.post_request(
            f"{self.endpoint}/{volume_id}/actions", headers=self.headers, data=data
        )
