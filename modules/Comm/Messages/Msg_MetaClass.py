#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" FILL """
# ---------------------------------------------------------------------------
import abc


class MessagesPayloadInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __instancecheck__(cls, instance):
        """

        :param instance:
        :return:
        """
        return cls.__subclasscheck__(type(instance))

    @classmethod
    def __subclasshook__(cls, subclass):
        """

        :param subclass:
        :return:
        """
        return (hasattr(subclass, 'serialize_payload') and
                callable(subclass.serialize_payload) and
                hasattr(subclass, 'is_payload_correct') and
                callable(subclass.is_payload_correct) and
                hasattr(subclass, 'send_start_task') and
                callable(subclass.execute_action) and
                hasattr(subclass, 'execute_action')
                or
                NotImplementedError)

    @staticmethod
    @abc.abstractmethod
    def serialize_payload():
        """

        :return:
        """
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def is_payload_correct(message: str) -> bool:
        """

        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def execute_action(self, new_value: int | str | dict) -> None:
        """

        :return:
        """
        raise NotImplementedError
