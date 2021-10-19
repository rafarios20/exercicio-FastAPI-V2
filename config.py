from tomatic import Tomatic
from tomatic.buckets import EnvironBucket

t = Tomatic(EnvironBucket, static_profile="FASTAPI", raise_if_none=ValueError)

SQLALCHEMY_DATABASE_URL = "sqlite:///db.sqlite3"

SQLALCHEMY_DATABASE_ARGS = {"check_same_thread": False}
