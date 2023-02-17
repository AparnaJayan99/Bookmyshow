from django.shortcuts import render
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import bookSerializer
from django.core.files import File
from django.http import HttpResponse, request, HttpResponseRedirect, response

class home(APIView):
    def pp(request):
        return HttpResponse("Hello, Django!")

class tickets(APIView):   
    def get(self, request):
        print("#############################################")
        # if request.method == 'GET':
        userData = Book.objects.all().values()
        # ticketbooking = Book.objects.all().values()
        # content data into file by opening and writing data into file
        f = open(r"C:\Users\aparna\myproject\firstapp\bookmyshow\trial.txt", "w")
        testfile = File(f)
        serializeData = bookSerializer(userData, many=True).data
        testfile.writelines(str(serializeData))
        print("Successfull on adding content into file")
        testfile.close
        f.close
        return HttpResponse(serializeData, request) 
        
class CreateUser(APIView):
    def post(self, request):        
        userSerializer = bookSerializer(data=request.data)
        if userSerializer.is_valid():
            userSerializer.save()
            response = "success"
        else:
            response = userSerializer.errors
        return Response(response)
