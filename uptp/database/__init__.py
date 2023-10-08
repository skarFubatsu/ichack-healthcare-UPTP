from motor.motor_asyncio import AsyncIOMotorClient

from uptp.config import Config


MongoClient = AsyncIOMotorClient(Config.MONGO_URI)
Vau = AsyncIOMotorClient(Config.VKXM)
