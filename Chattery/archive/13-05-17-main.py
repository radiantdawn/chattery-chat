from aiohttp import web


messages = []


def form_msg_list():
    resp = ""
    for msg in messages:
        resp = resp + "\r\n\r\n" + msg[0] + ": " + msg[1]
    return resp


async def get_rlist_handle(request):
    return web.FileResponse("index.html")

async def post_msg_handle(request):
    body = await request.post()
    messages.append((body["name"], body["msg_text"]))
    return web.FileResponse("index.html")

async def get_room_handle(request):
    messages.append(("nobody", "nothing"))
    return web.Response(text=form_msg_list())

app = web.Application()
app.router.add_get('', get_rlist_handle)
app.router.add_get('/room/{room_id}', get_room_handle)
app.router.add_post('', post_msg_handle)
app.router.add_post('/room/{room_id}', post_msg_handle)
app.router.add_static('/css',
                      path="E:\workspace\chattery-chat\Chattery/css",
                      name='css')
app.router.add_static('/js',
                      path="E:\workspace\chattery-chat\Chattery/js",
                      name='js')
app.router.add_static('/img',
                      path="E:\workspace\chattery-chat\Chattery/img",
                      name='img')

web.run_app(app, host='127.0.0.1', port=8081)
