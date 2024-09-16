"""
    Main module for collecting Google Play data.
"""

import logging

from typing import List

import pandas as pd

from google_play_scraper.conf import GooglePlayCategory
from google_play_scraper.models import PlayItem
from google_play_scraper.scraper import GooglePlayScraper


DEFAULT_OUTPUT_FILE = "play_items.csv"


class GooglePlayDataCollector:
    """Data collector class for Google Play"""

    def __init__(
        self,
        output_file: str | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._scraper = GooglePlayScraper()
        self._output_file = output_file if output_file else DEFAULT_OUTPUT_FILE
        self._logger = logger if logger else logging.getLogger(__name__)

    def _save_to_csv(self, items: List[PlayItem], category: GooglePlayCategory) -> None:
        """Saves given list of play items to a CSV file."""
        output_file_name = f"{category.value}_{self._output_file}"
        self._logger.info(f"Writing {len(items)} items to {output_file_name}..")
        play_items = [item.payload.model_dump() for item in items]
        df = pd.DataFrame(play_items)
        df.to_csv(output_file_name)

    def save_play_data(self, query: str, category: GooglePlayCategory) -> None:
        """
        Scrapes data from Google Play for a given query string and stores it into a CSV file.

        Args:
            query (str): The query string for which to get Google Play results.
            category (GooglePlayCategory): The category in which to search for Google Play results.
        """
        self._logger.info(
            f"Getting Google Play data for query {query} in category {category.value}.."
        )
        try:
            items = self._scraper.get_play_data(query, category)
        except Exception:
            self._logger.exception(
                f"Error when scraping Google Play for query {query}."
            )
            return

        if not items:
            self._logger.info("No items found for query.")
            return

        self._save_to_csv(items, category)
