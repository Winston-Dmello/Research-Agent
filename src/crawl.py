import os
import asyncio
from serpapi import GoogleSearch
from dotenv import load_dotenv
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai import CacheMode

load_dotenv()

class SerpCrawlService:
    def __init__(self):
        api_key = os.getenv("SERPAPI_API_KEY")
        if not api_key:
            raise ValueError("Missing SERPAPI_API_KEY environment variable")
        self.api_key = api_key

    def search_companies(self, query: str, num_results: int = 5):
        try:
            params = {
                "engine": "google",
                "q": f"{query} company pricing",
                "api_key": self.api_key,
                "num": num_results
            }
            search = GoogleSearch(params)
            results = search.get_dict()
            return [r["link"] for r in results.get("organic_results", [])]
        except Exception as e:
            print(e)
            return []

    def scrape_company_pages(self, url: str):
        try:
            return asyncio.run(self._scrape_url_async(url))
        except Exception as e:
            print(e)
            return None

    async def _scrape_url_async(self, url: str, headless: bool = True):
        browser_cfg = BrowserConfig(headless=headless)
        run_cfg = CrawlerRunConfig(cache_mode=CacheMode.ENABLED)
        async with AsyncWebCrawler(config=browser_cfg) as crawler:
            result = await crawler.arun(url=url, config=run_cfg)
            return result.markdown
