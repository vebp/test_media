from django.shortcuts import render

# Create your views here.
import random
import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Grabacion

def nuevo_nombre(extension):
		aleatorio=str(random.randint(0,10000000))
		hoydia=datetime.datetime.now()
		ano=hoydia.year
		mes=hoydia.month
		dia=hoydia.day
		hora=hoydia.hour
		minuto=hoydia.minute
		segundo=hoydia.second

		nombre_archivo="audio_{}{}{}{}{}{}_{}.{}".format( ano,mes,dia,hora,minuto,segundo,aleatorio,extension)

		return nombre_archivo


def datos_archivo(nombre_original):
	permitido=True

	lista_tmp=nombre_original.split('.')
	extension=lista_tmp[len(lista_tmp)-1]
	if extension not in ['mp3','webm']:

		permitido=False

	return {'permitido':permitido, 'extension':extension}

def index(request):
    return render(request, "app1/index.html")

@csrf_exempt
def guardaraudio(request):

	if request.method !="POST":
		return JsonResponse({"error":"POST request required"}, status=400)

	print(request.FILES['archivo'].name)
	print(request.FILES['archivo'].size)

	if not request.FILES['archivo']:
		return JsonResponse({'error':"No hay archivo"}, status=400)
	revision=datos_archivo(request.FILES['archivo'].name)
	print('revision')
	print(revision)
	if revision['permitido']:
		request.FILES['archivo'].name=nuevo_nombre(revision['extension'])
		print('revision')
		print(request.FILES['archivo'].name)


		try:

			grabacion=Grabacion()
			grabacion.nombre=request.FILES['archivo'].name
			grabacion.archivo=request.FILES['archivo']
			grabacion.save()

			return JsonResponse({"success":True}, status=200)



		except Exception as e:
			print(e)

		return JsonResponse({"success":False, "error":"error al final"}, status=400)
