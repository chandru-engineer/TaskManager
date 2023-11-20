import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG')
PORT=os.getenv('PORT')
HOST=os.getenv('HOST')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
SECRET_KEY = os.getenv('SECRET_KEY')
BROKER_URL = os.getenv('BROKER_URL')
RESULT_BACKEND = os.getenv('RESULT_BACKEND')