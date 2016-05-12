#!/usr/bin/env python
# -*- coding: utf-8 -*-
from binascii import hexlify, unhexlify
from dtoperation import DTOperation


class DTHexlify(DTOperation):
    '''
    Returns Hexlified and UnHexlified data.
    Useful for scripts and binaries with hardcoded and hexlified shellcode.
    '''

    def needs_key(self):
        ''''''
        return False

    def needs_second_key(self):
        ''''''
        return False

    def needs_IV(self):
        ''''''
        return False

    def transform(self, dt_input, dt_key1=None, dt_key2=None, dt_iv=None, dt_mode='dec'):
        ''''''
        if dt_mode == 'enc':
            return hexlify(dt_input)
        elif dt_mode == 'dec':
            return unhexlify(dt_input)
        return None
