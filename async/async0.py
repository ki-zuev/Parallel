import asyncio
import time

async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    # await asyncio.sleep(0.5)
    print('finifhed')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(end_time-start_time)