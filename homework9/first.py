import json
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import argparse
from collections import Counter
from stop_words import stop_words
import time

parser = argparse.ArgumentParser(description="fetcher")
parser.add_argument("-c", "--count", type=int, help="Count of simultaneous requests")
parser.add_argument("path", type=str)
args = parser.parse_args()


def get_web_page_data(url):
    soup = BeautifulSoup(url, 'html.parser')
    lst_of_words = soup.get_text().split()
    lst_cleared_1_stage = list(map(lambda x: x.strip('()[]/.,!?<>=;:').lower(), lst_of_words))
    lst_cleared_2_stage = list(filter(lambda x: len(x) > 1 and x not in stop_words, lst_cleared_1_stage))
    dict_of_popular_words = dict(Counter(lst_cleared_2_stage).most_common(10))
    response = json.dumps(dict_of_popular_words, ensure_ascii=False)
    return response


async def fetch(url, session):
    async with session.get(url) as resp:
        data = await resp.read()
        url_data = get_web_page_data(data)
        print(url_data)


async def main(count_conn, file_urls):
    tasks = []
    conn = aiohttp.TCPConnector(limit=count_conn)

    async with aiohttp.ClientSession(connector=conn) as session:
        with open(file_urls, "r") as f:
            for line in f:
                tasks.append(asyncio.create_task(fetch(line.rstrip(), session)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main(args.count, args.path))
    t2 = time.time()

    print('TT', t2 - t1)
