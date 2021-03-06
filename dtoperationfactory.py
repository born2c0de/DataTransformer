#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dthexlify import DTHexlify
from dtnoop import DTNoOp
from dtrc4 import DTRC4
from dtbase64 import DTBase64
from dtzlib import DTZlib
from dtreverse import DTReverse
from dtxor import DTXor
from dtaesecb import DTAESECB
from dtsha1 import DTSHA1
from dtsha2 import DTSHA2
from dtsha512 import DTSHA512
from dtmd5 import DTMD5
from dtcrc32 import DTCRC32
from dtaplib import DTAplib
from dtgzip import DTGZip
from dtdesecb import DTDESECB
from dtdescbc import DTDESCBC
from dttdesecb import DTTripleDES
from dtsmartasm import DTSmartAsm


class DTOperationFactory:
    '''Factory class for DTOperation objects.'''

    @staticmethod
    def get_dt_operator(operation=None):
        '''Returns appropriate DTOperation object.'''
        if not operation:
            return DTNoOp()
        elif operation == 'hxlfy':
            return DTHexlify()
        elif operation == 'rc4':
            return DTRC4()
        elif operation == 'b64':
            return DTBase64()
        elif operation == 'zlib':
            return DTZlib()
        elif operation == 'rev':
            return DTReverse()
        elif operation == 'xor':
            return DTXor()
        elif operation == 'aesecb':
            return DTAESECB()
        elif operation == 'sha1':
            return DTSHA1()
        elif operation == 'sha2':
            return DTSHA2()
        elif operation == 'sha512':
            return DTSHA512()
        elif operation == 'md5':
            return DTMD5()
        elif operation == 'crc32':
            return DTCRC32()
        elif operation == 'aplib':
            return DTAplib()
        elif operation == 'gzip':
            return DTGZip()
        elif operation == 'desecb':
            return DTDESECB()
        elif operation == 'descbc':
            return DTDESCBC()
        elif operation == 'smartasm':
            return DTSmartAsm()
        elif operation == 'tdesecb':
            return DTTripleDES()
        else:
            return None
