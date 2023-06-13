import json
from homeassistant.components.smart_solity.smartsolity_lock_lib.lock_device import (
    LockDevice,
)
from homeassistant.components.smart_solity.smartsolity_lock_lib.auth import Auth


class LockControl:
    def __init__(self, auth: Auth, deviceId: str):
        self.auth = auth
        self.deviceId = deviceId
        self._device = None

    @property
    def is_gateway_connected(self):
        return self._device.gateway_conn_status == "Y"

    @property
    def is_locked(self):
        if not self._device is None:  # ew
            return self._device.locker_status == 0

    @is_locked.setter
    def is_locked(self, value):
        if not self._device is None:  # ew
            self._device.locker_status = value

    @property
    def device(self):
        return self._device

    async def get_current_state(self):
        response = await self.auth.request("GET", "api/mydevice")
        devices = json.loads(await response.text())
        for device in devices["contents"]["myDeviceList"]:
            if device["myDeviceId"] == self.deviceId:
                self._device = LockDevice(device)
                break

    async def connect_gateway(self):
        data = {
            "lang": "1",
            "optionValue": "60",
            "appSource": "0",
            "controlType": "connect_gateway",
        }
        url = f"api/controldevice/{self.deviceId}"
        response = await self.auth.request("PUT", url, json=data)
        results = json.loads(await response.text())
        if results["result"] == 0:
            self._device.gateway_conn_status = "Y"
        else:
            raise Exception("Failed to connect gateway")

    async def _control_device(self, control_type):
        if self._device is None:
            await self.get_current_state()
        if not self.is_gateway_connected:
            await self.connect_gateway()

        data = {"controlType": control_type, "lang": "1", "appSource": "0"}
        url = f"api/controldevice/{self.deviceId}"
        response = await self.auth.request("PUT", url, json=data)
        data = json.loads(await response.text())
        if data["result"] != 0:
            raise Exception("Failed to control device")

    async def lock(self):
        await self._control_device("close")
        self.is_locked = "Y"

    async def unlock(self):
        await self._control_device("open")
        self.is_locked = "N"
