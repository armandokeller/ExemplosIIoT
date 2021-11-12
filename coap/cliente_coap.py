import asyncio
from aiocoap import *
from aiocoap.interfaces import Request

async def principal():
    contexto = await Context.create_client_context()
    
    status_led = ""
    while status_led not in ['on','off']:
        status_led = input("Setar estado do LED: [on,off]: ").strip().lower()

    request = Message(code=PUT, payload=str(status_led).encode('utf-8'), uri='coap://localhost:5683/led')
    response = await contexto.request(request).response

    print(f'Resposta: {response.code}\n{response.payload}')

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(principal())

