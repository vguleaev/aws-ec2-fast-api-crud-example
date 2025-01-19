from sqlmodel import SQLModel, create_engine
from app.config.config import Settings

settings = Settings()

engine = create_engine(settings.database_uri)

SQLModel.metadata.create_all(engine)
