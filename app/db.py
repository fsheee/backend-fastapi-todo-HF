


# # # app/db.py
# # from sqlmodel import SQLModel, create_engine, Session
# # import os

# # # Load environment variables (HF Secrets)
# # DB_USER="neondb_owner"
# # DB_PASSWORD="npg_jCi7XldZ9Dnf"
# # DB_HOST="ep-falling-frost-a40mkwy9-pooler.us-east-1.aws.neon.tech"
# # DB_NAME="neondb"
# # DB_SSL="require"


# # # Build the connection string using psycopg
# # DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# # # Create engine
# # engine = create_engine(DATABASE_URL, echo=True)

# # # Function to create tables
# # def create_db_and_tables():
# #     SQLModel.metadata.create_all(engine)

# # # Session generator
# # def get_session():
# #     with Session(engine) as session:
# #         yield session

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
