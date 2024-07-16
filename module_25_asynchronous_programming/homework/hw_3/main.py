import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re

class Crawler:
    def __init__(self, max_iterations=3):
        self.max_iterations = max_iterations
        self.visited_urls = set()
        self.external_urls = set()

    async def fetch(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def extract_urls(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href.startswith('http'):
                self.external_urls.add(href)

    async def crawl(self, url, iteration=1):
        if url in self.visited_urls or iteration > self.max_iterations:
            return

        print(f'Crawling: {url}')

        html = await self.fetch(url)
        await self.extract_urls(html)

        self.visited_urls.add(url)

        for link in self.external_urls:
            await self.crawl(link, iteration + 1)

    async def run(self, urls):
        tasks = [self.crawl(url) for url in urls]
        await asyncio.gather(*tasks)

        with open('external_urls.txt', 'w') as file:
            for url in self.external_urls:
                file.write(url + '\\n')

if __name__ == "__main__":
    urls = ['https://example.com']
    crawler = Crawler()
    asyncio.run(crawler.run(urls))