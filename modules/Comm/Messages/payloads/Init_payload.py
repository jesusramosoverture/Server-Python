#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 26/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" VOLUMEN PAYLOAD"""
# ---------------------------------------------------------------------------
import json
import logging
from abc import ABC
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
from modules.Comm.Messages.Msg_MetaClass import MessagesPayloadInterface
from modules.ConstantsValues import MsgParameter
from modules.Utils.SystemStatus import SystemStatus


@dataclass
class InitPayload(MessagesPayloadInterface, ABC):
    type_of_data: dict = field(default_factory=lambda: {
        "device": "NA",
        "IP": "NA"
    })
    type_of_Id: int = 0

    def __post_init__(self):
        """

        :return:
        """
        self.system_status = SystemStatus()

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
                    and isinstance(data_json[MsgParameter.ORDER.value], dict)
                    and isinstance(data_json[MsgParameter.ORDER.value]["device"], str)
                    and isinstance(data_json[MsgParameter.ORDER.value]["IP"], str)])

    def execute_action(self, command: int | str | dict) -> None:
        """

        :param command:
        :return: bool
        """
        print(f"Command: {command}")
        self.system_status.the_client_is_ = True
        self.system_status.name_device_connected = command["device"]
        self.system_status.ip_device_connected = command["IP"]
