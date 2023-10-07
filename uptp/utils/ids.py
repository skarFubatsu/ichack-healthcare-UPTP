import hashlib
import struct
import random
import time
import base64

import aiofiles

from uptp.constants import CHUNK, STRUCT_FID_PACK


async def get_file_hash(path: str) -> str:
    """generates a SHA256 for the given file path"""
    h_obj = hashlib.sha256()
    async with aiofiles.open(path, 'rb') as file:
        while True:
            data = await file.read(CHUNK)
            if not data:
                break
            h_obj.update(data)
    return h_obj.hexdigest()


async def generate_file_id(uid: int, path: str, byte_len: int = 4):
    file_hash = await get_file_hash(path)
    packet = struct.pack(
        STRUCT_FID_PACK.format(byte_len=byte_len),
        uid, random.randbytes(byte_len), file_hash.encode(), int(time.time())
    )
    return base64.b64encode(packet).decode("utf-8")
