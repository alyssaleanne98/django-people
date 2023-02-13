from rest_framework.views import APIView    # <- as super to your class
from rest_framework.response import Response  # <- to send data to the frontend
from rest_framework import status # <- to include status codes in your response
from django.shortcuts import render 

from .serializer import PeopleSerializer # <- to format data to and from the database, enforces schema
from .models import People
from django.shortcuts import get_object_or_404

# class (People)

#  GET     /people - index
#  POST    /people - create

# class  (PeopleDetail) - use primary key (pk) as argument to access id

#  GET     /people/:id - show
#  PUT     /people/:id - update
#  DELETE  /people/:id - delete


#Creat views here
class Person(APIView): # person is the class name 

  def get(self, request):
    # Index Request
    print(request)
   
    person = People.objects.all()
    # Use serializer to format table data to JSON
    data = PeopleSerializer(person, many=True).data
    return Response(data)


class PersonDetail(APIView):
    pass 
