# import asyncio
# import homeassistant.components.smart_solity.smartsolity_lock_lib.lock_control as lock_control
# from os import environ
# import homeassistant.components.smart_solity.smartsolity_lock_lib.auth as auth
# from aiohttp import ClientSession


# async def setup():
#     client_session = ClientSession()
#     auth = auth.Auth(client_session, "https://www.smartsolity.com")

#     lock_control = lock_control.LockControl(auth, "XXXX")
#     await lock_control.get_current_state()

#     print(f"Device is locked: {lock_control.is_locked}")

#     # await lock_control.unlock()
#     # print("Door unlocked")

#     await lock_control.lock()
#     print("Door locked")


# if __name__ == "__main__":
#     asyncio.run(setup())
