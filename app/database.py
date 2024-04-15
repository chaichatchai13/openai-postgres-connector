from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from dotenv import load_dotenv

from app.models import OpenAIResult
from app.schemas import OpenAIResultResponse

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    # Create tables if they don't exist
    try:
        OpenAIResult.__table__.create(engine, checkfirst=True)
    except ProgrammingError as e:
        print(f"An error occurred: {e}")

create_tables()

def init_db():
    """Create database tables if they don't exist."""
    Base.metadata.create_all(bind=engine)

def create_openai_result(prompt: str, response: str) -> OpenAIResultResponse:
    """Save a new OpenAIResult entry to the database."""
    db_session = SessionLocal()
    try:
        new_result = OpenAIResult(prompt=prompt, response=response)
        db_session.add(new_result)
        db_session.commit()
        print(f"Inserted openai result Id : {new_result.id}")
        return new_result
    except Exception as e:
        db_session.rollback()
        raise e
    finally:
        db_session.close()

def get_openai_result_by_prompt_id(prompt_id: int) -> OpenAIResultResponse:
    """Retrieve an OpenAIResult entry by its ID."""
    db_session = SessionLocal()
    try:
        result = db_session.query(OpenAIResult).filter(OpenAIResult.id == prompt_id).first()
        return result
    except Exception as e:
        db_session.rollback()
        raise e
    finally:
        db_session.close()