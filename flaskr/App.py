from flaskr import create_app
from .modelos import db, Usuario, Album, Medio, Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()


with app.app_context():
    u = Usuario(nombre_usuario='jhoan', contrasena=123455)
    a = Album(titulo='prueba2', an=2001, descripcion='ninguna', medio='CD')
    c = Cancion(titulo='Un sueño', minutos=1, segundos=15, interprete='yotas')
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].albumes)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())
