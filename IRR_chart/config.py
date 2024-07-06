from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
