#!/usr/bin/python3
"""Module contains Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a Place."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    num_rooms = 0
    num_bathrooms = 0
    max_guest = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
