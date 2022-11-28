# Importing libraries
import logging
from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine
import os

# Initialization
meta = MetaData()


# Creating engine
auth = f"{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
db = create_engine(
    f"mysql+pymysql://{auth}@{os.getenv('DATABASE_URL')}/{os.getenv('DATABASE_NAME')}",
    pool_recycle=3600,
)

# dev url
# db = create_engine("mysql+pymysql://root:3k2HlQOQV6z8nTEaCcRM@containers-us-west-104.railway.app:5950/railway",pool_recycle=5950,)
# 
# Connecting db
try:
    db.connect()
    logging.info("Database connected successfully.")
except Exception as e: 
    logging.error(e)