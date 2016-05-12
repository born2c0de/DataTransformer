#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation


class DTReverse(DTOperation):
    '''Return reversed input as output.'''

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
        '''Return reversed input as output.'''
        return bytearray([x for x in reversed(dt_input)])
