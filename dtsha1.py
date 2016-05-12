#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from hashlib import sha1


class DTSHA1(DTOperation):
    '''Returns SHA1 of input'''

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
        '''Return SHA1(input) as output.'''
        sha1hash = sha1()
        sha1hash.update(dt_input)
        return sha1hash.hexdigest()
