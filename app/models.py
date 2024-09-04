from app import db

class Taxi(db.Model):  
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True) 
    plate = db.Column(db.String(10))


class Trajectory(db.Model):
    __tablename__ = 'trajectories'
    
    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, db.ForeignKey('taxis.id'))
    date = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
