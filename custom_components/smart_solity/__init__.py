"""The Smart Solity Lock integration."""
from __future__ import annotations
import logging
import aiohttp

from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.components.smart_solity.smartsolity_lock_lib.lock_control import (
    LockControl,
)
from homeassistant.components.smart_solity.smartsolity_lock_lib.auth import (
    Auth,
)
from .lock import Lock

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.LOCK]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Smart Solity Lock from a config entry."""
    _LOGGER.info("Setting up smart solity")

    hass.data.setdefault(DOMAIN, {})
    # TODO 1. Create API instance
    # TODO 2. Validate the API connection (and authentication)
    # TODO 3. Store an API object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)
    username = entry.data["username"]
    password = entry.data["password"]
    host = entry.data["host"]
    device_id = entry.data["device_id"]

    auth = Auth(
        async_get_clientsession(hass),
        host,
        username,
        password,
    )
    lock_control = LockControl(auth, device_id)
    hass.data[DOMAIN][entry.entry_id] = Lock(lock_control)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
