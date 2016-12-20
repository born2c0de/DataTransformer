#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from Crypto.Cipher import DES3


class DTTripleDES(DTOperation):
    '''Triple DES ECB Crypto Class.'''

    def needs_key(self):
        ''''''
        return True

    def needs_second_key(self):
        ''''''
        return False

    def needs_IV(self):
        ''''''
        return False

    def transform(self, dt_input, dt_key1=None, dt_key2=None, dt_iv=None, dt_mode='dec'):
        '''Return TripleDES transformed output'''
        des = DES3.new(str(dt_key1), DES3.MODE_ECB)
        if dt_mode == 'dec':
            return des.decrypt(str(dt_input))
        else:
            return des.encrypt(str(dt_input))
