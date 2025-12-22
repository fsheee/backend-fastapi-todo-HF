# import os
# from sqlmodel import SQLModel, create_engine, Session
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# if not DATABASE_URL:
#     # fallback to SQLite for local dev
#     DATABASE_URL = "sqlite:///./todo.db"
#     engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
# else:
#     engine = create_engine(DATABASE_URL, echo=True)

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# def get_session():
#     with Session(engine) as session:
#         yield session
