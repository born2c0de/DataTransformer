#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from Crypto.Cipher import DES


class DTDESCBC(DTOperation):
    '''DES CBC Crypto Class.'''

    def needs_key(self):
        ''''''
        return True

    def needs_second_key(self):
        ''''''
        return False

    def needs_IV(self):
        ''''''
        return True

    def transform(self, dt_input, dt_key1=None, dt_key2=None, dt_iv=None, dt_mode='dec'):
        '''Return DES transformed output'''
        des = DES.new(str(dt_key1), DES.MODE_CBC, str(dt_iv))
        if dt_mode == 'dec':
            return des.decrypt(str(dt_input))
        else:
            return des.encrypt(str(dt_input))
