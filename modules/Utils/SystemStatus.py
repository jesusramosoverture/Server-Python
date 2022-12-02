#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
"""TODO: Singlenton version Thread safe"""
# ---------------------------------------------------------------------------
import logging
from dataclasses import dataclass, field
from threading import Lock

# ----------------------SET UP LOGGING MODULE -------------------------------
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]


@dataclass
class SystemStatus(metaclass=SingletonMeta):
    """
    Singleton used to store all the variables and make them accessible to all the functions
    that could need it.

    A correct way of getting and setting has been carried out.
    """
    flag_current_volume: bool = False
    _flag_check_init: bool = False
    _verdict_on_the_client: bool = False
    _device_name: str = ""
    _Ip_device: str = ""
    _list_of_speakers: list = field(default_factory=lambda: [])
    _current_speaker: str = ""
    _list_of_microphones: list = field(default_factory=lambda: [])
    _current_of_microphone: str = None

    def __post_init__(self):
        super(SystemStatus, self).__init__()

    @property
    def current_volume_flag(self):
        return self.flag_current_volume

    @current_volume_flag.setter
    def current_volume_flag(self, new_value):
        self.flag_current_volume = new_value

    @property
    def new_client_connected(self):
        return self._flag_check_init

    @new_client_connected.setter
    def new_client_connected(self, new_value):
        self._flag_check_init = new_value

    @property
    def the_client_is_(self):
        return self._verdict_on_the_client

    @the_client_is_.setter
    def the_client_is_(self, new_value):
        self._verdict_on_the_client = new_value

    @property
    def name_device_connected(self):
        return self._device_name

    @name_device_connected.setter
    def name_device_connected(self, new_value):
        self._device_name = new_value

    @property
    def ip_device_connected(self):
        return self._Ip_device

    @ip_device_connected.setter
    def ip_device_connected(self, new_value):
        self._Ip_device = new_value

    def add_speaker(self, speaker: object):
        self._list_of_speakers.append(speaker)

    def add_microphone(self, microphone: object):
        self._list_of_microphones.append(microphone)

    @property
    def active_microphone(self):
        return self._current_of_microphone

    @active_microphone.setter
    def active_microphone(self, new_value):
        self._current_of_microphone = new_value

    @property
    def active_speaker(self):
        return self._current_speaker

    @active_speaker.setter
    def active_speaker(self, new_value):
        self._current_speaker = new_value

    @property
    def get_all_speakers(self):
        return self._list_of_speakers

    @property
    def get_all_microphones(self):
        return self._list_of_microphones
