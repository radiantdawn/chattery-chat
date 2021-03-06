import sqlalchemy as sa
from aiohttp import web


db_conf = {'database': 'chattery', 'user': 'postgres', 'password': 'admin',
           'host': '127.0.0.1', 'port': '5432'}

meta = sa.MetaData()


async def init_pg(app):
    engine = sa.create_engine('postgresql://postgres:admin@127.0.0.1:5432/chattery')
    app['db'] = engine
    meta.bind = engine


def get_table(t_name, engine):
    return sa.Table(t_name, meta, autoload=True)


def form_msg_list():
    resp = ""
    conn = app['db'].connect()
    messages = conn.execute(sa.select([get_table('messages', app['db'])]).order_by('id'))
    for msg in messages:
        resp = resp + "\r\n\r\n" + msg['username'] + ": " + msg['message']
    conn.close()
    return resp


async def get_rlist_handle(request):
    return web.FileResponse("index.html")


async def post_msg_handle(request):
    body = await request.post()
    messages_t = get_table('messages', app['db'])
    conn = app['db'].connect()
    coun_t = sa.select([sa.func.count()]).select_from(messages_t)
    ins = messages_t.insert().\
        values(id=coun_t,
               room_id=11,
               username=body["name"],
               message=body["msg_text"])
    conn.execute(ins)
    conn.close()
    return web.FileResponse("index.html")


async def get_room_handle(request):
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

app.on_startup.append(init_pg)

web.run_app(app, host='127.0.0.1', port=8081)
