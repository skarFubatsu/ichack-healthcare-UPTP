from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, HttpUrl


class Perms(IntEnum):
    """Defines the permission values"""
    READ = 0
    EDIT = 1
    DELETE = 2
    UNAUTHORIZED = -1  # Banned from API access


class Patient(BaseModel):
    """basic structure for patient entity"""
    perms: int = Perms.EDIT + Perms.DELETE
    display_name: Optional[str]
    first_name: str
    last_name: str
    username: str
    userId: int


class HealthCare(BaseModel):
    """basic structure for healthcare organization"""
    title: str
    perms: int = Perms.READ
    owner: str
    license: HttpUrl
