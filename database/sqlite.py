import aiosqlite
from config import DATABASES

async def get_sqlite():
    conf = next(db for db in DATABASES if db["type"] == "sqlite" and db["enabled"])
    db = await aiosqlite.connect(conf["file"])
    return db