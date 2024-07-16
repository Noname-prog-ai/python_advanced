import threading
import multiprocessing
import asyncio
import aiohttp
import time
import requests

async def download_cat_image(url, session):
    async with session.get(url) as response:
        return await response.read()

def download_cats_with_threads(urls):
    start_time = time.time()
    thread_list = []

    for url in urls:
        thread = threading.Thread(target=download_cat_image_sync, args=(url,))
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()

    end_time = time.time()
    print(f"Время, затраченное на загрузку {len(urls)} изображения кошек с резьбой: {end_time - start_time} секунд")

def download_cats_with_processes(urls):
    start_time = time.time()
    process_list = []

    for url in urls:
        process = multiprocessing.Process(target=download_cat_image_sync, args=(url,))
        process.start()
        process_list.append(process)

    for process in process_list:
        process.join()

    end_time = time.time()
    print(f"Время, затраченное на загрузку {len(urls)} изображения кошек с процессами: {end_time - start_time} секунд")

def download_cats_with_coroutines(urls):
    start_time = time.time()
    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = [download_cat_image(url, session) for url in urls]
            await asyncio.gather(*tasks)

    asyncio.run(main())

    end_time = time.time()
    print(f"Время, затраченное на загрузку {len(urls)} изображения кошек с помощью сопрограмм: {end_time - start_time} секунд")

def download_cat_image_sync(url):
    response = requests.get(url)
    return response.content

# Протестируйте функции на разном количестве изображений
urls_10 = ['https://cataas.com/cat']*10
urls_50 = ['https://cataas.com/cat']*50
urls_100 = ['https://cataas.com/cat']*100

download_cats_with_threads(urls_10)
download_cats_with_threads(urls_50)
download_cats_with_threads(urls_100)

download_cats_with_processes(urls_10)
download_cats_with_processes(urls_50)
download_cats_with_processes(urls_100)

download_cats_with_coroutines(urls_10)
download_cats_with_coroutines(urls_50)
download_cats_with_coroutines(urls_100)