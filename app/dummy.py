import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import *

engine = create_engine('sqlite:///test.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User(username = "admin",password = "password")
session.add(user)

user = User(username ="Oscar",password ="Zoulette")
session.add(user)

# commit the record the database
session.commit()
session.commit()