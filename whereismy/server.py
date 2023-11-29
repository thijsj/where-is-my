
__all__ = ['web_app']

from aiohttp import web

async def index(request):
    return web.Response(text="Welkom thuis!")


async def web_app():
    app = web.Application()
    app.router.add_get('/', index)
    return app
