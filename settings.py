from dotenv import load_dotenv

import os

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_ACCESS")
SQLALCHEMY_DATABASE_ARGS = {"check_same_thread": False}