#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
from os import getenv


class DBStorage:
    from sqlalchemy.orm import sessionmaker, scoped_session
    from models.user import User
    from models.state import State
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.amenity import Amenity
    """This class is the storage engine for AirBnB"""

    __engine = None
    __session = None

    def __init__(self):
        """database engine"""
        from sqlalchemy import create_engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls:
            for obj in self.__session:
                if type(obj).__name__ == cls:
                    new_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for obj in self.__session:
                new_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import Base
        self.__session = self.scoped_session(self.sessionmaker(bind=self.__engine))
        self.__session.configure(bind=self.__engine, expire_on_commit=False)
        self.__session = self.scoped_session(self.sessionmaker(bind=self.__engine))
        Base.metadata.create_all(self.__engine)

    def close(self):
        from models import storage
        self.__session.remove()
        self.__session.close()
        self.__engine.dispose()
        self.__session = None
        self.__engine = None
        storage.close()   
