#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

from enum import IntEnum

class QL_ENDIAN(IntEnum):
    EL = 1
    EB = 2

class QL_ARCH(IntEnum):
    X86 = 1
    X8664 = 2
    ARM = 3
    ARM_THUMB = 4
    ARM64 = 5
    MIPS32 = 6

class QL_OS(IntEnum):
    LINUX = 1
    FREEBSD = 2
    MACOS = 3
    WINDOWS = 4
    POSIX = 5

class QL_OUTPUT(IntEnum):
    OFF = 1
    DEFAULT = 2
    DISASM = 3
    DEBUG = 4
    DUMP = 5

class QL_DEBUGGER(IntEnum):
    GDB = 1
    IDAPRO = 2

D_INFO = 1 # GENERAL DEBUG INFO
D_PROT = 2 # FLAG, PROTOCOL DEBUG INFO
D_CONT = 3 # Print out content
D_RPRT = 4 # Extrame OUTPUT

QL_DEBUGGER_ALL = [QL_DEBUGGER.IDAPRO, QL_DEBUGGER.GDB]
QL_ARCH_ALL = [QL_ARCH.X86, QL_ARCH.X8664, QL_ARCH.ARM, QL_ARCH.ARM64, QL_ARCH.MIPS32]
QL_ENDINABLE = [QL_ARCH.MIPS32, QL_ARCH.ARM]
QL_OS_ALL = [QL_OS.LINUX, QL_OS.FREEBSD, QL_OS.MACOS, QL_OS.WINDOWS, QL_OS.POSIX]
QL_POSIX = [QL_OS.LINUX, QL_OS.FREEBSD, QL_OS.MACOS]
