from sqlmodel import Session, create_engine
from .config import settings

engine = create_engine(str(settings.DATABASE_SERVER))

def init_db(session: Session) -> None:
    # Tables should be created with Alembic Migrations

    pass