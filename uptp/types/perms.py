from enum import IntEnum

from pydantic import BaseModel


class Perms(IntEnum):
    """Defines the permission values"""
    READ = 0
    EDIT = 1
    DELETE = 2
    UNAUTHORIZED = -1


class Patient(BaseModel):
    """basic structure for patient entity"""
    name: str
    perms: int = Perms.EDIT + Perms.DELETE


class HealthCare(BaseModel):
    """basic structure for healthcare organization"""
    title: str
    perms: int = Perms.READ
