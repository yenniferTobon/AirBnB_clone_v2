#!/usr/bin/python3
"""engine must be linked to the MySQL database"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import os


class DBStorage():
    """class to database session"""

    __engine = None
    __session = None

    def __init__(self):
        """constructor class """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all objects of type class"""

        c_dict = {}
        if cls is None:
            all_cls = ['State', 'City', 'User', 'Place', 'Review']
            for classes in all_cls:
                for obj in self.__session.query(eval(classes)).all():
                    c_dict[type(obj).__name__+"."+obj.id] = obj
        else:
            for obj in self.__session.query(eval(cls)).all():
                c_dict[type(obj).__name__+"."+obj.id] = obj
        return c_dict

    def new(self, obj):
        """add the object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""

        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """Close this Session,
           This clears all items and ends any
           transaction in progress
        """
        self.__session.close()
