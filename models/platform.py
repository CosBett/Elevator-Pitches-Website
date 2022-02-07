from app import db
 
class Platform(db.model):
    __tablename__ = 'Platform'

    pitch = db.column(db.string(), nullable =False)
    downvote = db.column(db.integer, nullable =False)
    upvote = db.column(db.integer, nullable =False)
