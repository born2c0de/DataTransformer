#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dtoperation import DTOperation
from StringIO import StringIO
from gzip import GzipFile


class DTGZip(DTOperation):
    '''Contains GZip Compression/Decompression Handlers'''

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
        '''Launch GZip compression and decompression'''
        if dt_mode == 'dec':
            compressed_data = StringIO()
            decompressed_data = StringIO()
            compressed_data.write(dt_input)
            compressed_data.seek(0)
            decompressed_file = GzipFile(fileobj=compressed_data, mode='rb')
            decompressed_data.write(decompressed_file.read())
            decompressed_file.close()
            return decompressed_data.getvalue()
        else:
            compressed_data = StringIO()
            compressed_file = GzipFile(fileobj=compressed_data, mode='wb')
            compressed_file.write(str(dt_input))
            compressed_file.close()
            return compressed_data.getvalue()
