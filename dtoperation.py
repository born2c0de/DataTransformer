#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class DTOperation:
    '''
    Abstract class which serves as parent object of all DTOperations.
    All DTOperation child classes must implement all functions prototyped below.
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def needs_key(self):
        '''
        Return True if Operation requires Key.
        '''
        pass

    @abstractmethod
    def needs_second_key(self):
        '''
        Return True if Operation requires second key.
        '''
        pass

    @abstractmethod
    def needs_IV(self):
        '''
        Return False if Operation requires IV.
        '''
        pass


    @abstractmethod
    def transform(self,dt_input,dt_key1=None,dt_key2=None,dt_iv=None,dt_mode='dec'):
        '''
        Main function which will be overridden in child classes.
        transform contains the actual operation code.

            Arguments:
                dt_input = bytearray containing input
                dt_key1  = bytearray containing key (or None)
                dt_key2  = bytearray containing second key (or None)
                dt_iv    = bytearray containing IV (or None)
                dt_mode  = Either 'enc' or 'dec'. default to 'dec'

            Return:
                bytearray of output
        '''
        pass