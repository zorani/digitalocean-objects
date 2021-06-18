from __future__ import annotations

from dataclasses import dataclass, field
from ..digitaloceanapi.droplets import Droplets
from ..digitaloceanapi.volumes import Volumes
from .action import *
from .snapshot import *
from .size import *
from .volume import *
from .account import *
from ..common.cloudapiexceptions import *
import json
import threading
import time
import re


@dataclass
class DropletSnapshotAttributes:
    id: int = None
    name: str = None
    distribution: str = None
    slug: str = None
    public: bool = None
    regions: list = field(default_factory=list)
    created_at: str = None
    min_disk_size: int = None
    type: str = None
    size_gigabytes: float = None


class DropletSnapshot:
    def __init__(self):
        self.attributes = DropletSnapshotAttributes()


class DropletManager:
    def __init__(self):
        self.dropletapi = Droplets()
        self.smanager = SnapshotManager()
        self.amanager = ActionManager()
        self.account_manager=AccountManager()

    def check_limit(self):
        droplet_limit = self.account_manager.droplet_limit()
        if not len(self.retrieve_all_droplets()) < droplet_limit:
            raise ErrorAccountDropletLimitReached
            (
                f"You have reached your droplet limit of {droplet_limit}"
            )

    def is_valid_droplet_name(self,droplet_name):
        #Double check hostname for valid chars
        re_is_valid_hostname=re.compile('^[a-zA-Z0-9.-]+$').search
        if not bool(re_is_valid_hostname(droplet_name)):
            raise ErrorDropletNameContainsInvalidChars(f"\"{droplet_name}\" is not a valid hostname, droplet names must contain only (a-z, A-Z, 0-9, . and -)")


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
        arguments = locals()
        del arguments["self"]


        self.is_valid_droplet_name(arguments['name'])
        self.check_limit()



        newdroplet = Droplet()
        newdroplet.arguments = DropletArguments(**arguments)
        response = self.dropletapi.create_new_droplet(**arguments)
        if response:
            #
            droplet_data = dict(json.loads(response.content.decode("utf-8"))["droplet"])
            newdroplet.attributes = DropletAttributes(**droplet_data)
        else:
            raise Exception(f"Could not create droplet {name}, {response.content}")
        return newdroplet

    def retrieve_droplet_by_id(self, id):
        """
        Returns a Droplet object containing attributes for a droplet with id.

        Args:
            id ([type]): [description]

        Returns:
            [Droplet]:A droplet object containing attributes for a droplet with object id.
        """
        if not self.does_droplet_id_exist(id):
            raise ErrorDropletNotFound(f"Droplet with id:{id} does not exists")
        newdroplet = Droplet(status="retrieve")
        response = self.dropletapi.retrieve_droplet_by_id(id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            droplet_data = dict(content["droplet"])
            newdroplet.attributes = DropletAttributes(**droplet_data)
        return newdroplet

    def retrieve_droplets_by_name(self, name):
        return_droplets = []
        droplets = self.retrieve_all_droplets()
        for droplet in droplets:
            if droplet.attributes.name == name:
                return_droplets.append(droplet)
        return return_droplets

    def retrieve_all_droplets(self):
        """
        Returns an array of Droplet objects, one for each droplet in digitalocean account.

        Returns:
            [type]: [description]
        """

        # Build list of droplets from api, but take in to account possible pagination.
        droplet_list = []
        page, per_page = 1, 10
        response = self.dropletapi.list_all_droplets(page=page, per_page=per_page)
        content = json.loads(response.content.decode("utf-8"))
        droplet_list.extend(content["droplets"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.dropletapi.list_all_droplets(
                    page=page, per_page=per_page
                )
                content = json.loads(response.content.decode("utf-8"))
                droplet_list.extend(content["droplets"])
        except KeyError:
            pass

        # Build and return that Droplet object array.
        droplet_objects = []
        for droplet_item in droplet_list:
            newdroplet = Droplet(status="retrieve")
            newdroplet.attributes = DropletAttributes(**droplet_item)
            droplet_objects.append(newdroplet)
        return droplet_objects

    # def retrieve_all_droplets_by_tag(self, tag_name=None):
    #    """
    #    Returns an array of Droplet objects, one for each droplet in digitalocean account.
    #
    #    Returns:
    #        [type]: [description]
    #    """
    #
    # If no tag has been provided, return no droplets
    #    if tag_name == None:
    #        return []

    # Build list of droplets from api, but take in to account possible pagination.
    #    droplet_list = []
    #    page, per_page = 1, 10
    #    response = self.dropletapi.list_all_droplets_by_tag(
    #        tag_name=tag_name, page=page, per_page=per_page
    #    )
    #    content = json.loads(response.content.decode("utf-8"))
    #    droplet_list.extend(content["droplets"])
    #    try:
    #        while content["links"]["pages"]["next"]:
    #            page = page + 1
    #            response = self.dropletapi.list_all_droplets(
    #                page=page, per_page=per_page
    #            )
    #            content = json.loads(response.content.decode("utf-8"))
    #            droplet_list.extend(content["droplets"])
    #    except KeyError:
    #        pass

    # Build and return that Droplet object array.
    #    droplet_objects = []
    #    for droplet_item in droplet_list:
    #        newdroplet = Droplet(status="retrieve")
    #        newdroplet.attributes = DropletAttributes(**droplet_item)
    #        droplet_objects.append(newdroplet)
    #    return droplet_objects

    def retrieve_droplets_with_only_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        return_droplets = []
        droplets = self.retrieve_all_droplets()
        for droplet in droplets:
            if set(list(tag)) == set(droplet.attributes.tags):
                return_droplets.append(droplet)
        if len(return_droplets) > 0:
            return return_droplets
        else:
            raise ErrorDropletNotFound(
                f"No droplets containing all tags: {tag} were found."
            )

    def delete_droplets_with_only_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        try:
            droplets = self.retrieve_droplets_with_only_tags(tag)
            for droplet in droplets:
                self.delete_droplet(droplet)
        except:
            pass

    def retrieve_droplets_with_all_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        return_droplets = []
        droplets = self.retrieve_all_droplets()
        for droplet in droplets:
            if set(list(tag)).issubset(set(droplet.attributes.tags)):
                return_droplets.append(droplet)
        if len(return_droplets) > 0:
            return return_droplets
        else:
            raise ErrorDropletNotFound(
                f"No droplets containing all tags: {tag} were found."
            )

    def delete_droplets_with_all_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        try:
            droplets = self.retrieve_droplets_with_all_tags(tag)
            for droplet in droplets:
                self.delete_droplet(droplet)
        except:
            pass

    def retrieve_droplets_with_any_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        return_droplets = []
        droplets = self.retrieve_all_droplets()
        for droplet in droplets:
            if not set(list(tag)).isdisjoint(set(droplet.attributes.tags)):
                return_droplets.append(droplet)
        if len(return_droplets) > 0:
            return return_droplets
        else:
            raise ErrorDropletNotFound(
                f"No droplets containing all tags: {tag} were found."
            )

    def delete_droplets_with_any_tags(self, tag: list):
        if isinstance(tag, str):
            tag = [tag]
        try:
            droplets = self.retrieve_droplets_with_any_tags(tag)
            for droplet in droplets:
                self.delete_droplet(droplet)
        except:
            pass

    def delete_droplet(self, droplet: Droplet):
        if not droplet.deleted==False:
            raise ErrorDropletNotFound(f"{droplet.attributes.id} was already deleted")
        self.delete_droplet_by_id(droplet.attributes.id)
        droplet.deleted=True 

    def delete_droplet_by_id(self, id):
        if self.does_droplet_id_exist(id):
            response = self.dropletapi.delete_droplet_id(id)

    #def delete_droplets_by_tag(self, tag_name=None):
    #    if not tag_name == None:
    #        response = self.dropletapi.delete_droplet_tag(tag_name=tag_name)

    
    def does_droplet_id_exist(self, id):
        droplets = self.retrieve_all_droplets()
        for droplet in droplets:
            if str(droplet.attributes.id) == str(id):
                return True
        return False


@dataclass
class DropletAttributes:
    id: int = None
    name: str = None
    memory: int = None
    vcpus: int = None
    disk: int = None
    locked: bool = None
    created_at: str = None
    status: str = None
    backup_ids: list = field(default_factory=list)
    snapshot_ids: list = field(default_factory=list)
    features: list = field(default_factory=list)
    region: object = field(default_factory=list)
    image: object = field(default_factory=list)
    size: object = field(default_factory=list)
    size_slug: str = None
    networks: object = field(default_factory=list)
    kernel: object = field(default_factory=list)
    next_backup_window: object = field(default_factory=list)
    tags: list = field(default_factory=list)
    volume_ids: list = field(default_factory=list)
    vpc_uuid: list = field(default_factory=list)


@dataclass
class DropletArguments:

    name: str = None
    region: str = None
    size: str = None
    image: object = None
    ssh_keys: list = field(default_factory=list)
    backups: bool = None
    ipv6: bool = None
    private_networking: bool = None
    vpc_uuid: str = None
    user_data: str = None
    monitoring: bool = None
    volumes: list = field(default_factory=list)
    tags: list = field(default_factory=list)


#@dataclass
#class DropletLastAction:
#    id: int = None
#    status: str = None
#    type: str = None
#    started_at: str = None
#    completed_at: str = None
#    resource_id: int = None
#    resource_type: str = None
#    region: object = None
#    region_slug: str = None


class Droplet:
    def __init__(self, status=None):
        self.arguments = DropletArguments()
        self.attributes = DropletAttributes()
        self.lastaction:Action = None
        self.attributes.status = status
        self.dropletapi = Droplets()
        self.volumeapi = Volumes()
        self.action_manager = ActionManager()
        self.size_manager = SizeManager()
        self.volume_manager = VolumeManager()
        self.snapshot_manager = SnapshotManager()
        self.droplet_manager = DropletManager()
        self.update_on_active_status()
        self.deleted=False

    def update(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        """
        Updates the Droplet attributes data class with the latest droplet information at digital ocean.
        """
        response = self.dropletapi.retrieve_droplet_by_id(self.attributes.id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            droplet_data = dict(content["droplet"])
            self.attributes = DropletAttributes(**droplet_data)

    def update_on_active_status(self):
        """
        A freshly created droplet will need time to completely boot up and be active.
        Information like IP addresses are not available untill the droplet is active.
        Here we start a background thread that waits for the droplet to become active and then update the droplet attributes.
        """

        def update_status():
            while not self.attributes.status == "active":
                if self.attributes.status == None:
                    time.sleep(10)
                elif self.attributes.status == "new":
                    self.update()
                    time.sleep(10)
                else:
                    break

        thread = threading.Thread(target=update_status, args=())
        thread.start()

    ###### Do we need to update droplet action, if action already updates itself

    # def update_droplet_action(self):
    #    """
    #    Updates the Droplet lastaction data class with the latest droplet action information at digital ocean.
    #    """
    #    response = self.dropletapi.retrieve_droplet_action(
    #        self.attributes.id, self.lastaction.id
    #    )
    #    if response:
    #        content = json.loads(response.content.decode("utf-8"))
    #        action_data = dict(content["action"])
    #        self.lastaction = DropletLastAction(**action_data)

    # def update_on_active_action(self):
    #    """
    #    A freshly created droplet will need time to completely boot up and be active.
    #    Information like IP addresses are not available untill the droplet is active.
    #    Here we start a background thread that waits for the droplet to become active and then update the droplet attributes.
    #    """

    #    def update_action():
    #        while (self.lastaction.status == None) or (
    #            self.lastaction.status == "in-progress"
    #        ):
    #            if not self.lastaction.status in ["completed", "errored"]:
    #                time.sleep(10)
    #                self.update_droplet_action()
    #            else:
    #                break
    #            if self.lastaction.status == "errored":
    #                raise ErrorActionFailed(
    #                    f"Action {self.attributes.id},{self.attributes.type} failed"
    #                )
    #
    #    thread = threading.Thread(target=update_action, args=())
    #    thread.start()

    def reboot(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        droplet_id = self.attributes.id
        response = self.dropletapi.reboot_droplet(droplet_id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_data)
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

    def powercycle(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        droplet_id = self.attributes.id
        response = self.dropletapi.powercycle_droplet(droplet_id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_data)
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

    def shutdown(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        droplet_id = self.attributes.id
        response = self.dropletapi.shutdown_droplet(droplet_id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_data)
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

    def poweroff(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        droplet_id = self.attributes.id
        response = self.dropletapi.poweroff_droplet(droplet_id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_data)
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

    def poweron(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        droplet_id = self.attributes.id
        response = self.dropletapi.poweron_droplet(droplet_id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_data)
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

    def rebuild(self, image):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        droplet_id = self.attributes.id
        response = self.dropletapi.rebuild_droplet(droplet_id, image)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_data)
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

    def rename(self, name):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        self.droplet_manager.is_valid_droplet_name(name)
        droplet_id = self.attributes.id
        response = self.dropletapi.rename_droplet(droplet_id, name)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_data)
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

    def create_snapshot(self, name):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        id = self.attributes.id
        response = self.dropletapi.create_snapshot_from_droplet(id, name)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action(ActionAttributes(**action_data))
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction
            #print(newaction.attributes.started_at)
            #print(newaction.attributes.completed_at)
            snapshot_objects=self.retrieve_snapshots()
            for snapshot_object in snapshot_objects:
                if (snapshot_object.attributes.name==name) and (snapshot_object.attributes.created_at==newaction.attributes.started_at):
                    return snapshot_object
            return None 

    def restore_droplet(self, image_id):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        id = self.attributes.id
        response = self.dropletapi.restore_droplet(id, image_id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action(ActionAttributes(**action_data))
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

    def resize_droplet(self, slug_size, disk_resize=False):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        # OK, if you try and resize to a smaller disk you will fail.
        desired_size = self.size_manager.retrieve_size(slug_size)
        target_disk_size = desired_size.attributes.disk
        current_disk_size = self.attributes.disk
        if target_disk_size < current_disk_size:
            raise ErrorDropletResizeDiskError(
                "You can't resize to a smaller disk, resize to same disk size with different RAM memory instead"
            )

        id = self.attributes.id
        response = self.dropletapi.resize_droplet(
            id, slug_size, disk_resize=disk_resize
        )
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction = Action()
            newaction.attributes = ActionAttributes(**action_data)
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction = newaction

            self.poweron()

    def delete(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        self.dropletapi.delete_droplet_id(self.attributes.id)
        self.deleted=True

    def retrieve_snapshots(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        id = self.attributes.id
        snapshot_list = []
        page, per_page = 1, 10
        response = self.dropletapi.list_snapshots_for_droplet(
            id=id, page=page, per_page=per_page
        )
        content = json.loads(response.content.decode("utf-8"))
        snapshot_list.extend(content["snapshots"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.dropletapi.list_snapshots_for_droplet(
                    id=id, page=page, per_page=per_page
                )
                content = json.loads(response.content.decode("utf-8"))
                snapshot_list.extend(content["snapshots"])
        except KeyError:
            pass
            #print(snapshot_list)
        # Build and return that Snapshot object array.
        dropletsnapshot_objects = []
        for snapshot_item in snapshot_list:
            newdropletsnapshot = DropletSnapshot()
            newdropletsnapshot.attributes = DropletSnapshotAttributes(**snapshot_item)
            dropletsnapshot_objects.append(newdropletsnapshot)
        return dropletsnapshot_objects

    def retrieve_snapshot_by_id(self,snapshot_id):
        snapshots=self.retrieve_snapshots()
        for snapshot in snapshots:
            if snapshot.attributes.id==snapshot_id:
                return snapshot
        return None 

    def retrieve_associated_volumes(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        self.update()
        volume_ids = self.attributes.volume_ids
        # build volume objects and add to list
        volume_objects = []
        for volume_id in volume_ids:
            newvolume = self.volume_manager.retrieve_volume_by_id(volume_id)
            volume_objects.append(newvolume)
        return volume_objects

    def count_associated_volumes(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        volumes = self.retrieve_associated_volumes()
        return len(volumes)

    def retrieve_associated_volume_snapshots(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        self.update() 
        volume_snapshot_ids = self.attributes.snapshot_ids
        # build volume objects and add to list
        volume_snapshot_objects = []
        for volume_snapshot_id in volume_snapshot_ids:
            newvolume_snapshot = self.snapshot_manager.retrieve_snapshot_id(
                volume_snapshot_id
            )
            volume_snapshot_objects.append(newvolume_snapshot)
        return volume_snapshot_objects

    def count_associated_volume_snapshots(self):
        if not self.deleted==False:
            raise ErrorDropletNotFound(f"{self.attributes.id} was deleted")
        volume_snapshots = self.retrieve_associated_volume_snapshots()
        return len(volume_snapshots)

    def attach_a_volume(self, target_volume:Volume):


        # Must check if the target_volume is in the same region
        if not self.attributes.region == target_volume.attributes.region:
            raise ErrorNotSameRegion(
                f"Volume {target_volume.attributes.id} not is same regions as Droplet {self.attributes.id}"
            )

        # Only 7 volumes allowed to be attached per droplet.
        self.update()
        if not self.count_associated_volumes() <=7 :
            raise ErrorDropletAttachedVolumeCountAlreadAtLimit(
                f"Droplet id:{self.attributes.id} already has the maximum of 7 attached volumes"
            )
        # Volumes can only be attached to one droplet
        ##remove volume from other droplets first
        target_volume.detach_from_droplets()

        response = self.volumeapi.attach_volume_to_droplet(
            target_volume.attributes.id, self.attributes.id,self.attributes.region['slug']
        )
        if response:
            content = json.loads(response.content.decode("utf-8"))
            action_data = dict(content["action"])
            newaction=Action(ActionAttributes(**action_data))
            self.action_manager.wait_for_action_completion(newaction)
            self.lastaction=newaction 
            self.update()
            target_volume.update()

    def detach_a_volume(self, target_volume:Volume):
        target_volume.detach_from_droplets()
        self.update()
        target_volume.update()




if __name__ == "__main__":
    dmanager = DropletManager()

    # a_droplet = dmanager.create_new_droplet(
    #    name="example.com",
    #    region="nyc3",
    #    size="s-1vcpu-1gb",
    #    image="ubuntu-16-04-x64",
    #    ssh_keys=[],
    #    backups=False,
    #    ipv6=True,
    #    user_data=None,
    #    private_networking=None,
    #    volumes=None,
    #    tags=["banabas"],
    # )

    # while not a_droplet.attributes.status == "active":
    #    time.sleep(5)
    #   print("waiting")

    # print("-----arguments-----")
    # print(a_droplet.arguments)
    # print("-------ATTRIBUTES-------------")
    # print(a_droplet.attributes)
    ## try:
    #    newdroplet = dmanager.retrieve_droplet_by_id(2496119371)
    # except DropletNotFound:
    #    print("Droplet wasnt found")
    # print(newdroplet.attributes)
    # print(newdroplet.arguments)
    # 249699371
    # droplets = dmanager.retrieve_all_droplets_by_tag("banabas")
    # for droplet in droplets:
    #    print(f"Deleteing droplet with id {droplet.attributes.id}")
    #    dmanager.delete_droplet(droplet)

    # print(dmanager.does_droplet_id_exist(249699371))

    # dmanager.delete_droplets_by_tag("banabas")
    droplets = dmanager.retrieve_droplets_by_name("example.com")
    for droplet in droplets:
        print(droplet.attributes.name)
        droplet.powercycle()
        while (droplet.lastaction.status == None) or (
            droplet.lastaction.status == "in-progress"
        ):
            time.sleep(5)
            print("waiting for action...")
        print(droplet.lastaction)
    print("finished")
