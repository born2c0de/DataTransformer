#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zlib import decompress, compress, error
from dtoperation import DTOperation


class DTZlib(DTOperation):
    '''ZLib compression/decompression'''

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
        '''Return encoded/decoded zlib content.'''
        # TODO: Compress/Decompress in blocks
        if dt_mode == 'enc':
            return compress(str(dt_input))
        elif dt_mode == 'dec':
            try:
                return decompress(str(dt_input))
            except error:
                # Try again without Error CRC checks
                return decompress(str(dt_input), -15)

        return None
