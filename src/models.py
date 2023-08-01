from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    facturas = db.relationship('Facturas', backref='parent',lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "facturas": list(map(lambda factura: factura.serialize(), self.facturas))
            # do not serialize the password, its a security breach
        }
    

class Facturas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platos = db.Column(db.String(120), unique=False, nullable=False)
    mesa = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    

    def __repr__(self):
        return '<Facturas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "platos": self.platos,
            "mesa": self.mesa,
            # do not serialize the password, its a security breach
        }

