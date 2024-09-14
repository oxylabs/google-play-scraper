"""
    Module for scraping Google Play.
"""

import logging
import time

from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from google_play_scraper.conf import GooglePlayCategory, google_play_scraper_settings
from google_play_scraper.models import PlayItem
from google_play_scraper.parser import GooglePlayParser


logging.getLogger("WDM").setLevel(logging.ERROR)


class ConsentFormAcceptError(BaseException):
    message = "Unable to accept Google consent form."


class DriverInitializationError(BaseException):
    message = "Unable to initialize Chrome webdriver for scraping."


class DriverGetPlayDataError(BaseException):
    message = "Unable to get Google Play data with Chrome webdriver."


class GooglePlayScraper:
    """Class for scraping Google Play"""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._consent_button_xpath = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span"
        self._parser = GooglePlayParser()

    def _init_chrome_driver(self) -> webdriver.Chrome:
        """Initializes Chrome webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def _click_consent_button(
        self, driver: webdriver.Chrome, query: str, category: GooglePlayCategory
    ) -> None:
        """Clicks google consent form with selenium Chrome webdriver"""
        self._logger.info("Accepting consent form..")
        url = google_play_scraper_settings.get_play_url(query, category)
        try:
            driver.get(url)
            consent_button = driver.find_element(
                By.XPATH,
                self._consent_button_xpath,
            )
            consent_button.click()
        except NoSuchElementException:
            self._logger.warning("Consent form button not found.")
        except Exception as e:
            raise ConsentFormAcceptError from e

        time.sleep(2)

    def get_play_data(self, query: str, category: GooglePlayCategory) -> List[PlayItem]:
        """
        Retrieves a list of items in Google Play for a query in a category.

        Returns:
            List[PlayItem]: A list of PlayItem objects.
        Raises:
            ConsentFormAcceptError: If the Google consent form cannot be accepted.
            DriverInitializationError: If the Chrome webdriver cannot be initialized.
            DriverGetPlayDataError: If the Play data cannot be scraped from the Google Play site.
        """
        self._logger.info(
            f"Retrieving {category.lower()} from Google Play for query {query}.."
        )
        try:
            driver = self._init_chrome_driver()
        except Exception as e:
            raise DriverInitializationError from e

        try:
            self._click_consent_button(driver, query, category)
        except Exception as e:
            driver.close()
            raise e

        self._logger.info("Scraping Google Play page..")
        try:
            return self._parser.parse_by_category(driver, category)
        except Exception as e:
            raise DriverGetPlayDataError from e
        finally:
            driver.close()
