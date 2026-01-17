import asyncio
from crawl4ai import AsyncWebCrawler

async def scrape_article(url: str):
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url)
        return result.markdown