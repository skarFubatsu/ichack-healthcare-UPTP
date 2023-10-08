""" Create a collection that stores the following attributes of a user
    ~ Display Name
    ~ First Name
    ~ Last Name
    ~ Username
    ~ Unique Id (links users to thier respective documents)
    ~ Password Hash Digest
    ~ Account creation date
 """
import secrets
from uptp.types.perms import Patient

from . import MongoClient


class Users:
    def __init__(self):
        self.collection = MongoClient['UserBase']['Details']

    async def update(self, user: Patient):
        """update any changes made to user details such as username, display name etc."""

        query = {
            "userId": user.userId
        }
        db_data = await self.collection.find_one(query)
        if db_data is None:
            return False
        if any([
            db_data.username != user.username,
            db_data.first_name != user.first_name,
            db_data.last_name != user.last_name
        ]):
            # Check for changes in public information regarding patient.
            # This should not alter password_hash and other sensitive data.
            data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
            return await self.collection.update_one(query, {"$set": data})
        return False

    async def insert(self, user: Patient):
        '''add a new entity to database'''
        query = {
            "userId": user.userId
        }
        if (await self.collection.find_one(query)) is not None:
            # There is already a user with said id, raise error later.
            return False
        return await self.collection.insert_one(user.model_dump())

    async def compare_hash(self, uid: int, other: str):
        '''compare passwprd hash saved in db'''
        _dsx = await self.collection.find_one({"userId": uid})
        if _dsx is None:
            return False
        return secrets.compare_digest(_dsx["passh"], other)

    async def set_hash(self, uid:  int, pssh: str):
        _dsx = await self.collection.find_one({'userId': uid})
        if _dsx is None:
            return False
        # Hmmm, gotta revise the logic for this...
        return 