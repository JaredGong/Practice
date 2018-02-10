# -*- coding:utf-8 -*-

import asyncio

#@asyncio.coroutine
async def hello():
    print('hello the fuck world')
 #   yield from asyncio.sleep(1)
    await asyncio.sleep(1)
    print('silly b')

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
