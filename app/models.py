# Este File define los modelos para las tablas taxis y trajectories de SQLAlchemy
from app import db

class Taxi(db.Model):
    __tablename__ = 'taxis'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    plate = db.Column(db.String(10), nullable=False)

class Trajectory(db.Model):
    __tablename__ = 'trajectories'

    id = db.Column(db.Integer, primary_key=True, nullable=False, default=db.func.nextval('trajectories_id_seq'))
    taxi_id = db.Column(db.Integer, db.ForeignKey('taxis.id'), nullable=False)
    date = db.Column(db.TIMESTAMP, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

     # Define la relación con la tabla 'taxis'
    taxi = db.relationship('Taxi', backref=db.backref('trajectories', lazy=True)) 