import os


class Config:
    """ acts as containner for config variables """
    MONGO_URI = os.getenv("MONGO_URI")
    # Serves as storage for keys
    VKXM = os.getenv("MDBK")
