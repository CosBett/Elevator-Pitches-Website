import email

from click import password_option
from app import db

class User (db.model):
  __tablename__ = 'Users'

  id = db.column(db.integer, primary_key=True, autoincrement=True)
  first_name = db.column(db.string(), nullable =False)
  second_name = db.column(db.string(), nullable =False)
  email = db.column(db.string(), nullable =False)
  username = db.column(db.string(), nullable =False, unique =True)
  password = db.column(db.string(), nullable =False)