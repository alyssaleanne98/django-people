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

  def post (self, request):
  #Post request
    print(request.data)
    #formt data for postgres
    people = PeopleSerializer(data=request.data)
    if people.is_valid():
        people.save()
        return Response(people.data, status=status.HTTP_201_CREATED)
    else:
        return Response(people.errors, status=status.HTTP_400_BAD_REQUEST)



class PersonDetail(APIView):
    pass 
