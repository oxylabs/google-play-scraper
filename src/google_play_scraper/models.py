"""
    Pydantic models for Google Play scraper.
"""

from pydantic import BaseModel


class App(BaseModel):
    title: str
    author: str
    rating: str | None
    icon_url: str
    url: str


class Movie(BaseModel):
    title: str
    url: str
    rating: str | None
    price: str | None
    cover_url: str


class Book(BaseModel):
    title: str
    url: str
    rating: str | None
    price: str | None
    cover_url: str


class PlayItem(BaseModel):
    payload: App | Movie | Book
