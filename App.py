from flaskr import create_app
from .modelos import db, Usuario, Album, Medio, Cancion
from .modelos import AlbumSchema
from flask_restful import Api
from .vistas import VistaCancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones,'/canciones')
api.add_resource(VistaCancion,'/canciones/<int:id_cancion>')

with app.app_context():
    Album_Schema = AlbumSchema()
    #u = Usuario(nombre_usuario='jhoan', contrasena=123455)
    a = Album(titulo='prueba2', an=2001, descripcion='texto', medio=Medio.CD)
    db.session.add(a)
    db.session.commit()
    print([Album_Schema.dump(album) for album in Album.query.all()])
    #c = Cancion(titulo='Un sueño', minutos=1, segundos=15, interprete='yotas')
    #u.albumes.append(a)
    #a.canciones.append(c)
    #db.session.add(u)
    #db.session.add(c)
    #db.session.commit()
    #print(Album.query.all())
    #print(Album.query.all()[0].canciones)
    #print(Cancion.query.all())
    #db.session.delete(a)
    #print(Album.query.all())
    #print(Cancion.query.all())
