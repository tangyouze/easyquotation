import asyncio

import aiohttp
import yarl


# t = easyquotation.use('sina')
# quote = t.all
# print(quote)
async def main():
    async with aiohttp.ClientSession() as c:
        url = yarl.URL('http://hq.sinajs.cn/list=sh601006,sh600000', encoded=True)
        a = await c.get(url)
        print(await a.text())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
