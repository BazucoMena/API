from flaskr import create_app
from .modelos import db, Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
#Prueba
with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete='Joes')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())
    a = Album(titulo='prueba2', an=2001, descripcion='ninguna', medio='audio')
    db.session.add(a)
    db.session.commit()
    print(Album.query.all())