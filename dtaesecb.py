#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
try:
    from Crypto.Cipher import AES
except ImportError:
    print 'Please install the pyCrypto module for the AES module to work'


class DTAESECB(DTOperation):
    '''AES crypto class for ECB mode.'''

    def needs_key(self):
        '''AES key needed with length being a multiple of 16, 24, 32 bytes'''
        return True

    def needs_second_key(self):
        ''''''
        return False

    def needs_IV(self):
        '''No IV needed as this uses ECB mode.'''
        return False

    def transform(self, dt_input, dt_key1=None, dt_key2=None, dt_iv=None, dt_mode='dec'):
        '''Return AES encrypted or decrypted output.'''
        key_length = len(dt_key1)
        input_length = len(dt_input)
        if key_length != 16 and key_length != 24 and key_length != 32:
            print 'AES key must be 16, 24 or 32 bytes long'
            return None
        if input_length % 16 != 0:
            print 'Input data length must be a multiple of 16 bytes.'
            return None
        cipher = AES.new(dt_key1, AES.MODE_ECB)
        if dt_mode == 'dec':
            return cipher.decrypt(str(dt_input))
        else:
            return cipher.encrypt(str(dt_input))
