#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity
from models.base_model import Base


place_amenity = Table('place_amenity', Base.metadata,
                      Column('Place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('Amenity_id', String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False),
                            )



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review', cascade='all, delete', backref='place'
        )
        amenities = relationship(
            'Amenity', viewonly=False, secondary=place_amenity,
        )
    else:
        @property
        def reviews(self):
            """Getter attribute in case"""
            from models import storage
            from models.review import Review
            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
        
        @property
        def amenities(self):
            """Getter attribute in case"""
            from models import storage
            from models.amenity import Amenity
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in storage.all(Place).values():
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj=None):
            """Setter attribute in case"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
