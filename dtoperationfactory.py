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

class DTOperationFactory:
    '''
    Factory class for DTOperation objects.
    '''

    @staticmethod
    def get_dt_operator(operation=None):
        '''
        Returns appropriate DTOperation object.
        '''
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
        else:
            return None
