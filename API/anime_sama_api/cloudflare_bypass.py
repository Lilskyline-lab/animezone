"""
Wrapper pour cloudscraper avec une interface async compatible avec httpx
"""
import cloudscraper
import asyncio
from typing import Optional
from dataclasses import dataclass


@dataclass
class Response:
    """Response object compatible with httpx.Response"""
    text: str
    status_code: int
    url: str
    
    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300
    
    def raise_for_status(self):
        if not self.is_success:
            raise Exception(f"HTTP {self.status_code}: {self.url}")
        return self


class AsyncCloudScraperClient:
    """
    Client HTTP async qui utilise cloudscraper pour contourner Cloudflare.
    Interface compatible avec httpx.AsyncClient
    """
    
    def __init__(self):
        self.scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            }
        )
    
    async def get(self, url: str, **kwargs) -> Response:
        """Effectue une requête GET async en utilisant cloudscraper"""
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: self.scraper.get(url, **kwargs)
        )
        return Response(
            text=response.text,
            status_code=response.status_code,
            url=str(response.url)
        )
    
    async def post(self, url: str, **kwargs) -> Response:
        """Effectue une requête POST async en utilisant cloudscraper"""
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: self.scraper.post(url, **kwargs)
        )
        return Response(
            text=response.text,
            status_code=response.status_code,
            url=str(response.url)
        )
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
