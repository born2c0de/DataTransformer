#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from binascii import crc32

class DTCRC32(DTOperation):
    '''
    Returns CRC32 of input
    '''

    def needs_key(self):
        '''
        '''
        return False

    def needs_second_key(self):
        '''
        '''
        return False

    def needs_IV(self):
        '''
        '''
        return False

    def transform(self,dt_input,dt_key1=None,dt_key2=None,dt_iv=None,dt_mode='dec'):
        '''
        Return CRC32(input) as output.
        '''
        return crc32(dt_input)
