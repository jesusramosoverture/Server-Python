import asyncio
import websockets
import time


async def init():
    async with websockets.connect("ws://127.0.0.134:5000") as websocket:
        await websocket.send("""{"Id": 1, "Order": {"device": "jesusPcGrande", "IP": "169.150.1.155"}}""")
        print(await websocket.recv())

        for i in range(50000):
            print(await websocket.recv())
            print(f"waiting... {i}")

asyncio.run(init())

# async def main():
#     task = loop.create_task(init())
#     # await asyncio.wait(task)
#     return task
#
# if __name__ == "__main__":
#     try:
#         loop = asyncio.get_event_loop()
#         t1 = loop.run_forever()
#     except Exception as e:
#         pass


