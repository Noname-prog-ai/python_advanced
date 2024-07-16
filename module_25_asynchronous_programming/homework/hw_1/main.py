import aiohttp
import asyncio

async def download_cat_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open('cat_image.jpg', 'wb') as file:
                file.write(data)

url = 'https://www.example.com/cat.jpg'
loop = asyncio.get_event_loop()
loop.run_until_complete(download_cat_image(url))