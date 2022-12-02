#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
"""MSG TYPE ID"""
# ---------------------------------------------------------------------------
from enum import Enum


class MsgParameter(Enum):
    ID = "Id"
    ORDER = "Order"


class Payload_order(Enum):
    VOLUME_MUTE = "muted"
    VOLUME_UNMUTE = "unmuted"
#
# class Action(Enum):
#     VOLUME_UP = "volumeup"
#     VOLUME_DOWN = "volumedown"
#     VOLUME_MUTE = "volumemute"
#     PLAY_PAUSE = "playpause"
#     STOP = "stop"
#     NEXT_TRACK = "nexttrack"
