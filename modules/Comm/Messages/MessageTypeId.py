#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
"""MSG TYPE ID"""
# ---------------------------------------------------------------------------
from enum import IntEnum


class TypeOfMsg(IntEnum):
    INIT = 1
    VOLUME = 100
    MUTE = 101
    BRIGHTNESS_UP = 102
    BRIGHTNESS_DOWN = 103
