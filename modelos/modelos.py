from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)
    class Album(db.Model):
        id = db.column(db.Integer,fore)
        titulo = db.column(db.String(128))
        an = db.column(db.Integer)
        descripcion = db.column(db.String(128))
        medio= db.column(db.String(128))

    def __rep__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.an, self.descripcion,self.medio)