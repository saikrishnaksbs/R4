# core_nats1.py

from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers
nc = NATS()

async def message_handler(msg):
    print(f"Core NATS 4 received a message: {msg.data.decode()}")
    await msg.ack()

async def run(loop):
    
    await nc.connect(servers=["nats://0.0.0.0:4222"])
    await nc.subscribe("nila.4.*", cb=message_handler)

    print("Core NATS 4 is subscribed to nila.3.*")

    await nc.flush() # Keep the connection alive
    

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()
