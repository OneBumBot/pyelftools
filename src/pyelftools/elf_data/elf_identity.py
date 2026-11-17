from dataclasses import dataclass


@dataclass
class ElfIdentity:
    """
    File identification data
    describe e_ident field from ElfN_Ehdr struct in elf.h
    """

    magic: bytes
    ei_class: int
    ei_data: int
    ei_version: int
    ei_osabi: int
    ei_abiversion: int
    ei_pad: bytes
