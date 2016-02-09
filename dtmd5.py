#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from hashlib import md5

class DTMD5(DTOperation):
    '''
    Returns MD5 of input
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
        Return MD5(input) as output.
        '''
        md5hash = md5()
        md5hash.update(dt_input)
        return md5hash.hexdigest()
