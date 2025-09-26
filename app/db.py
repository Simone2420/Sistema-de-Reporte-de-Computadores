import sqlmodel

DATABASE_URL = "sqlite:///db.sqlite"
engine = sqlmodel.create_engine(DATABASE_URL)


def create_db_and_tables():
    sqlmodel.SQLModel.metadata.create_all(engine)