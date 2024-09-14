import logging

from typing import Callable, Dict, List

from pydantic import ValidationError
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from google_play_scraper.conf import GooglePlayCategory
from google_play_scraper.models import App, Book, Movie, PlayItem


class GooglePlayParser:
    """Class for parsing Google Play data"""

    def __init__(
        self,
        logger: logging.Logger | None = None,
    ) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._parse_functions: Dict[GooglePlayCategory, Callable] = {
            GooglePlayCategory.APPS: self._parse_app_item,
            GooglePlayCategory.BOOKS: self._parse_book_item,
            GooglePlayCategory.MOVIES: self._parse_movie_item,
        }

    def parse_by_category(
        self,
        div: webdriver.Chrome,
        category: GooglePlayCategory,
    ) -> List[PlayItem]:
        """Parses Google Play data by category"""
        if category not in self._parse_functions:
            raise NotImplementedError(
                f"Parsing of category {category.value} is not implemented."
            )

        return self._parse_items(div, category)

    def _parse_items(
        self, div: webdriver.Chrome, category: GooglePlayCategory
    ) -> List[PlayItem]:
        """Parses apps from Google Play"""
        items = div.find_elements(By.CLASS_NAME, "Si6A0c")
        item_data = []

        parse_function: Callable = self._parse_functions[category]

        for div in items:
            try:
                item = PlayItem(payload=parse_function(div))
            except ValidationError:
                self._logger.error("Data missing from play item div. Skipping..")
                continue

            item_data.append(item)

        return item_data

    def _parse_app_item(self, div: webdriver.Chrome) -> App:
        """Parses app item from Google Play"""
        title = (
            div.find_element(By.CLASS_NAME, "ubGTjb")
            .find_element(By.CLASS_NAME, "DdYX5")
            .text
        )
        author = div.find_element(By.CLASS_NAME, "wMUdtb").text
        try:
            rating = div.find_element(By.CLASS_NAME, "w2kbF").text
        except NoSuchElementException:
            rating = None
        url = div.get_attribute("href")
        icon_url = div.find_element(By.CLASS_NAME, "T75of").get_attribute("src")

        return App(
            title=title,
            url=url,
            author=author,
            rating=rating,
            icon_url=icon_url,
        )

    def _parse_book_item(self, div: webdriver.Chrome) -> Book:
        """Parses book item from Google Play"""
        title = div.find_element(By.CLASS_NAME, "Epkrse").text
        url = div.get_attribute("href")
        try:
            rating = div.find_element(By.CLASS_NAME, "LrNMN").text
        except NoSuchElementException:
            rating = None

        try:
            price = div.find_element(By.CLASS_NAME, "VfPpfd").text
        except NoSuchElementException:
            price = None

        cover_url = div.find_element(By.CLASS_NAME, "T75of").get_attribute("src")
        return Book(
            title=title, url=url, rating=rating, price=price, cover_url=cover_url
        )

    def _parse_movie_item(self, div: webdriver.Chrome) -> Movie:
        """Parses movie item from Google Play"""
        title = div.find_element(By.CLASS_NAME, "Epkrse").text
        url = div.get_attribute("href")
        try:
            rating = div.find_element(By.CLASS_NAME, "LrNMN").text
        except NoSuchElementException:
            rating = None

        try:
            price = div.find_element(By.CLASS_NAME, "VfPpfd").text
        except NoSuchElementException:
            price = None

        cover_url = div.find_element(By.CLASS_NAME, "T75of").get_attribute("src")
        return Movie(
            title=title, url=url, rating=rating, price=price, cover_url=cover_url
        )
