"""
    Main module for google_play_scraper.
"""

import logging

import click

from google_play_scraper.collector import GooglePlayDataCollector
from google_play_scraper.conf import GooglePlayCategory


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    "--query",
    help="The query for which to return Google Play results for.",
    required=True,
)
@click.option(
    "--category",
    help="The category in which to search Google Play results for. Default: Apps",
    required=False,
    default="apps",
)
def scrape_google_play(query: str, category: str) -> None:
    try:
        category = GooglePlayCategory(category)
    except ValueError:
        categories = ", ".join(GooglePlayCategory.__members__.values())
        logging.error(f"Invalid category {category}. Must be one of: {categories}")
        return

    collector = GooglePlayDataCollector()
    collector.save_play_data(query, category)


if __name__ == "__main__":
    scrape_google_play()
