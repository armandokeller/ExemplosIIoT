import asyncio
import aiocoap.resource as resource
import aiocoap

class LedResource(resource.Resource):
    """
    Clase que representa el recurso del led.
    """
    def __init__(self):
        """
        Altera o valor do recurso pelo método PUT
        """
        super().__init__()
        self.estado = "off"
    
    async def render_put(self,request):
        self.estado = request.payload.decode()
        print(f"Atualizado status: {'ligado' if self.estado=='on' else 'desligado'}")
        return aiocoap.Message(code=aiocoap.CHANGED, payload=str(self.estado).encode())


def principal():

    root = resource.Site()
    root.add_resource(['led'],LedResource())

    asyncio.Task(aiocoap.Context.create_server_context(root, bind=("localhost",5683)))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    principal()
