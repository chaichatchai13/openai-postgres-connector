# models.py
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class OpenAIResult(Base):
    __tablename__ = 'open_ai_result'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
