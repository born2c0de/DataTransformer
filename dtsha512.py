#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from hashlib import sha512

class DTSHA512(DTOperation):
    '''
    Returns SHA512 of input
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
        Return SHA512(input) as output.
        '''
        sha512hash = sha512()
        sha512hash.update(dt_input)
        return sha512hash.hexdigest()
