from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.config import settings

# Connect to Supabase PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping = True
)

# Session factory — one session per API request
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

# All table models inherit from this
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
===========================
DATABASE SETUP SUMMARY
===========================

1️⃣ Engine
------------
engine = create_engine(...)

Purpose:
- Creates connection manager to PostgreSQL (Supabase).
- Handles connection pooling automatically.
- All DB operations go through this engine.

Important attributes:
- DATABASE_URL → connection string for DB
- pool_pre_ping=True → checks if DB connection is alive before using it
  (prevents errors when cloud DB drops idle connections)


2️⃣ SessionLocal (Session Factory)
-----------------------------------
SessionLocal = sessionmaker(...)

Purpose:
- Creates database sessions.
- Each API request gets its own session.
- Used for CRUD operations (create, read, update, delete).

Important attributes:
- autocommit=False → changes are saved only when db.commit() is called.
- autoflush=False → prevents automatic syncing before queries.
- bind=engine → connects session to DB engine.


3️⃣ Base (ORM Base Class)
---------------------------
Base = declarative_base()

Purpose:
- Parent class for all ORM models.
- Any class inheriting from Base becomes a database table.

Example:
class Implementation(Base):
    ...


4️⃣ get_db() Dependency
-------------------------
Purpose:
- Creates a DB session for each FastAPI request.
- Ensures session is closed safely after request finishes.

Flow:
Request starts → open session
API uses DB   → perform queries
Request ends  → close session automatically


🧠 Mental Model:
Engine  → Manages DB connections
Session → Talks to DB using Engine
Model   → Defines table structure
get_db  → Gives safe session per request

"""