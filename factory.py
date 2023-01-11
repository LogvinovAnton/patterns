from .workers import Worker1, Worker2
from enum import Enum


class ActionTypes(Enum):
    Worker1_Worker2_UPDATE_ALL = 'Worker1_Worker2_UPDATE_ALL'
    Worker1_Worker2_DIFF_ALL = 'Worker1_Worker2_DIFF_ALL'
    Worker1_Worker2_DIFF_DEVICES = 'Worker1_Worker2_DIFF_DEVICES'
    Worker1_Worker2_UPDATE_DEVICES = 'Worker1_Worker2_UPDATE_DEVICES'
    Worker1_DATA_COLLECTION = 'Worker1_DATA_COLLECTION'


class ActionsFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)


class Worker1Functions:
    def __init__(self, worker):
        self.worker = worker

    def functions_normalize_devices(self):
        return [
            self.worker.site.fill_source_data,
            self.worker.site.normalize_source_data,

            self.worker.config_context.fill_source_data,
            self.worker.config_context.normalize_source_data,

            self.worker.vrfs.fill_source_data,
            self.worker.vrfs.normalize_source_data,

            self.worker.vlan_groups.fill_source_data,
            self.worker.vlan_groups.normalize_source_data,

            self.worker.vlans.fill_source_data,
            self.worker.vlans.normalize_source_data,

            self.worker.prefixes.fill_source_data,
            self.worker.prefixes.normalize_source_data,

            self.worker.locations.fill_source_data,
            self.worker.locations.normalize_source_data,

            self.worker.racks.fill_source_data,
            self.worker.racks.normalize_source_data,

            self.worker.devices.fill_source_data,
            self.worker.devices.normalize_source_data,
        ]

    def functions_normalize_all(self):
        return self.functions_normalize_devices() + [
            self.worker.interfaces.fill_source_data,
            self.worker.interfaces.normalize_source_data,

            self.worker.ipaddresses.fill_source_data,
            self.worker.ipaddresses.normalize_source_data,

            # self.worker.devices.fill_local_context,
        ]


class Worker2Functions:
    def __init__(self, worker):
        self.worker = worker

    def function_update_devices(self):
        return [
            self.worker.site.fill_source_data,
            self.worker.site.normalize_source_data,
            self.worker.site.prepare_modified_data,
            self.worker.site.create_objects,
            self.worker.site.update_objects,

            self.worker.config_context.fill_source_data,
            self.worker.config_context.normalize_source_data,
            self.worker.config_context.prepare_modified_data,
            self.worker.config_context.create_objects,
            self.worker.config_context.update_objects,

            self.worker.vrfs.fill_source_data,
            self.worker.vrfs.normalize_source_data,
            self.worker.vrfs.prepare_modified_data,
            self.worker.vrfs.create_objects,
            self.worker.vrfs.update_objects,

            self.worker.vlan_groups.fill_source_data,
            self.worker.vlan_groups.normalize_source_data,
            self.worker.vlan_groups.prepare_modified_data,
            self.worker.vlan_groups.create_objects,
            self.worker.vlan_groups.update_objects,

            self.worker.vlans.fill_source_data,
            self.worker.vlans.normalize_source_data,
            self.worker.vlans.prepare_modified_data,
            self.worker.vlans.create_objects,
            self.worker.vlans.update_objects,

            self.worker.prefixes.fill_source_data,
            self.worker.prefixes.normalize_source_data,
            self.worker.prefixes.prepare_modified_data,
            self.worker.prefixes.create_objects,
            self.worker.prefixes.update_objects,

            self.worker.locations.fill_source_data,
            self.worker.locations.normalize_source_data,
            self.worker.locations.prepare_modified_data,
            self.worker.locations.create_objects,
            self.worker.locations.update_objects,

            self.worker.racks.fill_source_data,
            self.worker.racks.normalize_source_data,
            self.worker.racks.prepare_modified_data,
            self.worker.racks.create_objects,
            self.worker.racks.update_objects,

            self.worker.devices.fill_source_data,
            self.worker.devices.normalize_source_data,
            self.worker.devices.prepare_modified_data,
            self.worker.devices.create_objects,
            self.worker.devices.update_objects,
        ]

    def functions_update_all(self):
        return self.function_update_devices() + [
            self.worker.interfaces.fill_source_data,
            self.worker.interfaces.normalize_source_data,
            self.worker.interfaces.prepare_modified_data,
            self.worker.interfaces.create_objects,
            self.worker.interfaces.update_objects,

            self.worker.ipaddresses.fill_source_data,
            self.worker.ipaddresses.normalize_source_data,
            self.worker.ipaddresses.prepare_modified_data,
            self.worker.ipaddresses.create_objects,
            self.worker.ipaddresses.update_objects,

            self.worker.devices.update_primary_ip4,
            self.worker.devices.update_local_context,
        ]

    def functions_get_modified_data_devices(self):
        return [
            self.worker.site.fill_source_data,
            self.worker.site.normalize_source_data,
            self.worker.site.prepare_modified_data,

            self.worker.config_context.fill_source_data,
            self.worker.config_context.normalize_source_data,
            self.worker.config_context.prepare_modified_data,

            self.worker.vrfs.fill_source_data,
            self.worker.vrfs.normalize_source_data,
            self.worker.vrfs.prepare_modified_data,

            self.worker.vlan_groups.fill_source_data,
            self.worker.vlan_groups.normalize_source_data,
            self.worker.vlan_groups.prepare_modified_data,

            self.worker.vlans.fill_source_data,
            self.worker.vlans.normalize_source_data,
            self.worker.vlans.prepare_modified_data,

            self.worker.prefixes.fill_source_data,
            self.worker.prefixes.normalize_source_data,
            self.worker.prefixes.prepare_modified_data,

            self.worker.locations.fill_source_data,
            self.worker.locations.normalize_source_data,
            self.worker.locations.prepare_modified_data,

            self.worker.racks.fill_source_data,
            self.worker.racks.normalize_source_data,
            self.worker.racks.prepare_modified_data,

            self.worker.devices.fill_source_data,
            self.worker.devices.normalize_source_data,
            self.worker.devices.prepare_modified_data,
        ]

    def functions_get_modified_data_all(self):
        return self.functions_get_modified_data_devices() + [
            self.worker.interfaces.fill_source_data,
            self.worker.interfaces.normalize_source_data,
            self.worker.interfaces.prepare_modified_data,

            self.worker.ipaddresses.fill_source_data,
            self.worker.ipaddresses.normalize_source_data,
            self.worker.ipaddresses.prepare_modified_data,
        ]


class Worker1Worker2DiffAllBuilder:
    def __init__(self):
        self._functions = None

    def __call__(self, site_name, Worker1_path, Worker2_url, Worker2_token, Worker2_ssl_verification, **_ignored):
        if not self._functions:
            Worker1_worker = Worker1(site_name, Worker1_path)
            Worker1_functions = Worker1Functions(Worker1_worker)
            Worker2_worker = Worker2(site_name, Worker2_url, Worker2_token, Worker2_ssl_verification, Worker1_worker)
            Worker2_functions = Worker2Functions(Worker2_worker)
            self._functions = (Worker1_functions.functions_normalize_all() +
                               Worker2_functions.functions_get_modified_data_all())
        return self._functions


class Worker1Worker2UpdateAllBuilder:
    def __init__(self):
        self._functions = None

    def __call__(self, site_name, Worker1_path, Worker2_url, Worker2_token, Worker2_ssl_verification, **_ignored):
        if not self._functions:
            Worker1_worker = Worker1(site_name, Worker1_path)
            Worker1_functions = Worker1Functions(Worker1_worker)
            Worker2_worker = Worker2(site_name, Worker2_url, Worker2_token, Worker2_ssl_verification, Worker1_worker)
            Worker2_functions = Worker2Functions(Worker2_worker)
            self._functions = Worker1_functions.functions_normalize_all() + Worker2_functions.functions_update_all()
        return self._functions


class Worker1Worker2DiffDevicesBuilder:
    def __init__(self):
        self._functions = None

    def __call__(self, site_name, Worker1_path, Worker2_url, Worker2_token, Worker2_ssl_verification, **_ignored):
        if not self._functions:
            Worker1_worker = Worker1(site_name, Worker1_path)
            Worker1_functions = Worker1Functions(Worker1_worker)
            Worker2_worker = Worker2(site_name, Worker2_url, Worker2_token, Worker2_ssl_verification, Worker1_worker)
            Worker2_functions = Worker2Functions(Worker2_worker)
            self._functions = (Worker1_functions.functions_normalize_devices() +
                               Worker2_functions.functions_get_modified_data_devices())
        return self._functions


class Worker1Worker2UpdateDevicesBuilder:
    def __init__(self):
        self._functions = None

    def __call__(self, site_name, Worker1_path, Worker2_url, Worker2_token, Worker2_ssl_verification, **_ignored):
        if not self._functions:
            Worker1_worker = Worker1(site_name, Worker1_path)
            Worker1_functions = Worker1Functions(Worker1_worker)
            Worker2_worker = Worker2(site_name, Worker2_url, Worker2_token, Worker2_ssl_verification, Worker1_worker)
            Worker2_functions = Worker2Functions(Worker2_worker)
            self._functions = (Worker1_functions.functions_normalize_devices() +
                               Worker2_functions.function_update_devices())
        return self._functions


class Worker1DataCollectionBuilder:
    def __init__(self):
        self._functions = None

    def __call__(self, site_name, Worker1_path, **_ignored):
        if not self._functions:
            Worker1_worker = Worker1(site_name, Worker1_path)
            Worker1_functions = Worker1Functions(Worker1_worker)
            self._functions = Worker1_functions.functions_normalize_all()
        return self._functions


actions = ActionsFactory()
actions.register_builder(ActionTypes.Worker1_Worker2_DIFF_ALL.value, Worker1Worker2DiffAllBuilder())
actions.register_builder(ActionTypes.Worker1_Worker2_UPDATE_ALL.value, Worker1Worker2UpdateAllBuilder())
actions.register_builder(ActionTypes.Worker1_Worker2_DIFF_DEVICES.value, Worker1Worker2DiffDevicesBuilder())
actions.register_builder(ActionTypes.Worker1_Worker2_UPDATE_DEVICES.value, Worker1Worker2UpdateDevicesBuilder())
actions.register_builder(ActionTypes.Worker1_DATA_COLLECTION.value, Worker1DataCollectionBuilder())
