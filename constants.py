___all__ = ['UUIDS']


class Immutable(type):

    def __call__(*args):
        raise Exception("You can't create instance of immutable object")

    def __setattr__(*args):
        raise Exception("You can't modify immutable object")


class UUIDS(object):

    __metaclass__ = Immutable

    BASE = '0000%s-0000-1000-8000-00805f9b34fb'
    CHARACTERISTIC_BASE = '0000%s-0000-3512-2118-0009af100700'

    # Services
    SERVICE_ALERT = BASE % '1802'
    SERVICE_HEART_RATE = BASE % '180d'
    SERVICE_ALERT_NOTIFICATION = BASE % '1811'
    SERVICE_DEVICE_INFO = BASE % '180a'
    SERVICE_MIBAND1 = BASE % 'fee0'
    SERVICE_MIBAND2 = BASE % 'fee1'

    CHARACTERISTIC_SENSOR = CHARACTERISTIC_BASE % '0001'
    CHARACTERISTIC_HZ = CHARACTERISTIC_BASE % '0002'
    CHARACTERISTIC_CONFIGURATION = CHARACTERISTIC_BASE % '0003'
    CHARACTERISTIC_BATTERY = CHARACTERISTIC_BASE % '0006'
    CHARACTERISTIC_STEPS = CHARACTERISTIC_BASE % '0007'
    CHARACTERISTIC_USER_SETTINGS = CHARACTERISTIC_BASE % '0008'
    CHARACTERISTIC_AUTH = CHARACTERISTIC_BASE % '0009'
    CHARACTERISTIC_DEVICEEVENT = CHARACTERISTIC_BASE % '0010'

    CHARACTERISTIC_REVISION = 0x2a28
    CHARACTERISTIC_SERIAL = 0x2a25
    CHARACTERISTIC_HRDW_REVISION = 0x2a27

    CHARACTERISTIC_ALERT = BASE % '2a06'
    CHARACTERISTIC_CURRENT_TIME = BASE % '2a2b'
    CHARACTERISTIC_HEART_RATE_MEASURE = BASE % '2a37'
    CHARACTERISTIC_HEART_RATE_CONTROL = BASE % '2a39'
    CHARACTERISTIC_CUSTOM_ALERT = BASE % '2a46'
    CHARACTERISTIC_AGE = BASE % '2a80'
    CHARACTERISTIC_LE_PARAMS = BASE % 'ff09'

    NOTIFICATION_DESCRIPTOR = 0x2902

    # Device Firmware Update
    SERVICE_DFU_FIRMWARE = CHARACTERISTIC_BASE % '1530'
    CHARACTERISTIC_DFU_FIRMWARE = CHARACTERISTIC_BASE % '1531'
    CHARACTERISTIC_DFU_FIRMWARE_WRITE = CHARACTERISTIC_BASE % '1532'


class AUTH_STATES(object):

    __metaclass__ = Immutable

    AUTH_OK = 'Auth ok'
    AUTH_FAILED = 'Auth failed'
    ENCRIPTION_KEY_FAILED = 'Encryption key auth fail, sending new key'
    KEY_SENDING_FAILED = 'Key sending failed'
    REQUEST_RN_ERROR = 'Something went wrong when requesting the random number'


class ALERT_TYPES(object):

    __metaclass__ = Immutable

    NONE = b'\x00'
    MESSAGE = b'\x01'
    PHONE = b'\x02'


class QUEUE_TYPES(object):

    __metaclass__ = Immutable

    HEART = 'heart'
    RAW_ACCEL = 'raw_accel'
    RAW_HEART = 'raw_heart'
