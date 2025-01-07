import asyncio
from aiohttp import web

async def on_stasis_start(request):
    data = await request.json()
    print("Evento recibido:", data)

    return web.Response(text="Evento manejado correctamente")

# Crear la aplicación web
app = web.Application()
app.router.add_post('/stasis_start', on_stasis_start)

if __name__ == '__main__':
    print("Iniciando manejador Stasis en el puerto 8088...")
    web.run_app(app, host='0.0.0.0', port=8088)
