#!/usr/bin/env python
# -*- coding: utf-8 -*-
from binascii import hexlify,unhexlify
from dtoperation import DTOperation

class DTNoOp(DTOperation):
    '''
    Do nothing. Return input as output.
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
        Return input as output.
        '''
        return dt_input
