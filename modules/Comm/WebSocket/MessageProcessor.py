#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" MSG PROCESSOR """
import json
import logging
import traceback
# ---------------------------------------------------------------------------
from dataclasses import dataclass
from modules.Comm.Messages.MessageTypeId import TypeOfMsg
from modules.Comm.Messages.payloads.Init_payload import InitPayload
from modules.Comm.Messages.payloads.Volume_payload import VolumePayload
from modules.Comm.Messages.payloads.Volumen_Mute_payload import VolumeMutePayload
from modules.ConstantsValues import MsgParameter
from modules.Audio.ControlAudio import AudioControl


@dataclass
class MsgProcessor:
    """

    """
    msg: str = "Empty"
    id: int = 0
    order: int = 0

    def __post_init__(self):
        """

        :return:
        """
        self.audio = AudioControl()

    @staticmethod
    def is_json(myjson):
        """

        :param myjson:
        :return:
        """
        response = False
        try:
            json.loads(myjson)
            response = True
        except ValueError:
            print(traceback.format_exc())
        finally:
            return response

    @staticmethod
    def is_well_formed_message(message: str) -> bool:
        """

        :type message: str
        :param message:
        :return: bool
        """
        try:
            data_json = json.loads(message)
            return MsgParameter.ID.value in data_json and MsgParameter.ORDER.value in data_json
        except OSError:
            logging.error(f'Payload wrong formed: {traceback.format_exc()}')
            return False

    def obtain_data_from_json(self) -> bool:
        """

        :return:
        """
        try:
            data = json.loads(self.msg)
            self.id = data[MsgParameter.ID.value]
            self.order = data[MsgParameter.ORDER.value]
            return True
        except OSError:
            logging.info(f'Error in obtain_data_from_json: \n {traceback.format_exc()}')
            return False

    def process_the_message(self, msg_recv: json) -> bool:
        """

        :return:
        """
        self.msg = msg_recv
        response = False
        "Guard Clauses"
        if not self.is_json(self.msg):
            return False
        if not self.is_well_formed_message(self.msg):
            return False
        if not self.obtain_data_from_json():
            return False

        "Goto the switch case (Goto...very professional XDD)"
        match self.id:
            case TypeOfMsg.INIT.value:
                if InitPayload.is_payload_correct(self.msg):
                    InitPayload(self.id, self.order).execute_action(self.order)
                    response = True
            case TypeOfMsg.VOLUME.value:
                if VolumePayload.is_payload_correct(self.msg):
                    VolumePayload(self.id, self.order).execute_action(self.order)
                    response = True
            case TypeOfMsg.MUTE.value:
                if VolumeMutePayload.is_payload_correct(self.msg):
                    VolumeMutePayload(self.id, self.order).execute_action(self.order)
                    response = True
            case TypeOfMsg.BRIGHTNESS_UP.value:
                print('BRIGHTNESS_UP')
            case TypeOfMsg.BRIGHTNESS_DOWN.value:
                print('BRIGHTNESS_UP')

        return response
