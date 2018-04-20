import asyncio
from aiomysql import create_pool


HOST = '139.199.0.245'
PORT = 3306
USER = 'dear'
PASSWORD = 'both-win'
DB = 'pcc'

loop = asyncio.get_event_loop()

async def list():
    pass


async def like():
    pass

async def count(oid):
    async with create_pool(host=HOST, port=PORT,
                           user=USER, password=PASSWORD,
                           db=DB) as pool:
        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute("select oid, count(uid) from favour where oid=%s group by oid;", oid)
                value = await cur.fetchone()
                return {"oid": value[0],
                        "count": value[1]
                        }

async def is_like():
    pass
