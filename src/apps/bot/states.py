from enum import Enum, auto


class States(Enum):
    START = auto()
    GET_LANG = auto()
    GET_PHONE = auto()
    GET_LOCATION = auto()
    GET_NAME = auto()

    GET_MENU = auto()
    CHANGE_LANG = auto()
    CORPORATE_CLIENTS = auto()
    FAQ = auto()
    SERVICE = auto()
    GET_SERVICE_TYPE = auto()
    FULL_NAME = auto()
    GET_VIDEO = auto()

    MESSAGE = auto()
    GET_PHONE_NUMBER = auto()