from flask import Flask
from database import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from flask_bootstrap import Bootstrap
#import sqlite3

app = Flask(__name__)
app.config.from_object(Config)
#engine = create_engine('sqlite:///test.db', echo=True)
bootstrap = Bootstrap(app)
# create a Session
#Session = sessionmaker(bind=engine)
#session = Session()

from app import routes

if __name__ == '__main__':
        import os  
        app.run(host='0.0.0.0')
# venv\Scripts\activate
# set FLASK_APP=Muscu_site.py

# Linux : source activate (in venv/bin)
