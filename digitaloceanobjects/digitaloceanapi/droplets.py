from .digitaloceanapiconnection import DigitalOceanAPIConnection
import os
import time
import queue
import threading
import datetime
import random
import json


class Droplets(DigitalOceanAPIConnection):
    """[summary]

    Args:
        DigitalOceanAPIConnection ([type]): [description]

    API Returns Droplet Attributes:
                id(int):	                A unique identifier for each Droplet instance.  This is automatically generated upon Droplet creation.
                name(str):	                The human-readable name set for the Droplet instance.
                memory(int):                Memory of the Droplet in megabytes.
                vcpus(int): 	            The number of virtual CPUs.
                disk(int):  	            The size of the Droplet's disk in gigabytes.
                locked(bool):	            A boolean value indicating whether the Droplet has been locked, preventing actions by users.
                created_at(str):	        A time value given in ISO8601 combined date and time format that represents when the Droplet was created.
                status(str):    	        A status string indicating the state of the Droplet instance.  This may be "new", "active", "off", or "archive".
                backup_ids([]):             An array of backup IDs of any backups that have been taken of the Droplet instance.  Droplet backups are enabled at the time of the instance creation.
                snapshot_ids([]):	        An array of snapshot IDs of any snapshots created from the Droplet instance.
                features([]):   	        An array of features enabled on this Droplet.
                region(obj):    	        The region that the Droplet instance is deployed in.  When setting a region, the value should be the slug identifier for the region.  When you query a Droplet, the entire region object will be returned.
                image(obj):     	        The base image used to create the Droplet instance.  When setting an image, the value is set to the image id or slug.  When querying the Droplet, the entire image object will be returned.
                size(obj):      	        The current size object describing the Droplet. When setting a size, the value is set to the size slug.  When querying the Droplet, the entire size object will be returned. Note that the disk volume of a Droplet may not match the size's disk due to Droplet resize actions. The disk attribute on the Droplet should always be referenced.
                size_slug(str): 	        The unique slug identifier for the size of this Droplet.
                networks(obj):  	        The details of the network that are configured for the Droplet instance.  This is an object that contains keys for IPv4 and IPv6.  The value of each of these is an array that contains objects describing an individual IP resource allocated to the Droplet.  These will define attributes like the IP address, netmask, and gateway of the specific network depending on the type of network it is.
                kernel(obj):    	        Nullable object	The current kernel. This will initially be set to the kernel of the base image when the Droplet is created.
                next_backup_window(obj)	    Nullable object	The details of the Droplet's backups feature, if backups are configured for the Droplet. This object contains keys for the start and end times of the window during which the backup will start.
                tags([]):	                An array of Tags the Droplet has been tagged with.
                volume_ids([]):             A flat array including the unique identifier for each Block Storage volume attached to the Droplet.
                vpc_uuid([]):           	A string specifying the UUID of the VPC to which the Droplet is assigned.
    """

    def __init__(self):
        DigitalOceanAPIConnection.__init__(self)
        self.endpoint = "/v2/droplets"

    def list_all_droplets(self, page=0, per_page=0):
        """[summary]

        Returns:
            [type]: [description]
        API Expects:
                page(int)                   which page to return
                per_page(int)               how many results per page
        API Returns:
                A list of droplets objects, with standard droplet attributes.

        """
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments

        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def list_all_droplets_by_tag(self, tag_name, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        # params must be set from a dictionary not a json dump
        params = arguments

        return self.get_request(self.endpoint, headers=self.headers, params=params)

    def create_new_droplet(
        self,
        name,
        region,
        size,
        image,
        ssh_keys=[],
        backups=None,
        ipv6=None,
        private_networking=None,
        vpc_uuid=None,
        user_data=None,
        monitoring=None,
        volumes=[],
        tags=[],
    ):

        """[summary]

        Returns:
            [type]: [description]
        API Expects:
                name(str):	                REQUIRED.  The human-readable string you wish to use when displaying the Droplet name. The name, if set to a domain name managed in the DigitalOcean DNS management system, will configure a PTR record for the Droplet. The name set during creation will also determine the hostname for the Droplet in its internal configuration.
                region(str):	            REQUIRED.  The unique slug identifier for the region that you wish to deploy in.
                size(str):                  REQUIRED.  The unique slug identifier for the size that you wish to select for this Droplet.
                image(int,str):	            REQUIRED.  integer (if using an image ID), or String (if using a public image slug)	The image ID of a public or private image, or the unique slug identifier for a public image. This image will be the base image for your Droplet.
                ssh_keys([]):	            An array containing the IDs or fingerprints of the SSH keys that you wish to embed in the Droplet's root account upon creation.
                backups(bool):              A boolean indicating whether automated backups should be enabled for the Droplet. Automated backups can only be enabled when the Droplet is created.
                ipv6(bool):                 A boolean indicating whether IPv6 is enabled on the Droplet.
                private_networking(bool):	This parameter has been deprecated. Use 'vpc_uuid' instead to specify a VPC network for the Droplet. If no `vpc_uuid` is provided, the Droplet will be placed in the default VPC.
                vpc_uuid(str):          	A string specifying the UUID of the VPC to which the Droplet will be assigned. If excluded, beginning on April 7th, 2020, the Droplet will be assigned to your account's default VPC for the region.
                user_data(str):             A string containing 'user data' which may be used to configure the Droplet on first boot, often a 'cloud-config' file or Bash script. It must be plain text and may not exceed 64 KiB in size.
                monitoring(bool):           A boolean indicating whether to install the DigitalOcean agent for monitoring.
                volumes([]):            	A flat array including the unique string identifier for each block storage volume to be attached to the Droplet. At the moment a volume can only be attached to a single Droplet.
                tags([])                    A flat array of tag names as strings to apply to the Droplet after it is created. Tag names can either be existing or new tags.

        API Returns:
               A droplets object, with standard droplet attributes.

        API data example:
                data = '{"name":"example.com","region":"nyc3","size":"s-1vcpu-1gb","image":"ubuntu-16-04-x64","ssh_keys":[107149],"backups":false,"ipv6":true,"user_data":null,"private_networking":null,"volumes": null,"tags":["web"]}'


        """
        arguments = locals()
        del arguments["self"]
        data = json.dumps(arguments)
        return self.post_request(self.endpoint, headers=self.headers, data=data)

    def delete_droplet_id(self, id):
        """
        To delete a Droplet, send a DELETE request to /v2/droplets/$DROPLET_ID
        """
        return self.delete_request(f"{self.endpoint}/{id}", headers=self.headers)

    def delete_droplet_tag(self, tag_name):
        """
        To delete Droplets by a tag (for example awesome), send a DELETE request to /v2/droplets?tag_name=$TAG_NAME.
        """
        return self.delete_request(
            f"{self.endpoint}?tag_name={tag_name}", headers=self.headers
        )

    def retrieve_droplet_by_id(self, id):
        """[summary]

        Args:
            id ([type]): [description]
            To show information about an individual Droplet, send a GET request to /v2/droplets/$DROPLET_ID.
        """
        return self.get_request(f"{self.endpoint}/{id}", headers=self.headers)

    def retrieve_droplet_action(self, droplet_id, action_id):
        """

        Args:
            droplet_id ([type]): [description]
            action_id ([type]): [description]
        """

        return self.get_request(
            f"{self.endpoint}/{droplet_id}/actions/{action_id}", headers=self.headers
        )

    def reboot_droplet(self, id):
        """

        Args:
            id ([type]): [description]
        """
        data_dict = {}
        data_dict["type"] = "reboot"
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{id}/actions", headers=self.headers, data=data
        )

    def shutdown_droplet(self, id):
        """

        Args:
            id ([type]): [description]
        """
        data_dict = {}
        data_dict["type"] = "shutdown"
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{id}/actions", headers=self.headers, data=data
        )

    def poweron_droplet(self, id):
        """

        Args:
            id ([type]): [description]
        """
        data_dict = {}
        data_dict["type"] = "power_on"
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{id}/actions", headers=self.headers, data=data
        )

    def poweroff_droplet(self, id):
        """

        Args:
            id ([type]): [description]
        """
        data_dict = {}
        data_dict["type"] = "power_off"
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{id}/actions", headers=self.headers, data=data
        )

    def powercycle_droplet(self, id):
        """

        Args:
            id ([type]): [description]
        """
        data_dict = {}
        data_dict["type"] = "power_cycle"
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{id}/actions", headers=self.headers, data=data
        )

    def rebuild_droplet(self, id, image):
        """
        Rebuld action functions just like a new create.

        Args:
            id ([type]): Droplet ID
            image ([type]): Image slug or ID.

        Returns:
            [type]: [description]
        """
        data_dict = {}
        data_dict["type"] = "rebuild"
        data_dict["image"] = image
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{id}/actions", headers=self.headers, data=data
        )

    def rename_droplet(self, id, name):
        print("rename api called")
        """
        Rebuld action functions just like a new create.

        Args:
            id ([type]): Droplet ID
            name ([type]): New droplet name

        Returns:
            [type]: [description]
        """
        data_dict = {}
        data_dict["type"] = "rename"
        data_dict["name"] = name
        data = json.dumps(data_dict)
        endpoint = f"{self.endpoint}/{id}/actions"
        print(endpoint)
        print(data)
        return self.post_request(endpoint, headers=self.headers, data=data)
        print("api finished")

    def create_snapshot_from_droplet(self, id, name):
        data_dict = {}
        data_dict["type"] = "snapshot"
        data_dict["name"] = name
        # api doesnt let you have tags for droplets at this point
        # data_dict["tags"] = tags
        data = json.dumps(data_dict)
        return self.post_request(
            f"{self.endpoint}/{id}/actions", headers=self.headers, data=data
        )

    def list_snapshots_for_droplet(self, id, page=0, per_page=0):
        arguments = locals()
        del arguments["self"]
        del arguments["id"]
        # params must be set from a dictionary not a json dump
        params = arguments
        return self.get_request(
            f"{self.endpoint}/{id}/snapshots", headers=self.headers, params=params
        )

    def restore_droplet(self, droplet_id, image_id):
        data_dict = {}
        data_dict["type"] = "restore"
        data_dict["image"] = image_id
        data = json.dumps(data_dict)

        return self.post_request(
            f"{self.endpoint}/{droplet_id}/actions", headers=self.headers, data=data
        )

    def resize_droplet(self, droplet_id, size, disk_resize=False):
        ##WARNING... if you try to resie to a lower size disk  api will hang.
        ##need to implement checking if resize is allowed.
        """[summary]

        Args:
            droplet_id ([type]): [description]
            size ([type]): [description]
            disk_resize (bool, optional): When set to True you resize not only the memory, but also you upgrade to the disk size of the slug, meaning you cant resize back down. Defaults to False.

        Returns:
            [type]: [description]
        """
        data_dict = {}
        data_dict["type"] = "resize"
        if disk_resize:
            data_dict["disk"] = True
        data_dict["size"] = size
        data = json.dumps(data_dict)

        return self.post_request(
            f"{self.endpoint}/{droplet_id}/actions", headers=self.headers, data=data
        )

    def list_droplet_resources(self, droplet_id):
        return self.get_request(
            f"{self.endpoint}/{droplet_id}/destroy_with_associated_resources",
            headers=self.headers,
        )


if __name__ == "__main__":
    digitalocean_droplets = Droplets()

    # def make_a_call_to_digitalocea_to_list_all_droplets(x):
    #    response = digitalocean_droplets.list_all_droplets()
    #    print(x, datetime.datetime.now())

    # for x in range(0, 20):
    #    threading.Thread(
    #        target=make_a_call_to_digitalocea_to_list_all_droplets, args=(x,)
    #    ).start()

    response = digitalocean_droplets.create_new_droplet(
        name="example.com",
        region="nyc3",
        size="s-1vcpu-1gb",
        image="ubuntu-16-04-x64",
        ssh_keys=[],
        backups=False,
        ipv6=True,
        user_data=None,
        private_networking=None,
        volumes=None,
        tags=["banabas"],
    )

    # response = digitalocean_droplets.delete_droplet_id(249612802)

    # response = digitalocean_droplets.list_all_droplets(page=1, per_page=2)
    content = response.content.decode("utf-8")
    droplet_data = dict(json.loads(content)["droplet"])
    print(droplet_data)
