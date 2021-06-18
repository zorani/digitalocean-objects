<h1 align="center">digitalocean-objects</h1>
<p align="left"><b>everyone:</b> I wish, for once, to just have a simple object oriented experience with the api.</p>
<p align="left"><b>digitalocean-objects:</b> </p>

<p align="center">
<a href="https://github.com/zorani/digitalocean-objects"><img src="https://img.shields.io/github/forks/zorani/digitalocean-objects.svg?style=social&label=Fork"></a>
<a href="https://github.com/zorani/digitalocean-objects"><img src="https://img.shields.io/github/stars/zorani/digitalocean-objects.svg?style=social&label=Star"></a>
<a href="https://github.com/zorani/digitalocean-objects"><img src="https://img.shields.io/github/watchers/zorani/digitalocean-objects.svg?style=social&label=Watch"></a>
</p>



# Table of Contents

- [How to install](#how-to-install)
- [Configurations](#configurations)
- [OMG OMG SHOW ME SHOW ME HOW... NOW!!!](#omg-omg-show-me-show-me-how...-now!!!)
- [Account](#account)
	- [Account Manager](#account-manager)
		- [Retrieve Account Information](#retrieve-account-information)
- [Sizes](#sizes)
	- [Size Manager](#size-manager)
		- [Retrieve Sizes](#retrieve-sizes)
	- [Size Object](#size-object)
- [Regions](#regions)
	- [Region Manager](#region-manager)
		- [Retrieve All Regions](#retrieve-all-regions)
	- [Region Object](#region-object)
- [SSH Keys](#ssh-keys)
	- [SSH Key Manager](#ssh-key-manager)
		- [Retrieve All SSH Keys](#retrieve-all-ssh-keys)
		- [Create New Key](#create-new-key)
		- [Retrieve SSH Key Using ID](#retrieve-ssh-key-using-id)
	- [SSH Key Object](#ssh-key-object)
		- [Update SSH Key Name](#update-ssh-key-name)
		- [Delete SSH Key](#delete-ssh-key)
- [Droplets](#droplets)
	- [Droplet Manager](#droplet-manager)
		- [Create New Droplet](#create-new-droplet)
		- [Retrieve Droplet By ID](#retrieve-droplet-by-id)
		- [Retrieve Droplets By Name](#retrieve-droplets-by-name)
		- [Retrieve All Droplets](#retrieve-all-droplets)
		- [Retrieve Droplets With ANY tags](#retrieve-droplets-with-any-tags)
		- [Retrieve Droplets With ALL tags](#retrieve-droplets-with-all-tags)
		- [Retrieve Droplets With ONLY tags](#retrieve-droplets-with-only-tags)
		- [Delete Droplets With ANY tags](#delete-droplets-with-any-tags)
		- [Delete Droplets With ALL tags](#delete-droplets-with-all-tags)
		- [Delete Droplets With ONLY tags](#delete-droplets-with-only-tags)
		- [Delete Droplet By ID](#delete-droplet-by-id)
	- [Droplet Object](#droplet-object)
		- [Reboot](#reboot)
		- [Power Cycle](#power-cycle)
		- [Shutdown](#shutdown)
		- [Power Off](#power-off)
		- [Power On](#power-on)
		- [Rebuild](#rebuild)
		- [Rename](#rename)
		- [Create Snapshot](#create-snapshot)
		- [Retrieve Snapshots](#retrieve-snapshots)
		- [Retrieve Snapshot By ID](#retrieve-snapshot-by-id)
		- [Retrieve Associated Volumes](#retrieve-associated-volumes)
		- [Retrieve Associated Volume Snapshots](#retrieve-associated-volume-snapshots)
		- [Attach A Volume](#attach-a-volume)
		- [Detach A Volume](#detach-a-volume)
		- [Restore Droplet](#restore-droplet)
		- [Resize Droplet](#resize-droplet)
		- [Delete Snapshot](#delete-snapshot)
- [Block Storage (Volumes)](#block-storage-(volumes))
	- [Volume Manager](#volume-manager)
		 - [Create New Volume ](#create-new-volume)
		- [Retrieve All Volumes](#retrieve-all-volumes)
		- [Retrieve All Volumes By Name](#retrieve-all-volumes-by-name)
		- [Retrieve Volume By ID](#retrieve-volume-by-id)
		- [Retrieve Volume By Name And Region](#retrieve-volume-by-name-and-region)
		- [Retrieve Volumes With ANY Tags](#retrieve-volumes-with-any-tags)
		- [Retrieve Volumes With ALL Tags](#retrieve-volumes-with-all-tags)
		- [Retrieve Volumes With ONLY Tags](#retrieve-volumes-with-only-tags)
		- [Delete Volume By ID](#delete-volume-by-id)
		- [Delete Volume By Name And Region](#delete-volume-by-name-and-region)
		- [Delete Volumes With ANY Tags](#delete-volumes-with-any-tags)
		- [Delete Volumes With ALL Tags](#delete-volumes-with-all-tags)
		- [Delete Volumes With ONLY Tags](#delete-volumes-with-only-tags)
	- [Volume Object](#volume-object)
		- [Create Snapshot](#create-snapshot)
		- [Retrieve Snapshots](#retrieve-snapshots)
		- [Detach From Droplets](#detach-from-droplets)
		- [Resize Volume](#resize-volume)
- [Snapshots](#snapshots)
	- [Snapshot Manager](#snapshot-manager)
		- [Retrieve All Snapshots](#retrieve-all-snapshots)
		- [Retrieve All Droplet Snapshots](#retrieve-all-droplet-snapshots)
		- [Retrieve All Volume Snapshots](#retrieve-all-volume-snapshots)
		- [Retrieve Snapshot By ID](#retrieve-snapshot-by-id)
	- [Snapshot Object](#snapshot-object)
		- [Delete Snapshot](#delete-snapshot)
- [Floating IPs](#floating-ips)
	- [Floating IP Manager](#floating-ip-manager)
		- [Retrieve All Floating IPs](#retrieve-all-floating-ips)
		- [Create New Floating IP](#create-new-floating-ip)
		- [Create Region Reserve IP](#create-region-reserve-ip)
		- [Retrieve Floating IP](#retrieve-floating-ip)
	- [Floating IP Object](#floating-ip-object)
		- [Delete Floating IP](#delete-floating-ip)
		- [Unassign Floating IP](#unassign-floating-ip)
		- [Retrieve All IP Actions](#retrieve-all-ip-actions)
		- [Retrieve Existing IP Action](#retrieve-existing-ip-action)
- [Actions](#actions)
	- [Action Manager](#action-manager)
		- [Retrieve All Actions](#retrieve-all-actions)
		- [Retrieve Action](#retrieve-action)
	- [Action Object](#action-object)
- [Exceptions](#exceptions)
    - [Droplet Exceptions](#droplet-exceptions)
    - [Volume Exceptions](#volume-exceptions)
    - [Snapshot Exceptions](#snapshot-exceptions)
    - [Action Exceptions](#action-exceptions)
    - [Region Exceptions](#region-exceptions)
    - [Floating IP Exceptions](#floating-ip-exceptions)
    - [SSH Key Exceptions](#ssh-key-exceptions)

# How to install

You can install digitalocean-objects using **pip3**

    pip3 install -U digitalocean-objects

or if you prefer install from a cloned git hub repo, from the root of the repo:

    pip3 install -e ./

**[⬆ back to top](#table-of-contents)**

# Configurations

## Token

Set the DIGITALOCEAN_ACCESS_TOKEN environment variable with your api key.

    export DIGITALOCEAN_ACCESS_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

## api connection settings

You don't need to look too deeply here, this is for information only.

digitalocean-objects is powered by a baserestapi class from the following project.

https://github.com/zorani/cloudapi/blob/main/cloudapi/baserestapi.py

digitalocean-objects/digitaloceanapi/digitaloceanapiconnection.py inherits baserestapi, 
baseresapi takes care of all the tricky rate limiting.

Inside /digitaloceanapiconnection.py you will find
a 'callrateperhour' variable set to the current digital ocean limit of 5000.
digitalocean-objects converts 'callrateperhour' to seconds between requests.

You will also see the following variables.

geometric_delay_multiplier: If a request fails, the 'seconds between requests' is increased by multiplying by this number.

maximum_geometric_delay_multiplicaiton: How many times should you increase the 'seconds between requests' before considering it a fail.

maximum_failed_attempts: a failed attempt is put to the back of an internal queue for a retry. how many failed attempts are allowed before
                         returning the response with failure codes and content.

```python
        BaseRESTAPI.__init__(
            self,
            baseurl="https://api.digitalocean.com",
            callrateperhour=5000,
            geometric_delay_multiplier=2,
            maximum_geometric_delay_multiplications=6,
            maximum_failed_attempts=3,
        )
```

**[⬆ back to top](#table-of-contents)**

# OMG OMG SHOW ME SHOW ME HOW... NOW!!!

Okay!! Okay!!  Here is a quick start example!

Look how easy it is to work with digitaloceanobjects...

...read the code comments...

```python3
#!/usr/bin/env python3

from digitaloceanobjects import Droplet, DropletManager
from digitaloceanobjects import Volume, VolumeManager

#Create a droplet manager, to you know... manage your droplets.
droplet_manager = DropletManager()

#Create a new droplet.
my_brand_new_droplet = droplet_manager.create_new_droplet(
    name="test-droplet",
    region="ams3",
    size="s-1vcpu-1gb",
    image="ubuntu-16-04-x64",
    tags=["digitalocean", "objects", "are", "great"],
)

#What? Done already?
#Yup... now output the droplet details.
print(type(my_brand_new_droplet))
print(my_brand_new_droplet.attributes)

#Want to attache a volume? No problem...

#Create a volume manager.
volume_manager = VolumeManager()

#You'll need a volume, so lets create a new volume.
my_brand_new_volume = volume_manager.create_new_volume(
    size_gigabytes=10,
    name="test-volume",
    region="ams3",
    description="BlockStoreFor Examples",
    filesystem_type="ext4",
    filesystem_label="example",
    tags=["is", "it", "really", "this", "easy"],
)

#Well... damn that was easy. Peek at the volume object and the attributes. Nice.
print(type(my_brand_new_volume))
print(my_brand_new_volume.attributes)

#So, now just ask your droplet to attach your new volume.
my_brand_new_droplet.attach_a_volume(my_brand_new_volume)

#Still don't beleive how easy this was? Check the droplet attributes, you will now have a volume id attached to it.
print(my_brand_new_droplet.attributes.volume_ids)
```

Hope you're happy...

... now read the rest of the documentation to see what other amazing things you can do!

**[⬆ back to top](#table-of-contents)**

# Account
## Account Manager
```python
from digitaloceanobjects import AccountManager
account_manager=AccountManager()
```
### Retrieve Account Information
```python
droplet_limit = account_manager.droplet_limit()

floating_ip_limit = account_manager.floating_ip_limit()

volume_limit = account_manager.volume_limit()

email = account_manager.email()

email_verified = account_manager.email_verified()

uuid = account_manager.uuid()

status = account_manager.status()

status_message = account_manager.status_message()
```
**[⬆ back to top](#table-of-contents)**

# Sizes
```python
from digitaloceanobjects import Size, SizeManager
```
## Size Manager
```python
size_manager=SizeManager()
```
### Retrieve Sizes
```python
list_of_size_objects=size_manager.retrieve_sizes()
```

## Size Object
```python
class Size:
    def __init__(self):
        self.attributes = SizeAttributes()
```

```python
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
```

**[⬆ back to top](#table-of-contents)**

# Regions
```python
from digitaloceanobjects import Region, RegionManager
```
## Region Manager
```python
region_manager = RegionManager()
```
### Retrieve All Regions
```python
list_of_region_objects = region_manager.retrieve_all_regions()
```

## Region Object
```python
class Region:
    def __init__(self):
        self.attributes = RegionAttributes()
```
```python
@dataclass
class RegionAttributes:
    slug: str = None
    name: str = None
    sizes: list = field(default_factory=list)
    available: bool = None
    features: list = field(default_factory=list)
```
**[⬆ back to top](#table-of-contents)**

# SSH Keys
```python
from digitaloceanobjects import SSHkey, SSHkeyManager
```
## SSH Key Manager
```python
sshkey_manager = SSHkeyManager()
```
### Retrieve All SSH Keys
```python
list_of_sshkey_objects=sshkey_manager.retrieve_all_sshkeys()
```
### Create New Key
```python
sshkey_object=sshkey_manager.create_new_key(name:str, public_key:str)
```
### Retrieve SSH Key Using ID
```python
sshkey_object=sshkey_manager.retrieve_sshkey_with_id(id:int)
```
## SSH Key Object
```python
sshkey_object=SSHkey()
```

```python
class SSHkey:
    def __init__(self):
        self.attributes = SSHkeyAttributes()
```
```python
@dataclass
class SSHkeyAttributes:
    id: str = None
    fingerprint: str = None
    public_key: str = None
    name: str = None
```
### Update SSH Key Name

```python
sshkey_object.update_name(name:str)
```
### Delete SSH Key
```python
sshkey_object.delete()
```
**[⬆ back to top](#table-of-contents)**

# Droplets
```python
from digitaloceanobjects import Droplet, DropletManager
```
## Droplet Manager
```python
droplet_manager = DropletManager()
```
### Create New Droplet
```python
droplet_object = droplet_manager.create_new_droplet(
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
						tags=["bananas"],
					)
```
### Retrieve Droplet By ID
```python
droplet_object = droplet_manager.retrieve_droplet_by_id(id:int)
```
### Retrieve Droplets By Name
```python
droplet_object = droplet_manager.retrieve_droplet_by_name(name:str)
```
### Retrieve All Droplets
```python
list_of_droplet_objects = droplet_manager.retrieve_all_droplets()
```
### Retrieve Droplets With ANY tags
```python
list_of_droplet_objects = droplet_manager.retrieve_droplets_with_any_tags(tag:list)
```
### Retrieve Droplets With ALL tags
```python
list_of_droplet_objects = droplet_manager.retrieve_droplets_with_all_tags(tag:list)
```
### Retrieve Droplets With ONLY tags
```python
list_of_droplet_objects = droplet_manager.retrieve_droplets_with_only_tags(tag:list)
```
### Delete Droplets With ANY tags
```python
droplet_manager.delete_droplets_with_any_tags(tag:list)
```
### Delete Droplets With ALL tags
```python
droplet_manager.delete_droplets_with_all_tags(tag:list)
```
### Delete Droplets With ONLY tags
```python
droplet_manager.delete_droplets_with_only_tags(tag:list)
```
### Delete Droplet By ID
```python
droplet_manager.delete_droplet_by_id(id:int)
```
**[⬆ back to top](#table-of-contents)**
## Droplet Object
```python
droplet_object=Droplet()
```
```python
class Droplet:
    def __init__(self, status=None):
        self.attributes = DropletAttributes()
        self.attributes.status = status
        self.deleted=False
        ...
```
```python
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
```
### Reboot
```python
droplet_object.reboot()
```
### Power Cycle
```python
droplet_object.powercycle()
```
### Shutdown
```python
droplet_object.shutdown()
```
### Power Off
```python
droplet_object.poweroff()
```
### Power On
```python
droplet_object.poweron()
```
### Rebuild
```python
droplet_object.rebuild(img:str)
```
### Rename
```python
droplet_object.rename(name:str)
```
### Create Snapshot
```python
dropletsnapshot_object = droplet_object.createsnapshot(name:str)
```
```python
class DropletSnapshot:
    def __init__(self):
        self.attributes = DropletSnapshotAttributes()
```
```python
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
```

### Retrieve Snapshots
```python
list_of_dropletsnapshot_objects = droplet_object.retrieve_snapshots()
```

### Retrieve Snapshot By ID
Only searches snapshots associated to droplet.
```python
dropletsnapshot_object = droplet_object.retrieve_snapshot_by_id(id:int)
```


### Retrieve Associated Volumes
```python
list_of_volume_objects = droplet_object.retrieve_associated_volumes()
```
### Retrieve Associated Volume Snapshots
```python
list_of_volume_snapshot_objects = droplet_object.retrieve_associated_volume_snapshots()
```
### Attach A Volume
```python
droplet_object.attach_a_volume(target_volume:Volume)
```
### Detach A Volume
```python
droplet_object.detach_a_volume(target_volume:Volume)
```
### Restore Droplet
```python
droplet_object.restore_droplet(image_id:int)
```
### Resize Droplet
If  you set ``` disk=False``` only the RAM will be increased.
If you set ```disk=True``` the disk size will be upgraded, and you will not be able to shrink your droplet down to it's previous RAM size.
```python
droplet_object.resize_droplet(
				slug_size='s-1vcpu-2gb',
				disk_resize=False
				)
```
### Delete Snapshot
```python
droplet_object.delete()
```
Deletes droplet from your account.
Sets ``` droplet_object.deleted=False``` so object methods will no longer work.

**[⬆ back to top](#table-of-contents)**

# Block Storage (Volumes)
```python
from digitaloceanobjects import Volume, VolumeManager
```
## Volume Manager
```python
volume_manager = VolumeManager()
```
### Create New Volume 
```python
volume_object = volume_manager.create_new_volume(
	        size_gigabytes=10,
	        name="testingavolume",
	        region="ams3",
	        description="BlockStoreExample",
	        filesystem_type="ext4",
	        filesystem_label="example",
	        tags=["banana"],
	    )
```
### Retrieve All Volumes
```python
list_of_volume_objects=volume_manager.retrieve_all_volumes()
```

### Retrieve All Volumes By Name
```python
list_of_volume_objects=volume_manager.retrieve_all_volumes_by_name(name:str)
```
### Retrieve Volume By ID
```python
volume_object=volume_manager.retrieve_volume_by_id(id:int)
```
### Retrieve Volume By Name And Region
```python
volume_object=volume_manager.retrieve_volume_by_name_region(
											name:str,
											region:str
										)
```
### Retrieve Volumes With ANY Tags
```python
list_of_volume_objects=volume_manager.retrieve_volumes_with_any_tags(tag:list)
```
### Retrieve Volumes With ALL Tags
```python
list_of_volume_objects=volume_manager.retrieve_volumes_with_all_tags(tag:list)
```
### Retrieve Volumes With ONLY Tags
```python
list_of_volume_objects=volume_manager.retrieve_volumes_with_only_tags(tag:list)
```
### Delete Volume By ID
```python
volume_manager.delete_volumes_by_id(id:int)
```


### Delete Volume By Name And Region
```python
volume_manager.delete_volume_by_name_region(
								name:str,
								region:str
							)
```


### Delete Volumes With ANY Tags
```python
volume_manager.delete_volumes_with_any_tags(tag:list)
```
### Delete Volumes With ALL Tags
```python
volume_manager.delete_volumes_with_all_tags(tag:list)
```
### Delete Volumes With ONLY Tags
```python
volume_manager.delete_volumes_with_only_tags(tag:list)
```

**[⬆ back to top](#table-of-contents)**

## Volume Object
```python
volume_object=Volume()
```
```python
class Volume:
    def __init__(self):
        self.attributes = VolumeAttributes()
        self.deleted=False
        ...
```
```python
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
```
### Create Snapshot
```python
snapshot_object=volume_object.create_snapshot(
						name:str,
						tags:list
					)
```
### Retrieve Snapshots
```python
list_of_snapshot_objects=volume_object.retrieve_snapshots()
```
### Detach From Droplets
```python
volume_object.detach_from_droplets()
```
### Resize Volume
```python
volume_object.resize(size_gigabytes:int)
```

**[⬆ back to top](#table-of-contents)**

# Snapshots
```python
from digitaloceanobjects import Snapshot, SnapshotManager
```
## Snapshot Manager
```python
snapshot_manager=SnapshotManager()
```
### Retrieve All Snapshots
```python
list_of_snapshot_objects=snapshot_manager.retrieve_all_snapshots()
```
### Retrieve All Droplet Snapshots
```python
list_of_snapshot_objects=snapshot_manager.retrieve_all_droplet_snapshots()
```
### Retrieve All Volume Snapshots
```python
list_of_snapshot_objects=snapshot_manager.retrieve_all_volume_snapshots()
```
### Retrieve Snapshot By ID
```python
snapshot_object=snapshot_manager.retrieve_snapshots_id(id:int)
```
**[⬆ back to top](#table-of-contents)**
## Snapshot Object
```python
snapshot_object=Snapshot()
```
```python
class Snapshot:
    def __init__(self):
        self.attributes = SnapshotAttributes()
		...
```

```python
@dataclass
class SnapshotAttributes:
    id: str = None
    name: str = None
    created_at: str = None
    regions: list = field(default_factory=list)
    resource_id: str = None
    resource_type: str = None
    min_disk_size: int = None
    size_gigabytes: float = None
    tags: list = field(default_factory=list)
```
### Delete Snapshot
```python
snapshot_object.delete()
```
**[⬆ back to top](#table-of-contents)**

# Floating IPs
```python
from digitaloceanobjects import FloatingIP, FloatingIPManager
```
## Floating IP Manager
```python
floatingip_manager=FloatingIPManager()
```
### Retrieve All Floating IPs
```python
list_of_floatingip_objects=floatingip_manager.retrieve_all_floating_ips()
```
### Create New Floating IP
Creates a floating IP and attaches it straight to the mentioned droplet.
```python
floatingip_object=floatingip_manager.create_new_floating_ip(droplet_object:Droplet)
```
### Create Region Reserve IP
```python
floatingip_object=floatingip_manager.reserve_ip_for_region(region_slug:str)
```
### Retrieve Floating IP
```python
floatingip_object=floatingip_manager.retrieve_floating_ip(ip:int)
```
**[⬆ back to top](#table-of-contents)**
## Floating IP Object
```python
floatingip_object=FloatingIP()
```
```python
class FloatingIP:
    def __init__(self):
        self.attributes = FloatingIPAttributes()
		...
```
```python
@dataclass
class FloatingIPAttributes:
    ip: str = None
    region: object = None
    droplet: object = None
    locked: bool = None
```
### Delete Floating IP
```python
floatingip_object.delete()
```
### Unassign Floating IP]
```python
floatingip_object.unassign()
```
### Retrieve All IP Actions
```python
list_of_action_objects=floatingip_object.retrieve_all_actions()
```
### Retrieve Existing IP Action
```python
action_object=floatingip_object.retrieve_existing_actions(action_id:int)
```
**[⬆ back to top](#table-of-contents)**

# Actions
```python
from digitaloceanobjects import Action, ActionManager
```
## Action Manager
```python
action_manager=ActionManager()
```
### Retrieve All Actions
```python
list_of_action_objects=action_manager.retrieve_all_actions()
```
### Retrieve Action
```python
action_object=action_manager.retrieve_action(action_id:int)
```
## Action Object
```python
action_object=Action()
```
```python
class Action:
    def __init__(self, action_attributes: ActionAttributes):
        self.attributes = action_attributes
		'''
```
```python
@dataclass
class ActionAttributes:
    id: int = None
    status: str = None
    type: str = None
    started_at: str = None
    completed_at: str = None
    resource_id: int = None
    resource_type: str = None
    region: object = None
    region_slug: str = None
```

**[⬆ back to top](#table-of-contents)**

# Exceptions

## Droplet Exceptions
```python
ErrorDropletNotFound
ErrorDropletNameContainsInvalidChars
ErrorDropletSlugSizeNotFound
ErrorDropletResizeDiskError
ErrorAccountDropletLimitReached
ErrorDropletAttachedVolumeCountAlreadAtLimit
```
## Volume Exceptions
```python
ErrorVolumeAlreadyExists
ErrorVolumeNotFound
ErrorVolumeResizeValueTooLarge
ErrorVolumeResizeDirection
ErrorAccountVolumeLimitReached
```

## Snapshot Exceptions
```python
ErrorSnapshotNotFound
```
## Action Exceptions
```python
ErrorActionDoesNotExists
ErrorActionFailed
```
## Region Exceptions
```python
ErrorNotSameRegion
ErrorRegionDoesNotExist
```
## Floating IP Exceptions
```python
ErrorAccountFloatingIPLimitReached
ErrorFloatingIPDoesNotExists
ErrorDropletAlreadyHasFloatingIP
```
## SSH Key Exceptions
```python
ErrorSSHkeyDoesNotExists
```

**[⬆ back to top](#table-of-contents)**