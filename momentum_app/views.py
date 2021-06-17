from django.shortcuts import render
from django.shortcuts import render
from django.http import request, JsonResponse, Http404
from .models import SP500, DJ30, Divs, Etf, Notes
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import DJ30Serializer, EtfSerializer, DivsSerializer, NotesSerializer, SP500Serializer

class ListSP500(APIView):

    def get(self, request):
        obj = SP500.objects.all().order_by('-avg_momentum')
        serializer_obj = SP500Serializer(obj, many=True)
        return Response(serializer_obj.data)


class ListDJ30(APIView):

    def get(self, request):
        obj = DJ30.objects.all().order_by('-avg_momentum')
        serializer_obj = DJ30Serializer(obj, many=True)
        return Response(serializer_obj.data)

class ListEtf(APIView):

    def get(self, request):
        obj = Etf.objects.all().order_by('-momentum_12_1')
        serializer_obj = EtfSerializer(obj, many=True)
        return Response(serializer_obj.data)


class ListDivs(APIView):

    def get(self, request):
        obj = Divs.objects.all().order_by('-div_p')
        serializer_obj = DivsSerializer(obj, many=True)
        return Response(serializer_obj.data)


class ListNotes(APIView):

    def get(self, request):
        obj = Notes.objects.all().order_by('id')
        serializer_obj = NotesSerializer(obj, many=True)
        return Response(serializer_obj.data)

    def post(self, request):
        data = request.data
        serializer_obj = NotesSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)
