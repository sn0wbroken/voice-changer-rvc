from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class MergeFile:
    filename: str
    strength: int


@dataclass_json
@dataclass
class MergeModelRequest:
    command: str = ""
    slot: int = -1
    defaultTrans: int = 0
    files: List[MergeFile] = field(default_factory=lambda: [])
