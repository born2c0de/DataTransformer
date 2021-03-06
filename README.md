
# DataTransformer - DT

DT is a command-line, static-analysis tool intended for malware researchers and reverse engineers.
It contains routines for various decompression and decryption algorithms typically used by malware.

It is licensed under GNU/GPL version 3.

# Scope

Note that the aim of the project is not to implement all compression and encryption algorithms.

The objective is to document algorithms used for obfuscation and data-hiding seen in malware samples. The idea is to have one tool capable of statically revealing crypted or compressed data within a malware sample instead of needing a collection of tools to decrypt data or debugging samples to arrive at the decrypted data. Individual operations can be combined and sent to DT (for example: Rolling XOR + ADD).

## Example Use Cases:

TODO

# Supported Algorithms
- [x] Cut (Extract selected bytes)
- [x] Reverse (Reverses selected bytes)
- [x] UnHexlify + Hexlify (Converts raw bytes into string representations of its hex equivalent)
- [x] Base64
- [x] CRC32
- [x] MD5
- [x] SHA1
- [x] SHA256
- [x] SHA512
- [x] AES (ECB mode)
- [ ] AES (CBC mode)
- [x] GZip
- [x] APLIB
- [x] RC4
- [ ] Modified RC4 (Spritz)
- [ ] LZNT
- [ ] TEA
- [x] ZLIB
- [ ] Simple ADD/SUB
- [ ] Rolling ADD/SUB
- [x] Simple XOR (w/ N-byte key)
- [ ] Rolling XOR (w/ N-byte key)
- [ ] Rolling XOR (w/ N-byte key)
- [ ] RoL/RoR
- [x] DES (ECB mode)
- [x] TripleDES (ECB mode)
- [ ] DES (CBC mode)
- [ ] DES (CFB mode)
- [x] .NET SmartAssembly Packer Resource Decryptor

# Build

DT is written in Python 2.7.9+.

# Dependencies (TODO:)

- [pyCrypto package](https://pypi.python.org/pypi/pyCrypto)

# External Libraries/Code Used

- [APLIB support](http://code.google.com/p/kabopan/)
- [hexdump functionality](https://pypi.python.org/pypi/hexdump)


# Contributions

Feel free to send pull requests and bug reports.
