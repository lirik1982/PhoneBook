from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///./phones.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()


# class SessionManager(object):
#     def __init__(self):
#         self.session = Session()
#         Base.metadata.create_all(engine)

#     def create_contact(self, name):
#         new_contact = Contact(name=name)
#         self.session.add(new_contact)
#         self.session.commit()
#         print('added-', name)
