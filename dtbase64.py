#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base64 import b64encode, b64decode
from dtoperation import DTOperation


class DTBase64(DTOperation):
    '''Uses built-in library for base64 encoding and decoding.'''

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
        '''Return Base64 encoded/decoded output.'''
        if dt_mode == 'enc':
            return b64encode(dt_input)
        elif dt_mode == 'dec':
            return b64decode(dt_input)
        return None
