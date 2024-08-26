from sqlalchemy import MetaData, Table, Column, String, Integer, URL, ARRAY, JSON
from sqlalchemy.dialects.postgresql import JSONB

metadata = MetaData()

tutors = Table(
    "tutor",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("avatar", String, nullable=True),
    Column("subjects", ARRAY(String), nullable=False),
    Column("prices", JSONB, nullable=False),
    Column("contact", String, nullable=False)
)
