
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

import orm

@asyncio.coroutine
def init(loop):
	
    yield from orm.create_pool(loop=loop, host='10.21.31.9', port=3316, user='root', password='root', db='awesome')
    u=User(name='test',email='test@test.com',password='test', image='about:blank')
    yield from u.save()

   # app = web.Application(loop=loop)
   # srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
   # logging.info('server started at http://127.0.0.1:9000...')
   # return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
