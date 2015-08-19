#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation

class DTXor(DTOperation):
    '''
    Return XORd input as output
    '''

    def needs_key(self):
        '''
        '''
        return True

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
        Return input as output.
        '''
        dt_output = bytearray(len(dt_input))
        for i, current_byte in enumerate(str(dt_input)):
            dt_output[i] = ord(current_byte) ^ ord(dt_key1[i % len(dt_key1)])
        return dt_output
