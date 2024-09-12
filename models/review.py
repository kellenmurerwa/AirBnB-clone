#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review class with the following attributes:
        place_id (str): the place id
        user_id (str): the user id
        text (str): the text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
