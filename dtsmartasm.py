#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from dtdescbc import DTDESCBC
from dtzlib import DTZlib


class DTSmartAsm(DTOperation):
    '''
        Smart Assembly Resource Decryptor
        The only input needed is dt_input containing an encrypted .NET resource
        This class will decrypt and decompress the resource using DES & deflate respectively and return output
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
        '''Return DES decrypted + deflated output'''
        des = DTDESCBC()
        decrypted = des.transform(dt_input=dt_input[0x13:], dt_key1=dt_input[0xb: 0xb + 0x8], dt_iv=dt_input[0x3:0x3 + 0x8])
        zlib = DTZlib()
        return zlib.transform(dt_input=decrypted)
