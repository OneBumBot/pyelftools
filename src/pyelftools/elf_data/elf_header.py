from dataclasses import dataclass

from .elf_identity import ElfIdentity


@dataclass
class ElfHeader:
    """
    Elf file header
    describe ElfN_Ehdr struct from elf.h
    """

    e_ident: ElfIdentity  # byte array, describe how to read file
    e_type: int  # object file type
    e_machine: int  # required file arch
    e_version: int  # file version
    e_entry: int  # virtual address for entrypoint
    e_phoff: int  # program header offset
    e_shoff: int  # section header offset
    e_flags: int  # specific processor flags
    e_ehsize: int  # elf header size in bytes
    e_phentsize: int  # size of program header element
    e_phnum: int  # number of program header elements; phnum*phentsize= ph table size in bytes; TODO: read about PN_XNUM
    e_shentsize: int  # size of section header element
    e_shnum: int  # number of section header elements; shnum*shentsize = sh table size in bytes; TODO: read about SHN_LORESERVE
    e_shstrndx: int  # section header index of pointer to headers names table
