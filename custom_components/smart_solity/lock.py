"""Basic lock definition"""
from __future__ import annotations
from homeassistant.components.lock import LockEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components.smart_solity.smartsolity_lock_lib.lock_control import (
    LockControl,
)

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities
):
    """Setup sensors from a config entry created in the integrations UI."""
    async_add_entities([hass.data[DOMAIN][config_entry.entry_id]])


class Lock(LockEntity):
    """Representation of a lock"""

    def __init__(self, lock_control: LockControl) -> None:
        super().__init__()
        self.lock_control = lock_control
        self._name = lock_control.deviceId
        self._unique_id = lock_control.deviceId

    @property
    def name(self) -> str:
        return self._name

    @property
    def unique_id(self) -> str:
        return self._unique_id

    @property
    def is_locked(self):
        return self.lock_control.is_locked

    async def async_unlock(self):
        await self.lock_control.unlock()

    async def async_lock(self):
        await self.lock_control.lock()

    async def async_update(self):
        await self.lock_control.get_current_state()
