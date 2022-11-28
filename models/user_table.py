# Importing libraries
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db_config import meta

# Initializing
user_table = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("email", String(255)),
    Column("username", String(255)),
    Column("password", String(255)),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
)
