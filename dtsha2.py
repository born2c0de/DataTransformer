#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from hashlib import sha256


class DTSHA2(DTOperation):
    '''Returns SHA256 of input'''

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
        '''Return SHA256(input) as output.'''
        sha256hash = sha256()
        sha256hash.update(dt_input)
        return sha256hash.hexdigest()
