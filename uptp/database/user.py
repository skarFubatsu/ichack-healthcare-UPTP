""" Create a collection that stores the following attributes of a user
    ~ Display Name
    ~ First Name
    ~ Last Name
    ~ Username
    ~ Unique Id (links users to thier respective documents)
    ~ Password Hash Digest
    ~ Account creation date
 """

from . import MongoClient


class Users:
    def __init__(self):
        self.collection = MongoClient['UserBase']['Details']
