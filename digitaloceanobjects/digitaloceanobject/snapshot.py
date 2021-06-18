from __future__ import annotations

from dataclasses import dataclass, field
from ..common.cloudapiexceptions import *
from ..digitaloceanapi.snapshots import Snapshots
import json
import threading
import time
import datetime


class SnapshotManager:
    def __init__(self):
        self.snapshotapi = Snapshots()

    def retrieve_all_snapshots(self):
        snapshot_list = []
        page, per_page = 1, 10
        response = self.snapshotapi.list_all_snapshots(page=page, per_page=per_page)
        content = json.loads(response.content.decode("utf-8"))
        snapshot_list.extend(content["snapshots"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.snapshotapi.list_all_snapshots(
                    page=page, per_page=per_page
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

    def retrieve_all_droplet_snapshots(self):
        snapshot_list = []
        page, per_page = 1, 10
        response = self.snapshotapi.list_all_droplet_snapshots(
            page=page, per_page=per_page
        )
        content = json.loads(response.content.decode("utf-8"))
        snapshot_list.extend(content["snapshots"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.snapshotapi.list_all_droplet_snapshots(
                    page=page, per_page=per_page
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

    def retrieve_all_volume_snapshots(self):
        snapshot_list = []
        page, per_page = 1, 10
        response = self.snapshotapi.list_all_volume_snapshots(
            page=page, per_page=per_page
        )
        content = json.loads(response.content.decode("utf-8"))
        snapshot_list.extend(content["snapshots"])
        try:
            while content["links"]["pages"]["next"]:
                page = page + 1
                response = self.snapshotapi.list_all_volume_snapshots(
                    page=page, per_page=per_page
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

    def retrieve_snapshot_id(self, id):
        if not self.does_snapshot_id_exist(id):
            raise ErrorSnapshotNotFound(f"Snapshot with id:{id} not found")
        newsnapshot = Snapshot()
        response = self.snapshotapi.retrieve_snapshot_by_id(id)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            snapshot_data = dict(content["snapshots"])
            newsnapshot.attributes = SnapshotAttributes(**snapshot_data)
        return newsnapshot

    def delete_snapshot(self, snapshot: Snapshot):
        id = snapshot.attributes.id
        self.delete_snapshot_id(id)

    def delete_snapshot_id(self, id):
        if self.does_snapshot_id_exist(id):
            self.snapshotapi.delete_snapshot_id(id)

    def does_snapshot_id_exist(self, id):
        snapshots = self.retrieve_all_snapshots()
        for snapshot in snapshots:
            if str(snapshot.attributes.id) == str(id):
                return True
        return False


@dataclass
class SnapshotArguments:
    name: str = None
    tags: list = field(default_factory=list)


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


class Snapshot:
    def __init__(self):
        self.arguments = SnapshotArguments()
        self.attributes = SnapshotAttributes()
