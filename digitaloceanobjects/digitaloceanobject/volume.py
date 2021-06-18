from __future__ import annotations

from dataclasses import dataclass, field
from ..digitaloceanapi.volumes import Volumes
from ..digitaloceanapi.snapshots import Snapshots
from ..common.cloudapiexceptions import *
from .action import *
from .snapshot import *
from .account import *
import json
import threading
import time


@dataclass
class VolumeAttributes:
    id: str = None
    region: object = field(default_factory=list)
    droplet_ids: list = field(default_factory=list)
    name: str = None
    description: str = None
    size_gigabytes: int = None
    created_at: str = None
    filesystem_type: str = None
    filesystem_label: str = None
    tags: list = field(default_factory=list)


@dataclass
class VolumeArguments:
    size_gigabytes: int = None
    name: str = None
    region: str = None
    description: str = None
    snapshot_id: str = None
    filesystem_type: str = None
    filesystem_label: str = None
    tags: list = field(default_factory=list)


#@dataclass
#class VolumeLastActions:
#    id: int = None
#    status: str = None
#    type: str = None
#    started_at: str = None
#    completed_at: str = None
#    resource_id: int = None
#    resource_type: str = None
#    region: object = None
#    region_slug: str = None


class VolumeManager:
    def __init__(self):
        self.volumeapi = Volumes()
        self.account_manager = AccountManager()

    def check_limit(self):
        volume_limit = self.account_manager.volume_limit()
        if not len(self.retrieve_all_volumes()) < volume_limit:
            raise ErrorAccountVolumeLimitReached
            (
                f"You have reached your volume limit of {volume_limit}"
            )


    def create_new_volume(
        self,
        size_gigabytes: int,
        name: str,
        region: str,
        description: str = None,
        snapshot_id: str = None,
        filesystem_type: str = None,
        filesystem_label: str = None,
        tags: list= None,
    ):

        arguments = locals()
        del arguments["self"]

        if self.does_volume_name_region_exist(name, region):
            raise ErrorVolumeAlreadyExists(
                f"Volume name:{name}, region:{region} Already Exists"
            )

        self.check_limit()

        newvolume = Volume()
        newvolume.arguments = VolumeArguments(**arguments)
        response = self.volumeapi.create_new_volume(**arguments)
        if response:
            #
            volume_data = dict(json.loads(response.content.decode("utf-8"))["volume"])
            newvolume.attributes = VolumeAttributes(**volume_data)
        else:
            raise Exception(f"Could not create volume {name}")
        return newvolume

    def retrieve_all_volumes(self):

        volume_list = []
        page, per_page = 1, 10
        response = self.volumeapi.list_all_volumes(page=page, per_page=per_page)
        content = json.loads(response.content.decode("utf-8"))
        volume_list.extend(content["volumes"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.volumeapi.list_all_volumes(page=page, per_page=per_page)
                content = json.loads(response.content.decode("utf-8"))
                volume_list.extend(content["volumes"])
        except KeyError:
            pass

        # Build and return that Volume object array.
        volume_objects = []
        for volume_item in volume_list:
            newvolume = Volume()
            newvolume.attributes = VolumeAttributes(**volume_item)
            newvolume.arguments = VolumeArguments()
            #You need to actually retreive the last action for the volume object before creating an Action
            #newvolume.lastaction = Action()
            volume_objects.append(newvolume)
        return volume_objects

    def retrieve_all_volumes_by_name(self, name):
        volume_list = []
        page, per_page = 1, 10
        response = self.volumeapi.list_all_volumes_by_name(
            name=name, page=page, per_page=per_page
        )
        content = json.loads(response.content.decode("utf-8"))
        volume_list.extend(content["volumes"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.volumeapi.list_all_volumes_by_name(
                    name=name, page=page, per_page=per_page
                )
                content = json.loads(response.content.decode("utf-8"))
                volume_list.extend(content["volumes"])
        except KeyError:
            pass

        # Build and return that Volume object array.
        volume_objects = []
        for volume_item in volume_list:
            newvolume = Volume()
            newvolume.attributes = VolumeAttributes(**volume_item)
            newvolume.arguments = VolumeArguments()
            #You need to actually retreive the last action for the volume object before creating an Action
            #newvolume.lastaction = Action()
            volume_objects.append(newvolume)
        return volume_objects

    def retrieve_volume_by_id(self, id):
        if self.does_volume_id_exist(id):
            newvolume = Volume()
            response = self.volumeapi.retrieve_volume_by_id(id)
            content = json.loads(response.content.decode("utf-8"))
            volume_info = content["volume"]
            newvolume.attributes = VolumeAttributes(**volume_info)
            newvolume.arguments = VolumeArguments()
            #You need to actually retreive the last action for the volume object before creating an Action
            #newvolume.lastaction = Action()
            return newvolume
        else:
            raise ErrorVolumeNotFound(f"Volume {id} does not exist")

    def retrieve_volume_by_name_region(self, name, region):
        if self.does_volume_name_region_exist(name, region):
            newvolume = Volume()
            response = self.volumeapi.retrieve_volume_name_region(name, region)
            content = json.loads(response.content.decode("utf-8"))
            volume_info = content["volumes"][0]
            newvolume.attributes = VolumeAttributes(**volume_info)
            newvolume.arguments = VolumeArguments()
            #You need to actually retreive the last action for the volume object before creating an Action
            #newvolume.lastaction = Action()
            return newvolume
        else:
            raise ErrorVolumeNotFound(
                f"Volume name:{name}, region:{region} does not exist"
            )

    def retrieve_volumes_with_only_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        return_volumes = []
        volumes = self.retrieve_all_volumes()
        for volume in volumes:
            if set(list(tag)) == set(volume.attributes.tags):
                return_volumes.append(volume)
        if len(return_volumes) > 0:
            return return_volumes
        else:
            raise ErrorVolumeNotFound(
                f"No volumes containing all tags: {tag} were found."
            )

    def delete_volumes_with_only_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        try:
            volumes = self.retrieve_volumes_with_only_tags(tag)
            for volume in volumes:
                self.delete_volume(volume)
        except:
            pass

    def retrieve_volumes_with_all_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        return_volumes = []
        volumes = self.retrieve_all_volumes()
        for volume in volumes:
            if set(list(tag)).issubset(set(volume.attributes.tags)):
                return_volumes.append(volume)
        if len(return_volumes) > 0:
            return return_volumes
        else:
            raise ErrorVolumeNotFound(
                f"No volumes containing all tags: {tag} were found."
            )

    def delete_volumes_with_all_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        try:
            volumes = self.retrieve_volumes_with_all_tags(tag)
            for volume in volumes:
                self.delete_volume(volume)
        except:
            pass

    def retrieve_volumes_with_any_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        return_volumes = []
        volumes = self.retrieve_all_volumes()
        for volume in volumes:
            if not set(list(tag)).isdisjoint(set(volume.attributes.tags)):
                return_volumes.append(volume)
        if len(return_volumes) > 0:
            return return_volumes
        else:
            raise ErrorVolumeNotFound(
                f"No volumes containing any of the tags: {tag} were found."
            )

    def delete_volumes_with_any_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        try:
            volumes = self.retrieve_volumes_with_any_tags(tag)
            for volume in volumes:
                self.delete_volume(volume)
        except:
            pass

    def delete_volume(self, volume: Volume):
        """
        Given a Volume object, this method deletes the volume represnted by the object.

        Args:
            volume (volume): [description]
        """
        self.delete_volume_by_id(volume.attributes.id)

    def delete_volume_by_id(self, id):
        if self.does_volume_id_exist(id):
            response = self.volumeapi.delete_volume_id(id)

    def delete_volume_by_name_region(self, name=None, region=None):
        if (not name == None) and (not region == None):
            if self.does_volume_name_region_exist(name, region):
                self.volumeapi.delete_volume_name_region(name, region)

    def does_volume_id_exist(self, id):
        volumes = self.retrieve_all_volumes()
        for volume in volumes:
            if str(volume.attributes.id) == str(id):
                return True
        return False

    def does_volume_name_region_exist(self, name, region):
        volumes = self.retrieve_all_volumes()
        for volume in volumes:
            if (str(volume.attributes.name) == str(name)) and (
                str(volume.attributes.region["slug"]) == str(region)
            ):
                return True
        return False



class Volume:
    def __init__(self):
        self.arguments = VolumeArguments()
        self.attributes = VolumeAttributes()
        self.lastaction:Action = None
        self.volumeapi = Volumes()
        self.volume_manager = VolumeManager()
        self.action_manager = ActionManager()
        self.deleted=False
        
    def update(self):
        if not self.deleted==False:
            raise ErrorVolumeNotFound(f"{self.attributes.id} was deleted")
        """
        Updates the Volume attributes data class with the latest volume information at digital ocean.
        """
        response = self.volumeapi.retrieve_volume_by_id(self.attributes.id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            volume_data = dict(content["volume"])
            self.attributes = VolumeAttributes(**volume_data)

    #Actions are self updating, no need for these methods.
    #def update_volume_action(self):
    #    """
    #    Updates the Droplet lastaction data class with the latest droplet action information at digital ocean.
    #    """
    #    response = self.volumeapi.retrieve_volume_action(
    #        self.attributes.id, self.lastaction.id
    #    )
    #    if response:
    #        content = json.loads(response.content.decode("utf-8"))
    #        action_data = dict(content["action"])
    #        self.lastaction = VolumeLastAction(**action_data)#
    #
    #def update_on_active_action(self):
    #    """
    #    A freshly created droplet will need time to completely boot up and be active.
    #    Information like IP addresses are not available untill the droplet is active.
    #    Here we start a background thread that waits for the droplet to become active and then update the droplet attributes.
    #    """#
    #
    #    def update_action():
    #        while (self.lastaction.status == None) or (
    #            self.lastaction.status == "in-progress"
    #        ):
    #            if not self.lastaction.status in ["completed", "errored"]:
    #                time.sleep(10)
    #                self.update_volume_action()
    #            else:
    #                break

    #    thread = threading.Thread(target=update_action, args=())
    #    thread.start()


    def create_snapshot(self, name, tags=[]):
        id = self.attributes.id
        if not self.volume_manager.does_volume_id_exist(id):
            raise ErrorVolumeNotFound(f"Volume id:{id} not found.")
        volumename = self.attributes.name
        arguments = {}
        arguments["name"] = name
        arguments["tags"] = tags
        if self.volume_manager.does_volume_id_exist(id):
            newsnapshot = Snapshot()
            newsnapshot.arguments = SnapshotArguments(**arguments)
            response = self.volumeapi.create_snapshot_from_volume(id, name, tags)
            if response:
                content = json.loads(response.content.decode("utf-8"))
                snapshot_info = content["snapshot"]
                newsnapshot.attributes = SnapshotAttributes(**snapshot_info)
                return newsnapshot

        else:
            raise ErrorVolumeNotFound(
                f"Cant create snapshot from non existent volume {id}:{volumename}"
            )

    def retrieve_snapshots(self):
        # Buildlist of snapshots from api, but take in to account pagination
        snapshot_list = []
        page, per_page = 1, 10
        response = self.volumeapi.list_snapshots_for_volume(
            id, page=page, per_page=per_page
        )
        content = json.loads(response.content.decode("utf-8"))
        print(content)
        snapshot_list.extend(content["snapshots"])
        try:
            while content["links"]["pages"]["next"]:
                response = self.volumeapi.list_snapshots_for_volume(
                    id, page=page, per_page=per_page
                )
                content = json.loads(response.content.decode("utf-8"))
                snapshot_list.extend(content["snapshots"])
        except KeyError:
            pass

        # Build and return that Snapshot object array.
        snapshot_objects = []
        for snapshot_item in snapshot_list:
            newsnapshot = Snapshot()
            newsnapshot.attributes = SnapshotAttributes(**snapshot_item)
            newsnapshot.arguments = SnapshotArguments()
            snapshot_objects.append(newsnapshot)
        return snapshot_objects



    

    def detach_from_droplets(self):
        #If volume is attached to any droplets, we detach it from them.
        self.update()
        droplet_ids=self.attributes.droplet_ids
        if len(droplet_ids)>0:
            for droplet_id in droplet_ids:
                response = self.volumeapi.detach_volume_from_droplet(
                self.attributes.id, droplet_id
            )
            if response:
                content = json.loads(response.content.decode("utf-8"))
                action_data = dict(content["action"])
                newaction=Action(ActionAttributes(**action_data))
                self.action_manager.wait_for_action_completion(newaction)
                self.lastaction=newaction

        

    def resize(self,size_gigabytes):
        #size from 1GB to max 16,384GB
        if(size_gigabytes>16384):
            raise ErrorVolumeResizeValueTooLarge("Maximum volume resize value of 16384 GB has been requested.")
        #can only resize upwards
        current_size=self.attributes.size_gigabytes
        target_size=size_gigabytes
        if(target_size<=current_size):
            raise ErrorVolumeResizeDirection("You tried to shrink a volume, this isn't allowed. You can only increase a volumes size")

        response=self.volumeapi.resize_volume(self.attributes.id,size_gigabytes,self.attributes.region['slug'])
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction=Action(ActionAttributes(**action_data))
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction=newaction
