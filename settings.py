from dotenv import load_dotenv

import os

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("ADYEN_URL_TERMINAL")
SQLALCHEMY_DATABASE_ARGS = {"check_same_thread": False}