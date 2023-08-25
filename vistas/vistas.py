from flask_restful import Resource
from ..modelos import db, Cancion, CancionShema
from flask import request

cancion_shema = CancionShema()

class VistaCancion(Resource):
    def get(self): #trae todas las caciones
        return [cancion_shema.dump(Cancion) for Cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],
                                minutos=request.json['minutos'],
                                segundos=request.json['segundos'],
                                interprete=request.json['interprete'])
        db.session.add(nueva_cancion)#agg en la bd
        db.session.commit()#guarda los cambios
        return cancion_shema.dump(nueva_cancion)#retorna la nueva cancion en formato json


class VistacCancion(Resource):
    def get(self, id_cancion):
        return cancion_shema.dump(Cancion.query.get_or_404(id_cancion))

    def put(self, id_cancion):
        cancion= Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get('titulo', cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete',cancion.interprete)
        db.session.commit()
        return cancion_shema.dump(cancion)

    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return 'Operacion ecitosa', 204
