"""
Bluetooth connector proof of concept
"""


from aiohttp import web
import logging
import bluetooth


LOGGER = logging.getLogger(__name__)
routes = web.RouteTableDef()


def setup(app: web.Application):
    app.router.add_routes(routes)


def discover():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    LOGGER.info(f'discovered {nearby_devices}')
    return nearby_devices


@routes.get('/discover')
async def get_discover(request):
    """
    ---
    tags:
    - Bluetooth
    summary: Discover nearby bluetooth devices
    operationId: bluetooth.discover
    produces:
    - application/json
    """
    return web.json_response(discover())
