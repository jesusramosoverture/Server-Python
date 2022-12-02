#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" VOLUMEN PAYLOAD"""
# ---------------------------------------------------------------------------
import json
from abc import ABC
from dataclasses import dataclass

from modules.Audio.ControlAudio import AudioControl
# ---------------------------------------------------------------------------
from modules.Comm.Messages.Msg_MetaClass import MessagesPayloadInterface
from modules.ConstantsValues import MsgParameter


@dataclass
class VolumePayload(MessagesPayloadInterface, ABC):
    type_of_Id: int = 0
    type_of_data: int = 0

    def __post_init__(self):
        """

        :return:
        """
        self.audio = AudioControl()

    @staticmethod
    def serialize_payload():
        """

        :return:
        """
        pass

    @staticmethod
    def is_payload_correct(message: str) -> bool:
        """

        :type message: str
        :param message:
        :return: bool
        """

        data_json = json.loads(message)
        return any([isinstance(data_json[MsgParameter.ID.value], int)
                    and isinstance(data_json[MsgParameter.ORDER.value], int)
                    and (0 <= data_json[MsgParameter.ORDER.value] <= 100)])

    def execute_action(self, command: int | str | dict) -> None:
        """

        :param command:
        :return: bool
        """
        self.audio.set_new_volume(int(command))
