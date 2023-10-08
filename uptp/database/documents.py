""" access the saved documents """

from uptp.database import MongoClient, Vau
from uptp.types.document import File


class Documents:
    def __init__(self) -> None:
        self.collection = MongoClient.srdsx["__edst"]
        self.__vau = Vau["__ieu"]

    async def fetch(self, access_hash: int, file_ref: str):
        return await self.collection.find_one({'access_hash': access_hash, 'file_ref': file_ref})

    async def save_doc(self, access_hash: int, encrpt_data: str, key: str, file: File):
        