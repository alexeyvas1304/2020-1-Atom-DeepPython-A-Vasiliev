import time
import asyncio
import aiohttp


def write_file(data):
    name = f'photo_{int(time.time() * 1000)}'
    with open(name, 'wb') as f:
        f.write(data)


# Исходный
# async def fetch(url, session):
#     async with session.get(url, allow_redirects=True) as resp:
#         data = await resp.read()
#         write_file(data)

#  C aiofiles
# async def write_file(data):
#     name = f'Downloaded_imgs/photo_{int(time.time() * 1000)}.jpg'
#     async with aiofiles.open(name, mode='wb') as f:
#         await f.write(data)
#         await f.close()
#
#
# async def fetch(url, session):
#     async with session.get(url, allow_redirects=True) as resp:
#         data = await resp.read()
#         await write_file(data)

async def fetch(url, session):
    async with session.get(url, allow_redirects=True) as resp:
        data = await resp.read()
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, write_file, data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(fetch(url, session)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()

    print('TT', t2 - t1)

