#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dthexlify import DTHexlify
from dtnoop import DTNoOp
from dtrc4 import DTRC4

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
        else:
            return None
