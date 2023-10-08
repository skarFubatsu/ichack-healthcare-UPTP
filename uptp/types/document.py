from enum import IntEnum

from pydantic import BaseModel


class DocType(IntEnum):
    """"""
    MEDICAL_RECORD = 1
    PRESCRIPTION = 2
    TEST_RESULT = 3
    TREATMENT_PLAN = 4


class File(BaseModel):
    id: str
    ref: str
