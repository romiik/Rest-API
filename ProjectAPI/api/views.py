from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Trainer, Pokemon
from .serializers import TrainerSerializer, PokemonSerializer

# Create your views here.


def train_list(request):

    if request.method == 'GET':
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrainerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
         return JsonResponse(serializer.errors, status=400)
