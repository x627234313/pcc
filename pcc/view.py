import aiomysql

async def list():
    pass


async def like():
    pass


async def count():
    pass


async def is_like(uid, oid):
    async with aiomysql.create_pool(host='139.199.0.245', port=3306,
                           user='dear', password='both-win',
                           db='pcc') as pool:
        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await res = cur.execute('''SELECT uid, oid
                                  FROM  favour
                                  WHERE uid=%s AND oid=%s;''',(uid, oid))
                if res:
                    return {'status':'yes'}
                else:
                    return {'status':'no'}

