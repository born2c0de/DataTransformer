#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation

class DTRC4(DTOperation):
    '''
    Performs RC4 encryption/decryption.
    Since function is symmetric, mode can be ignored.
    Algorithm perf-optimized from Thimo Kraemer's implementation at http://www.joonis.de/en/code/rc4-algorithm
    '''

    def needs_key(self):
        '''
        '''
        return True

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
        Perform RC4.
        '''
        swap1 = 0
        box = range(256)
        for i in xrange(256):
            swap1 = (swap1 + box[i] + ord(dt_key1[i % len(dt_key1)])) % 256
            box[i], box[swap1] = box[swap1], box[i]
        swap1 = 0
        swap2 = 0
        dt_output = bytearray(len(dt_input))
        for i, current_byte in enumerate(str(dt_input)):
            swap1 = (swap1 + 1) % 256
            swap2 = (swap2 + box[swap1]) % 256
            box[swap1], box[swap2] = box[swap2], box[swap1]
            dt_output[i] = ord(current_byte) ^ box[(box[swap1] + box[swap2]) % 256]
        return dt_output
