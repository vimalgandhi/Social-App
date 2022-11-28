# Importing libraries
import logging
from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine
import os

# Initialization
meta = MetaData()


# Creating engine
auth = f"{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"

# db = create_engine(
#     f"mysql+pymysql://{auth}@{os.getenv('DATABASE_URL')}/{os.getenv('DATABASE_NAME')}",
#     pool_recycle=3600,
# )


# dev url
db = create_engine(f"mysql+pymysql://root:{os.getenv('DATABASE_PASSWORD_DEV')}@{os.getenv('DATABASE_URL_DEV')}:5950/railway",pool_recycle=5950,) 
# Connecting db
try:
    db.connect()
    logging.info("Database connected successfully.")
except Exception as e: 
    logging.error(e)