import asyncio
from aiohttp import web
# all user is served by one thread,so it must be fast and cannot use general syn

async def index(request):
    await asyncio.sleep(0.5)
    ret = web.Response(body= b'<h1>Index</h1>' )  #对web这个框架，必须返回response对象
    ret.content_type = 'text/html;charset=utf-8'  #没有这句，会直接下载
    return  '<h1>Index</h1>'

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name'] # match_info ？？？？
    text= web.Response(body=text)
    text.content_type = 'text/html;charset=utf-8'
    return text

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
