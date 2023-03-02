import asyncio
from umongo.frameworks import MotorAsyncIOInstance
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings


client = AsyncIOMotorClient(settings.APP_DB_MONGO_URI)[settings.APP_DB_MONGO_NAME]

client.get_io_loop = asyncio.get_running_loop
umongo_instance = MotorAsyncIOInstance(client)