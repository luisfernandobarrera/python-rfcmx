#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


class CURPException(Exception):
    pass


class CURPLengthError(CURPException):
    pass


class CURPStructureError(CURPException):
    pass


class CURPGeneral(object):
    general_regex = re.compile(
        r"[A-Z][AEIOUX][A-Z]{2}[0-9]{2}[0-1][0-9][0-3][0-9][M,H][A-Z]{2}[BCDFGHJKLMNPQRSTVWXYZ]{3}[0-9,A-Z][0-9]"
    )
    length = 19

    def validate(self, value):
        value = value.strip()
        if len(value) == self.length:
            if self.general_regex.match(value):
                return True
            else:
                raise CURPLengthError("CURP length must be 19")
        else:
            raise CURPStructureError("Invalid CURP structure")

