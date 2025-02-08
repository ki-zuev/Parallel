import asyncio
import time

async def do_ticking(amount_of_ticks, sound):
    for _ in range(amount_of_ticks):
        print(sound)
        await asyncio.sleep(1)
    print('BOOM!')

async def main():
    task1 = asyncio.create_task(do_ticking(1, 'tick'))
    task2 = asyncio.create_task(do_ticking(5, 'chick'))
    task3 = asyncio.create_task(do_ticking(9, 'click'))
    await task1
    await task2
    await task3

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(end_time-start_time)