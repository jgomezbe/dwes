from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import date
from .models import Tlibros,Tcomentarios
import json
def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola caracola</h1>");

def devolver_libros(request):
	lista = Tlibros.objects.all();
	respuesta_final = []
	for fila_sql in lista:
		diccionario = {}
		diccionario['id'] = fila_sql.id
		diccionario['titulo'] = fila_sql.nombre
		diccionario['fecha'] = fila_sql.anno_publicacion
		diccionario['foto']= fila_sql.url_imagen
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final,safe=False);

def devolver_libros_por_id (request, id_solicitado):
	libro = Tlibros.objects.get (id = id_solicitado)
	comentarios = libro.tcomentarios_set.all()
	lista_comentarios=[]
	for fila_comentario_sql in comentarios:
		diccionario={}
		diccionario['id']=fila_comentario_sql.id
		diccionario['comentario']=fila_comentario_sql.comentario
		diccionario['fecha']=fila_comentario_sql.fecha_comentario
		lista_comentarios.append(diccionario)
	resultado={
 	       'id':libro.id,
	        'nombre':libro.nombre,
	        'fecha':libro.anno_publicacion,
        	'comentarios':lista_comentarios,
		'foto':libro.url_imagen
	}
	return JsonResponse(resultado,json_dumps_params={'ensure_ascii':False})
@csrf_exempt
def guardar_comentario(request,libro_id):
	if request.method!='POST':
		return None

	json_peticion = json.loads(request.body)
	comentario=Tcomentarios()
	comentario.comentario=json_peticion['nuevo_comentario']
	comentario.libro=Tlibros.objects.get(id= libro_id)
	comentario.fecha_comentario=date.today()
	comentario.save()
	return JsonResponse( {"status":"ok"})
