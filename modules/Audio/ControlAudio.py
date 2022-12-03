#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" Audio control"""
import logging
# ---------------------------------------------------------------------------
from dataclasses import dataclass, field
from threading import Lock
# ---------------------------------------------------------------------------
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from modules.Utils.SystemStatus import SystemStatus
import soundcard as sc
from modules.Utils.SinglentonType import SingletonMeta

# ----------------------SET UP LOGGING MODULE -------------------------------
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


# class SingletonMeta(type):
#     """
#
#     """
#     _instances = {}
#     _lock: Lock = Lock()
#
#     def __call__(cls, *args, **kwargs):
#         with cls._lock:
#             if cls not in cls._instances:
#                 instance = super().__call__(*args, **kwargs)
#                 cls._instances[cls] = instance
#             return cls._instances[cls]


@dataclass
class AudioControl(metaclass=SingletonMeta):
    """

    """
    scalar_volume: int = 1
    mics: list = field(default_factory=lambda: [])

    def __post_init__(self):
        """

        :return:
        """
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(self.interface, POINTER(IAudioEndpointVolume))
        self.system_status = SystemStatus()
        self.gathering_info_audio_devices()

    def gathering_info_audio_devices(self):
        """

        :return:
        """
        self.get_list_of_speakers()
        self.get_list_of_microphones()
        self.current_speaker()
        self.current_microphones()

    def get_list_of_speakers(self):
        """

        :return:
        """
        speakers = sc.all_speakers()
        for speaker in speakers:
            speaker = str(speaker)
            log.info(f"speaker: {speaker} -- type{type(speaker)}")
            self.system_status.add_speaker(speaker)

    def get_list_of_microphones(self):
        """

        :return:
        """
        self.mics = sc.all_microphones()
        log.info(f"len of mics: {len(self.mics)}")
        for mic in self.mics:
            mic = str(mic)
            self.system_status.add_microphone(mic)

    def current_speaker(self):
        """

        :return:
        """
        self.system_status.active_speaker = str(sc.default_speaker())

    def current_microphones(self):
        """

        :return:
        """
        if self.mics:
            self.system_status.active_microphone = str(sc.default_microphone())

    def current_volume_value(self):
        """

        :return:
        """
        return int(round(self.volume.GetMasterVolumeLevelScalar() * 100))

    @staticmethod
    def clamp(n, min_n, max_n):
        """

        :param n:
        :param min_n:
        :param max_n:
        :return:
        """
        return max(min(max_n, n), min_n)

    def set_new_volume(self, new_value: int) -> None:
        """

        :return:
        """
        value_checked = self.clamp(new_value, 0, 100)
        self.scalar_volume = value_checked / 100 if value_checked != 0 else 0
        self.volume.SetMasterVolumeLevelScalar(self.scalar_volume, None)

    def mute_audio(self, value: str) -> None:
        if value == "unmuted":
            self.volume.SetMute(0, None)
        elif value == "muted":
            self.volume.SetMute(1, None)
