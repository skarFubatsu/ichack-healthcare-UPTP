""" access the saved documents """

from uptp.database import MongoClient, Vau
from uptp.types.document import File


class Documents:
    def __init__(self) -> None:
        self.collection = MongoClient.srdsx["__edst"]
        self.__vau = Vau["__ieu"]['owlxs']

    async def fetch(self, access_hash: int, file_ref: str):
        '''retrive a document from database

        param:
            access_hash (```int```) unique identifier of author/ owner of document

            file_ref (```str```) short id to locate a document from warehouse
        '''
        return await self.collection.find_one({'access_hash': access_hash, 'file_ref': file_ref})

    async def save_doc(self, access_hash: int, encrpt_data: str, key: str, file: File):
        """ save a document to warehouse

        param:
            access_hash (```int```) unique identifier of owner of file

            encrpt_data (```str```) base64 encoded encrypted data that needs to be stored

            key (```str```) base64 encoded encryption key that will be sent to remote vault

            file (```File```) metadata of the file that needs to be stored in central repository
        """
        exists = await self.fetch(access_hash, file.ref)
        if exists:
            # Handle file exists
            return False
        await self.__vau.insert_one({'_idxs': file.ref, "acs": access_hash, "k": key})
        return await self.collection.insert_one({
            'doc': file.type, 'dsx': encrpt_data, 'rsx': file.ref, 'hsx': file.id
        })

    async def delete_doc(self, access_hash: int, file: File):
        """ delete a document associated to the provided author and file metadata

        param:
            access_hash (```int```) unique identifier of owner of file

            file (```File```) metadata of the file that needs to be stored in central repository
        """
        exists = await self.fetch(access_hash, file.ref)
        if not exists:
            return False
        await self.__vau.delete_one({'_idxs': file.ref, 'acs': access_hash})
        return await self.collection.delete_one({'doc': file.type, 'rsx': file.ref, "hsx": file.id})
    
    async def edit(self, access_hash: int, encrpt_data: str, key: str, file: File):
        """ shorthand method to replace a document saved in warehouse

        param:
            access_hash (```int```) unique identifier of owner of file

            encrpt_data (```str```) base64 encoded encrypted data that needs to be stored

            key (```str```) base64 encoded encryption key that will be sent to remote vault

            file (```File```) metadata of the file that needs to be stored in central repository
        """
        await self.delete_doc(access_hash, file)
        return await self.save_doc(access_hash, encrpt_data, key, file)

