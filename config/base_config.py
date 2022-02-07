from flask import Flask


class Base:
  FLASK_APP = 'main.py'
  SQLACHEMY_TRACK_MODIFICATION = False