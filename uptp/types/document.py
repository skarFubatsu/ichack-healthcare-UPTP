from enum import IntEnum

from pydantic import BaseModel


class DocType(IntEnum):
    """specify the type of doc we are working with"""
    MEDICAL_RECORD = 1
    PRESCRIPTION = 2
    TEST_RESULT = 3
    TREATMENT_PLAN = 4


class File(BaseModel):
    '''basic struct for a file type entity'''
    id: str
    ref: str
    type: DocType
