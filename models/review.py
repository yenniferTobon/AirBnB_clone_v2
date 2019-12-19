#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = ""
    place_id = ""
    user_id = ""
