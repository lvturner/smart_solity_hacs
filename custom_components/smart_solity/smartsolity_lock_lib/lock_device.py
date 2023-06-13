class SmartFunction:
    def __init__(self, data):
        self.smartOpenSet = data["smartOpenSet"]
        self.smartOpenDistance = data["smartOpenDistance"]
        self.smartOpenSensitivity = data["smartOpenSensitivity"]
        self.smartOpenTime = data["smartOpenTime"]
        self.smartTouchSet = data["smartTouchSet"]
        self.smartTouchDistance = data["smartTouchDistance"]
        self.smartTouchSensitivity = data["smartTouchSensitivity"]
        self.smartTouchTime = data["smartTouchTime"]


class MyDeviceFunctions:
    def __init__(self, data):
        self.cmdSetLock = data["cmdSetLock"]
        self.cmdSetOutLock = data["cmdSetOutLock"]
        self.cmdSetSelfLock = data["cmdSetSelfLock"]
        self.cmdSetSound = data["cmdSetSound"]
        self.cmdSetCard = data["cmdSetCard"]
        self.cmdSetFingerPrint = data["cmdSetFingerPrint"]
        self.cmdSetFacePrint = data["cmdSetFacePrint"]
        self.cmdSetRemoteControl = data["cmdSetRemoteControl"]
        self.cmdDoorReset = data["cmdDoorReset"]
        self.cmdDoorStatus = data["cmdDoorStatus"]
        self.cmdDoorOpen = data["cmdDoorOpen"]
        self.cmdDoorClose = data["cmdDoorClose"]
        self.cmdSetClock = data["cmdSetClock"]
        self.cmdSetPassword = data["cmdSetPassword"]
        self.cmdSetSecurity = data["cmdSetSecurity"]
        self.cmdSetDoubleClose = data["cmdSetDoubleClose"]
        self.cmdSetBuzzer = data["cmdSetBuzzer"]
        self.cmdSetOnePass = data["cmdSetOnePass"]
        self.cmdSetVisitorPass = data["cmdSetVisitorPass"]
        self.cmdSetKeepOpen = data["cmdSetKeepOpen"]
        self.cmdSetFakeNumber = data["cmdSetFakeNumber"]
        self.cmdSetFireSense = data["cmdSetFireSense"]
        self.cmdSetEarthquakeSense = data["cmdSetEarthquakeSense"]
        self.notiSetDoorStatus = data["notiSetDoorStatus"]
        self.notiSetDoorEvent = data["notiSetDoorEvent"]


class LockDevice:
    def __init__(self, data):
        self.my_device_id = data["myDeviceId"]
        self.my_device_member_id = data["myDeviceMemberId"]
        self.my_device_reg_device_id = data["myDeviceRegDeviceId"]
        self.reg_device_serial_no = data["regDeviceSerialNo"]
        self.reg_device_app_key = data["regDeviceAppKey"]
        self.reg_device_broker_id = data["regDeviceBrokerId"]
        self.my_device_admin_yn = data["myDeviceAdminYn"]
        self.my_device_auth_type = int(data["myDeviceAuthType"])
        self.my_device_auth_type_name = data["myDeviceAuthTypeName"]
        self.my_device_nick_name = data["myDeviceNickName"]
        self.my_device_maker_name = data["myDeviceMakerName"]
        self.my_device_model_name = data["myDeviceModelName"]
        self.my_device_ble_mac_addr = data["myDeviceBleMacAddr"]
        self.my_device_latitude = float(data["myDeviceLatitude"])
        self.my_device_longitude = float(data["myDeviceLongitude"])
        self.my_device_altitude = float(data["myDeviceAltitude"])
        self.my_device_wifi_yn = data["myDeviceWifiYn"]
        self.my_device_gateway_yn = data["myDeviceGatewayYn"]
        self.my_device_ble_yn = data["myDeviceBleYn"]
        self.my_device_zigbee_yn = data["myDeviceZigbeeYn"]
        self.my_device_start_date = data["myDeviceStartDate"]
        self.my_device_end_date = data["myDeviceEndDate"]
        self.my_device_start_time = data["myDeviceStartTime"]
        self.my_device_end_time = data["myDeviceEndTime"]
        self.my_device_sunday_yn = data["myDeviceSundayYn"]
        self.my_device_monday_yn = data["myDeviceMondayYn"]
        self.my_device_tuesday_yn = data["myDeviceTuesdayYn"]
        self.my_device_wednesday_yn = data["myDeviceWednesdayYn"]
        self.my_device_thursday_yn = data["myDeviceThursdayYn"]
        self.my_device_friday_yn = data["myDeviceFridayYn"]
        self.my_device_saturday_yn = data["myDeviceSaturdayYn"]
        self.my_device_visit_password = data["myDeviceVisitPassword"]
        self.noti_door_status_set_status = int(data["notiDoorStatusSetStatus"])
        self.noti_door_event_set_status = int(data["notiDoorEventSetStatus"])
        self.security_set_status = int(data["securitySetStatus"])
        self.double_close_set_status = int(data["doubleCloseSetStatus"])
        self.keep_open_set_status = int(data["keepOpenSetStatus"])
        self.sound_set_status = int(data["soundSetStatus"])
        self.buzzer_use_status = int(data["buzzerUseStatus"])
        self.fake_number_set_status = int(data["fakeNumberSetStatus"])
        self.sublatch_set_status = int(data["sublatchSetStatus"])
        self.firmware_update_need_yn = data["firmwareUpdateNeedYn"]
        self.my_device_firmware_version = data["myDeviceFirmwareVersion"]
        self.latest_firmware_version = data["latestFirmwareVersion"]
        self.locker_status = int(data["lockerStatus"])
        self.battery = int(data["battery"])
        self.gateway_conn_status = data["gatewayConnStatus"]
        smart_func_data = data["smartFunction"] if "smartFunction" in data else {}
        self.smartFunction = SmartFunction(smart_func_data)
        my_device_funcs_data = (
            data["myDeviceFunctions"] if "myDeviceFunctions" in data else {}
        )
        self.myDeviceFunctions = MyDeviceFunctions(my_device_funcs_data)
        self.threatList = data["threatList"]
