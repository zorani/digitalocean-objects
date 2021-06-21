<h1 align="center">digitalocean objects (pip3 install digitaloceanobjects)</h1>
<p align="left"><b>everyone:</b> I wish, for once, to just have a simple object oriented experience with the api.</p>
<p align="left"><b>digitaloceanobjects:</b> </p>

<p align="center">
<a href="https://github.com/zorani/digitalocean-objects"><img src="https://img.shields.io/github/forks/zorani/digitalocean-objects.svg?style=social&label=Fork"></a>
<a href="https://github.com/zorani/digitalocean-objects"><img src="https://img.shields.io/github/stars/zorani/digitalocean-objects.svg?style=social&label=Star"></a>
<a href="https://github.com/zorani/digitalocean-objects"><img src="https://img.shields.io/github/watchers/zorani/digitalocean-objects.svg?style=social&label=Watch"></a>
</p>

Please visit <a href="https://github.com/zorani/digitalocean-objects">GitHub</a> page for documentation that has navigation that works.

# Table of Contents

- [How to install](#how-to-install)
- [Configurations](#configurations)
- [OMG OMG SHOW ME SHOW ME HOW... NOW!!!](#omg-omg-show-me-show-me-how-now)
- [Blocking Wonderful Blocking](#blocking-wonderful-blocking)
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
		- [Delete Droplet](#delete-droplet)
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

Here are your options.

## Install from pypi repository

The most popular way is to install the latest package available on pypi.

You can install digitaloceanobjects using **pip3**

    pip3 install -U digitaloceanobjects

You can uninstall if you like using,

    pip3 uninstall digitaloceanobjects

## Install from the cloned git hub repo

There are a few ways to install this python package from a clone of its github repo.
Check out a copy and try the following...

### Build a .tar.gz install package

From the root of the repo build a repo, and check the repo.

    python3 setup.py sdist
    twine check dist/*

Check the newly created dist directory for newly created .tar.gz files.
This is your .tar.gz package and you can install using...

    pip3 install ./dist/digitaloceanobjects-0.0.17.tar.gz

You can still uninstall using the same commands,

    pip3 uninstall digitaloceanobjects

### Install using the setup.py file

!WARNING! Install does not track which files, and where they are placed.
So, you need to keep a record of there python3 does this.

This is how... from the github repo root directory.

    sudo python3 setup.py install --record files.txt

You can uninstall using by playing back that files.txt file,

    sudo xargs rm -rf < files.txt

### Local interactive install

Using this method you can modify this packages code and have changes immediately available.
Perfect for if you want to tinker with the library, poke around and contribute to the project.

From the cloned repository root directory.

    pip3 install -e ./

You can uninstall using the usual command,

    pip3 uninstall digitaloceanobjects

**[⬆ back to top](#table-of-contents)**

# Configurations

## Token

Set the DIGITALOCEAN_ACCESS_TOKEN environment variable with your api key.

    export DIGITALOCEAN_ACCESS_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

## api connection settings

You don't need to look too deeply here, this is for information only.

digitaloceanobjects is powered by a baserestapi class from the following project.

https://github.com/zorani/cloudapi/blob/main/cloudapi/baserestapi.py

digitaloceanobjects/digitaloceanapi/digitaloceanapiconnection.py inherits baserestapi, 
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

# OMG OMG SHOW ME SHOW ME HOW NOW

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

# Blocking Wonderful Blocking

Did you notice in the quick start example above we didn't at any point check to see if the droplet, or the volume were ready and available?

Well... that's because digitaloceanobjects is 'blocking', it waits for an operation on digital ocean to complete before returning.

You can code away, without any worries.

For example, digitaloceanobjects will wait for a droplet to be ready before any further actions are applied to it. You can't attach a volume to a droplet that hasn't finished setting up.

If you want to setup multiple droplets concurrently you should thread your droplet set up script so you're not waiting on independent services.

# Account
Retrieve information about your current digital ocean account.


```python
from digitaloceanobjects import AccountManager
```


## Account Manager
```python
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
The [sizes](#https://developers.digitalocean.com/documentation/v2/#sizes) objects represent different packages of hardware resources that can be used for Droplets. When a Droplet is created, a size must be selected so that the correct resources can be allocated.

Each size represents a plan that bundles together specific sets of resources. This includes the amount of RAM, the number of virtual CPUs, disk space, and transfer. The size object also includes the pricing details and the regions that the size is available in.

Import the size object, and the sizemanager.

```python
from digitaloceanobjects import Size, SizeManager
```
## Size Manager

The size manager contains methods to query information about available sizes on digital ocean.

```python
size_manager=SizeManager()
```
### Retrieve Sizes
```python
list_of_size_objects=size_manager.retrieve_sizes()
```

## Size Object
Size objects contains an attributes data class with the standard digital ocean [size attributes](https://developers.digitalocean.com/documentation/v2/#sizes).

The size objects worked on by the above manager contain a data class with attributes describing the available digital ocean sizes.

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

A region in DigitalOcean represents a datacenter where Droplets can be deployed and images can be transferred.

Each region represents a specific datacenter in a geographic location. Some geographical locations may have multiple "regions" available. This means that there are multiple datacenters available within that area.

Import the digitaloceanobject Region and RegionManger to interact with Regions.

```python
from digitaloceanobjects import Region, RegionManager
```
## Region Manager

Create a region manager.
```python
region_manager = RegionManager()
```
### Retrieve All Regions
Retrieve a list of region objects.
```python
list_of_region_objects = region_manager.retrieve_all_regions()
```

## Region Object

Region objects contains an attributes data class with the standard digital ocean [region attributes](https://developers.digitalocean.com/documentation/v2/#regions).


```python
class Region:
    def __init__(self):
        self.attributes = RegionAttributes()
        ...
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
[SSH Keys](https://developers.digitalocean.com/documentation/v2/#ssh-keys). DigitalOcean allows you to add SSH public keys to the interface so that you can embed your public key into a Droplet at the time of creation. Only the public key is required to take advantage of this functionality.

Import the digitaloceanobject SSHKey and SSHKeyManger to interact with SSH Keys.



```python
from digitaloceanobjects import SSHKey, SSHKeyManager
```
## SSH Key Manager

Create an SSH key manager.

```python
sshkey_manager = SSHKeyManager()
```
### Retrieve All SSH Keys

Returns a list of SSHKey objects each containing details of existing keys.
```python
list_of_sshkey_objects=sshkey_manager.retrieve_all_sshkeys()
```
### Create New Key
'upload' a new key to digital ocean by providing your public key, and an easy to remember name.

Returns an SSHKey object with details of your new key stored in it's attribute data class.
```python
sshkey_object=sshkey_manager.create_new_key(name:str, public_key:str)
```
### Retrieve SSH Key Using ID

Each SSH Key has an ID.  Using this ID you can retrieve information on an existing SSH Key.

Returns an SSHKey object with details of your existing key stored in it's attribute data class.

```python
sshkey_object=sshkey_manager.retrieve_sshkey_with_id(id:int)
```
## SSH Key Object

SSH Key objects contains an attributes data class with the standard digital ocean [SSH Key attributes](https://developers.digitalocean.com/documentation/v2/#ssh-keys).



```python
sshkey_object=SSHKey()
```

```python
class SSHKey:
    def __init__(self):
        self.attributes = SSHKeyAttributes()
		...
```
```python
@dataclass
class SSHKeyAttributes:
    id: str = None
    fingerprint: str = None
    public_key: str = None
    name: str = None
```

To work on your digital ocean ssh keys first retrieve your ssh key objects using the ssh key object manager.  Then apply the objects following methods.

### Update SSH Key Name


Then call the objects update name method with your new ssh key name.

```python
sshkey_object.update_name(name:str)
```
### Delete SSH Key

You can delete an ssh key by calling the objects delete method.

```python
sshkey_object.delete()
```
**[⬆ back to top](#table-of-contents)**

# Droplets

A  [Droplet](https://www.digitalocean.com/docs/droplets/)  is a DigitalOcean virtual machine. 

Import the digitaloceanobject Droplet and DropletManger to interact with or create new droplets.

```python
from digitaloceanobjects import Droplet, DropletManager
```
## Droplet Manager

Create a droplet manager.
```python
droplet_manager = DropletManager()
```
### Create New Droplet

To create a new droplet use the following method supplying your desired droplet [Attribute Values](https://developers.digitalocean.com/documentation/v2/#create-a-new-droplet).

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

You can retreive an existing droplet by calling the following method and supplying the droplets id.

A droplet object will be returned. The droplet object will contain the standard digital ocean [droplet attributes](https://developers.digitalocean.com/documentation/v2/#droplets).

```python
droplet_object = droplet_manager.retrieve_droplet_by_id(id:int)
```
### Retrieve Droplets By Name
Many droplets can have the same name.

To retrieve a list of droplet objects that have a particular name use the following method supplying your name.

```python
list_of_droplet_objects = droplet_manager.retrieve_droplet_by_name(name:str)
```
### Retrieve All Droplets

To retrieve all droplets in your account apply the following method.

A list of droplet objects will be returned.
```python
list_of_droplet_objects = droplet_manager.retrieve_all_droplets()
```
### Retrieve Droplets With ANY tags

You can tag droplets with as many tags as you like.

This method will return a list of digital ocean objects that contain any of the tags you provide in a list.

```python
list_of_droplet_objects = droplet_manager.retrieve_droplets_with_any_tags(tag:list)
```
### Retrieve Droplets With ALL tags

This method will return a list of droplet objects, but only throse droplets that
have at least all of the tags that you specify in a list of tags.

```python
list_of_droplet_objects = droplet_manager.retrieve_droplets_with_all_tags(tag:list)
```
### Retrieve Droplets With ONLY tags

This method will return a list of droplet objects that exactly match a list of tags that you specify.

```python
list_of_droplet_objects = droplet_manager.retrieve_droplets_with_only_tags(tag:list)
```
### Delete Droplets With ANY tags

You can also delete droplets by tags.

This method allows you to delete all droplets that contain any, one or more, of a list of tags that you specify.

```python
droplet_manager.delete_droplets_with_any_tags(tag:list)
```
### Delete Droplets With ALL tags

This method will delete any droplets that contain all, at least all, of the tags that you specify.

```python
droplet_manager.delete_droplets_with_all_tags(tag:list)
```
### Delete Droplets With ONLY tags

This method will delete droplets that match exactly a tag list that you specify.
```python
droplet_manager.delete_droplets_with_only_tags(tag:list)
```
### Delete Droplet By ID

The droplet manager allowes you to request droplet deletion by supplying a droplet id.

You might prefer to delete a droplet by calling a droplet objects delete method directly though.

```python
droplet_manager.delete_droplet_by_id(id:int)
```
**[⬆ back to top](#table-of-contents)**
## Droplet Object

Droplet objects contains an attributes data class with the standard digital ocean [droplet attributes](https://developers.digitalocean.com/documentation/v2/#droplets).

Some of the droplet attributes such as ```region``` and ```image``` can be further inspected by retrieving their relative digitaloceanobject objects.


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
A reboot action is an attempt to reboot the Droplet in a graceful way, similar to using the reboot command from the console.

You can reboot a droplet by calling the following method.

```python
droplet_object.reboot()
```
### Power Cycle

A power cycle action is similar to pushing the reset button on a physical machine, it's similar to booting from scratch.

You can power cycle a droplet by calling the following method.


```python
droplet_object.powercycle()
```
### Shutdown

A shutdown action is an attempt to shutdown the Droplet in a graceful way, similar to using the shutdown command from the console. Since a shutdown command can fail, this action guarantees that the command is issued, not that it succeeds. The preferred way to turn off a Droplet is to attempt a shutdown, with a reasonable timeout, followed by a power off action to ensure the Droplet is off.

You can shutdown a droplet by calling the following method.

```python
droplet_object.shutdown()
```
### Power Off

A power_off event is a hard shutdown and should only be used if the shutdown action is not successful. It is similar to cutting the power on a server and could lead to complications.

You can power off a droplet by calling the following method.

```python
droplet_object.poweroff()
```
### Power On

You can power on a droplet by calling the following method.
```python
droplet_object.poweron()
```
### Rebuild

A rebuild action functions just like a new create.

You can supply an image slug, or an image id. Your droplet will
be rebuilt, and you object attributes will be updated to reflect
the changed this method makes.

You can rebuild a droplet by calling the following method.

```python
droplet_object.rebuild(img:str)
```
### Rename
You can rename a droplet by calling the following method.
```python
droplet_object.rename(name:str)
```
### Create Snapshot

You can create a droplet snapshot using the following method supplying a name to be use for your snapshot.

```python
dropletsnapshot_object = droplet_object.createsnapshot(name:str)
```
A [droplet snapshot  ](https://developers.digitalocean.com/documentation/v2/#snapshot-a-droplet) object is returned.  This type of snapshot, droplet snapshot, has more details than the usual [snapshot](#snapshot-object)  covered later. 

Here are the DropletSnapshot details.


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

You can retrieve all the DropletSnapshots for a droplet by calling the following method.


```python
list_of_dropletsnapshot_objects = droplet_object.retrieve_snapshots()
```

### Retrieve Snapshot By ID

You can retrieve a DropletSnapshot for a droplet by calling the following method and supplying an id.

This method will only search snapshots associated to the droplet.


```python
dropletsnapshot_object = droplet_object.retrieve_snapshot_by_id(id:int)
```


### Retrieve Associated Volumes

A droplet may have block storage attached to it.
You can retrieve a list of [volume objects](#volume-objects) associated to your droplet by calling the following method.

```python
list_of_volume_objects = droplet_object.retrieve_associated_volumes()
```
### Retrieve Associated Volume Snapshots

You can retrieve all associated [volume snapshots](#snapshot-object) by calling the following method.

```python
list_of_volume_snapshot_objects = droplet_object.retrieve_associated_volume_snapshots()
```
!WARNING! These snapshot objects are slightly different to the [droplet snapshots](#create-snapshots) we just looked at.

The [snapshots](https://developers.digitalocean.com/documentation/v2/#snapshots) object created here can actually detail saved instances of both Droplet or a block storage volume, which is reflected in the 'resource_type' attribute.

### Attach A Volume

You can attach a volume to a droplet by calling the following method and supplying a volume object.

```python
droplet_object.attach_a_volume(target_volume:Volume)
```
### Detach A Volume
You can similarly detach the volume by calling the following.
```python
droplet_object.detach_a_volume(target_volume:Volume)
```
### Restore Droplet
A Droplet restoration will rebuild an image using a backup image. The image ID that is passed in must be a backup of the current Droplet instance. The operation will leave any embedded SSH keys intact.

You can restore a droplet by calling the following method.

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

A Droplet must be powered off prior to resizing, digitaloceandroplets does this for you.

### Delete Droplet

You can delete a droplet from your account by applying the following method.

```python
droplet_object.delete()
```

This method sets your objects ``` droplet_object.deleted=True``` so object methods will no longer work.

**[⬆ back to top](#table-of-contents)**

# Block Storage (Volumes)
[DigitalOcean Block Storage Volumes](https://developers.digitalocean.com/documentation/v2/#block-storage) provide expanded storage capacity for your Droplets and can be moved between Droplets within a specific region. Volumes function as raw block devices, meaning they appear to the operating system as locally attached storage which can be formatted using any file system supported by the OS. They may be created in sizes from 1GiB to 16TiB.

Import the digitaloceanobject Volume and VolumeManger to interact with or create new volumes.

```python
from digitaloceanobjects import Volume, VolumeManager
```
## Volume Manager

Create a volume manager.
```python
volume_manager = VolumeManager()
```
### Create New Volume 

To create a new volume use the following method supplying your desired volume [Attribute Values](https://developers.digitalocean.com/documentation/v2/#block-storage).
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
**Note**: You can only create one volume per region with the same name.

### Retrieve All Volumes

To list all available volumes on your account apply the following method.

A list of [volume objects](#volume-object) will be returned.

```python
list_of_volume_objects=volume_manager.retrieve_all_volumes()
```

### Retrieve All Volumes By Name

To list volumes on your account that match a specified name use the following method.

```python
list_of_volume_objects=volume_manager.retrieve_all_volumes_by_name(name:str)
```
### Retrieve Volume By ID

To retrieve a volume by id, apply the following method.
```python
volume_object=volume_manager.retrieve_volume_by_id(id:int)
```
### Retrieve Volume By Name And Region

You can also pick out a specific existing volume by name and region, but calling the following method.

```python
volume_object=volume_manager.retrieve_volume_by_name_region(
											name:str,
											region:str
										)
```
### Retrieve Volumes With ANY Tags

To retrieve a list of volumes that match any, at least one, of your specified tags use the following method and supply a list of tag strings.

```python
list_of_volume_objects=volume_manager.retrieve_volumes_with_any_tags(tag:list)
```
### Retrieve Volumes With ALL Tags

To retrieve a list of volumes that are tagged with all, at least all, of your specified tags use the following command.

```python
list_of_volume_objects=volume_manager.retrieve_volumes_with_all_tags(tag:list)
```
### Retrieve Volumes With ONLY Tags

To retrieve a list of volumes that are tagged with only, exactly matching, your list of specified tags, apply the following method supplying a list of tag strings.

```python
list_of_volume_objects=volume_manager.retrieve_volumes_with_only_tags(tag:list)
```
### Delete Volume By ID

The volume manager allows you to delete a volume by supplying its ID.

Though you may prefer to delete a volume by directly calling delete on its volume object. 
```python
volume_manager.delete_volumes_by_id(id:int)
```


### Delete Volume By Name And Region
The volume manager allows you to delete a volume by supplying its name and region.

Though you may prefer to delete a volume by directly calling delete on its volume object. 
```python
volume_manager.delete_volume_by_name_region(
								name:str,
								region:str
							)
```


### Delete Volumes With ANY Tags
You can delete all volumes that match any of, at least one, of your specified tags by applying the following method and supplying a list of tag strings.
```python
volume_manager.delete_volumes_with_any_tags(tag:list)
```
### Delete Volumes With ALL Tags
You can delete all volumes that contain, at least have all, of your specified tags by applying the following method and supplying a list of tag strings.

```python
volume_manager.delete_volumes_with_all_tags(tag:list)
```
### Delete Volumes With ONLY Tags
You can also delete all volume that only contain, that match exactly, your list of specified tag strings by applying the following method.

```python
volume_manager.delete_volumes_with_only_tags(tag:list)
```

**[⬆ back to top](#table-of-contents)**

## Volume Object

Volume objects contain an attributes data class with the standard digital ocean [volume attributes](https://developers.digitalocean.com/documentation/v2/#block-storage).


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

You can create a [snapshot](#snapshot-object) from your volume using the following method.

A [snapshot](#snapshot-object) will be returned.

```python
snapshot_object=volume_object.create_snapshot(
						name:str,
						tags:list
					)
```
### Retrieve Snapshots

You can retrieve a list of snapshots for your object using the following method.

A list of [snapshot](#snapshot-object) objects will be returned. 
```python
list_of_snapshot_objects=volume_object.retrieve_snapshots()
```
### Detach From Droplets
You can detach a volume from a droplet by calling the following method.
No need to supply details of a droplet as volumes can only be attached to one droplet at a time. This method just makes sure the volume object detaches.
```python
volume_object.detach_from_droplets()
```
### Resize Volume
To resize a volume to a new size in GiB (1024^3), call the following method.

 Volumes may only be resized upwards. 
The maximum size for a volume is 16TiB.

```python
volume_object.resize(size_gigabytes:int)
```

**[⬆ back to top](#table-of-contents)**

# Snapshots

[Snapshots](https://developers.digitalocean.com/documentation/v2/#snapshots) are saved instances of a Droplet or a block storage volume, which is reflected in the ```resource_type``` attribute. In order to avoid problems with compressing filesystems, each defines a ```min_disk_size``` attribute which is the minimum size of the Droplet or volume disk when creating a new resource from the saved snapshot.

Import the digitaloceanobject Snapshot and SnapshotManger to interact with or create new snapshots.

```python
from digitaloceanobjects import Snapshot, SnapshotManager
```
## Snapshot Manager

Create a snapshot manager.

```python
snapshot_manager=SnapshotManager()
```
### Retrieve All Snapshots
To retrieve all existing snapshots call the following method.

A list of [Snapshot objects](#snapshot-object) will be returned.
```python
list_of_snapshot_objects=snapshot_manager.retrieve_all_snapshots()
```
### Retrieve All Droplet Snapshots
To retrieve a list of only droplet snapshots call the following method.
[Snapshot objects](#snapshot-object) will be returned, remember to not confiuse this with DropletSnapshot objects.
```python
list_of_snapshot_objects=snapshot_manager.retrieve_all_droplet_snapshots()
```
### Retrieve All Volume Snapshots
To retrieve a list of only volume snapshots call the following method.
```python
list_of_snapshot_objects=snapshot_manager.retrieve_all_volume_snapshots()
```
### Retrieve Snapshot By ID
You can retrieve a snapshot object by ID.
```python
snapshot_object=snapshot_manager.retrieve_snapshots_id(id:int)
```
**[⬆ back to top](#table-of-contents)**
## Snapshot Object

Snapshot objects contains an attributes data class with the standard digital ocean [snapshot attributes](https://developers.digitalocean.com/documentation/v2/#snapshots).
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
You can delete a snapshot from your account by calling the snapshot object delete method.
```python
snapshot_object.delete()
```
**[⬆ back to top](#table-of-contents)**

# Floating IPs

[DigitalOcean Floating IPs](https://developers.digitalocean.com/documentation/v2/#floating-ips)  are publicly-accessible static IP addresses that can be mapped to one of your Droplets. They can be used to create highly available setups or other configurations requiring movable addresses.

Floating IPs are bound to a specific region.

Import the digitaloceanobject FloatingIP and FloatingIPManger to interact with or create new floating ips.

```python
from digitaloceanobjects import FloatingIP, FloatingIPManager
```
## Floating IP Manager
Create a floating IP manager.
```python
floatingip_manager=FloatingIPManager()
```
### Retrieve All Floating IPs
To retrieve all floating IPs on your account, call the following method.

A list of [floating ip objects](#floating-ip-object) will be returned.
```python
list_of_floatingip_objects=floatingip_manager.retrieve_all_floating_ips()
```
### Create New Floating IP
Creates a floating IP and attaches it straight to the specified droplet object.

A [floating ip object](#floating-ip-object) is returned with details of your new floating ip.
```python
floatingip_object=floatingip_manager.create_new_floating_ip(droplet_object:Droplet)
```
### Create Region Reserve IP

You can reserve a floating ip in a specified region by calling the following method and specifying a region slug.

```python
floatingip_object=floatingip_manager.reserve_ip_for_region(region_slug:str)
```
### Retrieve Floating IP
You can retrieve details of floating ip by using the ip address itself.
Call the following method and specifying the ip address.

```python
floatingip_object=floatingip_manager.retrieve_floating_ip(ip:str)
```
**[⬆ back to top](#table-of-contents)**
## Floating IP Object
Floating IP objects contains an attributes data class with the standard digital ocean [floating IP attributes](https://developers.digitalocean.com/documentation/v2/#floating-ips).

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

You can delete a floating ip from your account by calling the following.
```python
floatingip_object.delete()
```
### Unassign Floating IP]
You can unasign a floating ip from a droplet by calling the following.
Specifying a droplet is not necessary.
```python
floatingip_object.unassign()
```
### Retrieve All IP Actions
You can retrieve all the actions applied to an ip by calling the following method.

A list of [action objects](#action-object) will be returned.
```python
list_of_action_objects=floatingip_object.retrieve_all_actions()
```
### Retrieve Existing IP Action

You can retrieve a specific action by specifying its id and using the following method.
```python
action_object=floatingip_object.retrieve_existing_actions(action_id:int)
```
**[⬆ back to top](#table-of-contents)**

# Actions
[Actions](https://developers.digitalocean.com/documentation/v2/#actions) are records of events that have occurred on the resources in your account. These can be things like rebooting a Droplet, or transferring an image to a new region.

An action object is created every time one of these actions is initiated. The action object contains information about the current status of the action, start and complete timestamps, and the associated resource type and ID.

Every action that creates an action object is available through this endpoint. Completed actions are not removed from this list and are always available for querying.

Import the digitaloceanobject Action and ActionManger to interact with  actions.
```python
from digitaloceanobjects import Action, ActionManager
```
## Action Manager
Create an action manager.
```python
action_manager=ActionManager()
```
### Retrieve All Actions

This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 20 on each page by default but the following method collects them all, and returns all of them in a list of action objects.

*If you want to have direct access to the api call please check the ```actions.py``` . You can paginate using the api call but still benefit from the rate limit management of digitaloceanobjects.*

A list of [Action Objects](#action-object)is returned.

```python
list_of_action_objects=action_manager.retrieve_all_actions()
```
### Retrieve Action
You can retreive one action at a time if you like, by specifying the action id.
```python
action_object=action_manager.retrieve_action(action_id:int)
```
## Action Object
Action objects contains an attributes data class with the standard digital ocean [action attributes](https://developers.digitalocean.com/documentation/v2/#actions).
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

Some exceptions for you to catch, to help your code run smoother.

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