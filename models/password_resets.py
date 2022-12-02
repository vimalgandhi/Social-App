from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, String
from config.db_config import meta

password_resets_table = Table(
    "password_resets",
    meta,
    Column("email",  String(255), nullable=False),
    Column("token", String(255), nullable=False),
    Column("created_at", DateTime),
)
