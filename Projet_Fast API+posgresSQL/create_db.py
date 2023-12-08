from database import Base, engine, SessionLocal
from models import EtablissementInfo
import pandas as pd
from sqlalchemy import String, Boolean, Column, Text, Date

print("Creating database tables...")

Base.metadata.create_all(engine)

