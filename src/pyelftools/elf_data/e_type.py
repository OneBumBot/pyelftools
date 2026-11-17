from enum import Enum


class EType(Enum):
    NONE = 0
    RELOCATABLE = 1
    EXECUTABLE = 2
    DYNAMIC = 3
    CORE = 4
