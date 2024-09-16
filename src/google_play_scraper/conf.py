"""
    Config module for google_play_scraper.
"""

from enum import Enum
from urllib.parse import quote

from pydantic_settings import BaseSettings


class GooglePlayCategory(str, Enum):
    """Enum for Google Play categories"""

    APPS = "apps"
    BOOKS = "books"
    MOVIES = "movies"


class GooglePlayScraperSettings(BaseSettings):
    """Settings class for Google Play Scraper"""

    url: str = "https://play.google.com/store/search"

    def get_play_url(self, query: str, category: GooglePlayCategory) -> str:
        """Returns a Google Play URL for a given query string."""
        encoded_query = quote(query)
        encoded_category = quote(category.value)
        return f"{self.url}?q={encoded_query}&c={encoded_category}&hl=en_GB&gl=UK"


google_play_scraper_settings = GooglePlayScraperSettings()
