#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser, Action, FileType
from hexdump import hexdump
from dtoperationfactory import DTOperationFactory

__version__ = '0.01'
__author__ = 'Sanchit Karve'

# Modified from: http://dayabay.bnl.gov/dox/DybPython/html/cmdline_8py_source.html
class opt_hex_input_action(Action):
    'An argparse.Action that handles hex string input'
    def __call__(self,parser, namespace, values, option_string=None):
        # print '%r %r %r' % (namespace, values, option_string)
        base = 10
        if values.startswith('0x'):
            base = 16
        setattr(namespace, self.dest, int(values,base))

def get_choices():
    '''
    Return a list of supported operations.
    '''
    op_list = [
        'cut',
        'hxlfy',
        'rev',
        'b64',
        'lznt',
        'rc4',
        'rc4v1',
        'md5',
        'sha1',
        'sha2',
        'sha512',
        'aesecb',
        'aescbc'
        'gzip',
        'zlib',
        'aplib',
        'tea',
        'xor',
        'add',
        'sub',
        'rol',
        'ror'
    ]
    return op_list

def get_dt_argparser():
    '''
    Return an ArgumentParser object tweaked with DT-specific argument support.
    '''
    from datetime import datetime
    parser = ArgumentParser()
    parser.add_argument('--version',help='Get version number of tool.',action='version',version='Data Transformer v{ver} : (C) 2014-{year} {author}'.format(ver=__version__,year=datetime.now().year,author=__author__))
    parser.add_argument('inputfile',help='Input file where all operations will be performed',type=FileType('rb'))
    parser.add_argument('--of',help='Output file (default:stdout)',dest='outputfile')
    parser.add_argument('-m','--mode',help='Selects encode/decode mode.',choices=['enc','dec'],dest='mode',default='dec')

    parser.add_argument('-o','--op',help='Perform specified operation',dest='operation',choices=get_choices())
    parser.add_argument('-b','--begin',help='Begin reading input from provided offset',dest='begin',action=opt_hex_input_action)
    # User can either provide length of bytes to read or constant offset in file
    grp_end = parser.add_mutually_exclusive_group()
    grp_end.add_argument('-e','--end',help='Stop reading input from provided offset',dest='end',action=opt_hex_input_action)
    grp_end.add_argument('-l','--length',help='Number of bytes to read',dest='length',action=opt_hex_input_action)
    # User can either provide entire keyfile to read or constant offset in inputfile as start of key or the key itself
    grp_keyfile = parser.add_mutually_exclusive_group()
    grp_keyfile.add_argument('--keyfile',help='Use file contents as key',dest='keyfile')
    grp_keyfile.add_argument('--kb','--keybegin',help='Begin reading input for key from provided offset from inputfile',dest='keybegin',action=opt_hex_input_action)
    grp_keyfile.add_argument('-k','--key',help='Use value as key',dest='key',action=opt_hex_input_action)
    # User can either provide length of bytes to read or constant offset in keyfile
    grp_keyend = parser.add_mutually_exclusive_group()
    grp_keyend.add_argument('--ke','--keyend',help='Stop reading input for key from provided offset from inputfile',dest='keyend',action=opt_hex_input_action)
    grp_keyend.add_argument('--kl','--keylen',help='Number of bytes to read as key from inputfile',dest='keylen',action=opt_hex_input_action)
    # User can either provide entire keyfile to read or constant offset in inputfile as start of key2 or the key itself
    grp_key2file = parser.add_mutually_exclusive_group()
    grp_key2file.add_argument('--key2file',help='Use file contents as key2',dest='key2file')
    grp_key2file.add_argument('--k2b','--key2begin',help='Begin reading input for key2 from provided offset from inputfile',dest='key2begin',action=opt_hex_input_action)
    grp_key2file.add_argument('--key2',help='Use value as key2',dest='key2',action=opt_hex_input_action)
    # User can either provide length of bytes to read or constant offset in key2file
    grp_key2end = parser.add_mutually_exclusive_group()
    grp_key2end.add_argument('--k2e','--key2end',help='Stop reading input for key2 from provided offset from inputfile',dest='key2end',action=opt_hex_input_action)
    grp_key2end.add_argument('--k2l','--key2len',help='Number of bytes to read as key2 from inputfile',dest='key2len',action=opt_hex_input_action)
    # User can either provide entire ivfile to read or constant offset in inputfile as start of IV
    grp_ivfile = parser.add_mutually_exclusive_group()
    grp_ivfile.add_argument('--ivfile',help='Use file contents as IV',dest='ivfile')
    grp_ivfile.add_argument('--ivb','--ivbegin',help='Begin reading input for IV from provided offset from inputfile',dest='ivbegin',action=opt_hex_input_action)
    # User can either provide length of bytes to read or constant offset in ivfile
    grp_ivend = parser.add_mutually_exclusive_group()
    grp_ivend.add_argument('--ive','--ivend',help='Stop reading input for IV from provided offset from inputfile',dest='ivend',action=opt_hex_input_action)
    grp_ivend.add_argument('--ivl','--ivlen',help='Number of bytes to read as IV from inputfile',dest='ivlen',action=opt_hex_input_action)
    return parser

def main():
    '''
    OEP of the Data Transformer tool.
    '''
    parser = get_dt_argparser()
    try:
        args = parser.parse_args()
    except IOError as error:
        if error.errno == 2: # No such file or directory
            print 'Input file not found.'
            return
        else:
            print 'UNHANDLED EXCEPTION - CONTACT DEV - ', error
            return

    # Get appropriate DTOperation object based on specified operation
    gen_obj = DTOperationFactory.get_dt_operator(args.operation)
    if not gen_obj:
        print '{op} operation is not implemented yet.'.format(op=args.operation)
        return

    #TODO: Read X MB at a time instead of in 1-go.
    data = args.inputfile.read()
    args.inputfile.close()

    # Extract input bytearray
    data_length = len(data)
    data_start = 0
    if args.begin:
        data_start = args.begin
    if args.length:
        data_length = args.length
    elif args.end and args.end > data_start:
        data_length = args.end - args.begin
    # dt_input can be NULL so no need to check for that.
    # Else, hashes (such as MD5) of null cannot be computed.
    dt_input = bytearray(data[data_start:data_start + data_length])

    if gen_obj.needs_key():
        #TODO: Extract input key array here
        pass
    if gen_obj.needs_second_key():
        #TODO: Extract input key2 array here
        pass
    if gen_obj.needs_IV():
        #TODO: Extract input IV array here
        pass

    #TODO: Pass other arguments (key,IV,key2) here
    # Perform operation and get output
    dt_output = gen_obj.transform(dt_input=dt_input,dt_mode=args.mode)
    if not dt_output:
        print 'Output was NULL.'
        return

    # Dump to file or hexdumped to stdout based on outputfile
    if args.outputfile:
        #TODO: Write X MB at a time instead of in 1-go.
        f = open(args.outputfile,'wb')
        f.write(dt_output)
        f.close()
    else:
        hexdump(str(dt_output))
    return # finito

if __name__ == '__main__':
    main()