from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    phones = relationship("PhoneNumber", back_populates="contact")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class PhoneNumber(Base):
    __tablename__ = 'phonenumbers'
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False, unique=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    contact = relationship("Contact", back_populates='phones')

    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return self.phone
