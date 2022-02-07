import secrets

class Base:
  FLASK_APP = 'main.py'
  SQLACHEMY_TRACK_MODIFICATION = False
  SECRET_KEY = secrets.token_hex(16)

class Development(Base):
  FLASK_ENV = 'development'
  DATABASE = ''
  POSTGRES_USER = ''
  POSTGRES_PASSWORD = ''
  SQLALCHEMY_DATABASE_URL = 'sqlite://tmp/elevatorPitch.db'

class Staging(Base):
  DATABASE = ''
  POSTGRES_USER = ''
  POSTGRES_PASSWORD = ''
  SQLALCHEMY_DATABASE_URL = 'sqlite://tmp/elevatorPitch.db'

class Production(Base):
  DATABASE = ''
  POSTGRES_USER = ''
  POSTGRES_PASSWORD = ''
  SQLALCHEMY_DATABASE_URL = 'sqlite://tmp/elevatorPitch.db'
