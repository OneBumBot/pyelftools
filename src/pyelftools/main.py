import pprint as pp
import struct
from enum import Enum
from pathlib import Path

from .elf_data import ElfHeader, ElfIdentity, EMachine, EType


def read_elf_header(file_path: Path) -> ElfHeader | None:
    with open(file_path, "rb") as file:
        identity = file.read(16)
        identity = ElfIdentity(*struct.unpack(">4sBBBBB7s", identity[:16]))
        if identity.magic != b"\x7fELF":
            print("Its not an elf file")
            return None
        elf_class = identity.ei_class
        byte_order = identity.ei_data
        if elf_class == 1:
            print("arch: x86")
            address_format = "I"
        elif elf_class == 2:
            print("arch: x86_64")
            address_format = "Q"
        else:
            print("arch: unknown")
            return None
        if byte_order == 1:
            print("byte order: litte endian")
            struct_byte_order = "<"
        elif byte_order == 2:
            print("byte order: big endian")
            struct_byte_order = ">"
        else:
            print("byte order: invalid")
            return None

        unpack_pattern = f"{struct_byte_order}HHI{address_format * 3}IHHHHHH"
        size = struct.calcsize(unpack_pattern)

        header = file.read(size)
        elf_header = ElfHeader(identity, *struct.unpack(unpack_pattern, header))
        file_type = EType(elf_header.e_type)
        machine = EMachine(elf_header.e_machine)
        print(f"filetype: {file_type.name}")
        print(f"machine: {machine.name}")
        print(
            f"e_entry: {elf_header.e_entry}\ne_phoff: {elf_header.e_phoff}, e_phnum: {elf_header.e_phnum}\ne_shoff: {elf_header.e_shoff}, e_shnum: {elf_header.e_shnum}"
        )
    return elf_header


def main():
    header = read_elf_header(Path("/usr/bin/ls"))
    if header == None:
        print("Error parsing elf file")
    pp.pprint(header)


if __name__ == "__main__":
    main()
