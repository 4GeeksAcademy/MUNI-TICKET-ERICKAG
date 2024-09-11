from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    event = db.relationship("Event", backref="administrator", lazy=True)

    def __repr__(self):
        return f"<Admin Name {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    district = db.Column(db.String(20), unique=False, nullable=True)
    phone = db.Column(db.String(12), unique=False, nullable=True)
    date_of_birth = db.Column(db.DateTime, nullable=True)
    purchase = db.relationship("Purchase", backref="user", lazy=True)
    favourite = db.relationship("Favourite", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.email}>"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    place = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    category = db.Column(db.String(250), nullable=False)
    stock = db.Column(db.Integer,nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey("administrator.id"))
    purchase = db.relationship("Purchase", backref="event", lazy=True)
    ticket = db.relationship("Ticket", backref="event", lazy=True)
    favourite = db.relationship("Favourite", backref="event", lazy=True)

    def __repr__(self):
        return f"<Event {self.name}>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))

    def __repr__(self):
        return f"<Ticket ID {self.id}>"

    def serialize(self):
        return {
            "id": self.id,
            "price": self.price,
        }


class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))