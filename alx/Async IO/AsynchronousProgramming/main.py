import asyncio

async def main():
    print('Taya')
    # await foo('taya')
    task = asyncio.create_task(foo('taya'))
    # await task
    print('finished')

async def foo(text):
    print(f'Welcome {text}')
    await asyncio.sleep(1)


asyncio.run(main())