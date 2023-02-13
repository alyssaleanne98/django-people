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
    #Get all persons from the table
    person = People.objects.all()
    # Use serializer to format table data to JSON
    data = PeopleSerializer(person, many=True).data
    return Response(data)

  def post (self, request):
  #Post request
    print(request.data)
    #format data for postgres
    people = PeopleSerializer(data=request.data)
    #we need to serialize the data that is coming in from the user "passing in the request.data we receive from user"
    if people.is_valid():
        #we need an if statement to see if data is in valid format before sending it to sql database. If so, we want to save it
        people.save()
        return Response(people.data, status=status.HTTP_201_CREATED)
        #If it works, we want to send a 201 status code
    else:
        return Response(people.errors, status=status.HTTP_400_BAD_REQUEST)
        #If there are any errors, return 400 status code

#After you create get route, go to local host - you get a pre-formatted page with your response data when you hit it in the browser. 

class PersonDetail(APIView):

  def get(self, request, pk):
    #Show Request
    print(request)
    people = get_object_or_404(People, pk=pk)
    #Gets the object or sends 404 status code
    #In mode, we are sending in primary key = primary key
    #Don't forget to import this at the top 
    data = PeopleSerializer(people).data
    #Formats data
    return Response(data)
    #Sends back data

  def put(self, request, pk):
    #update request
    print (request)
    people = get_object_or_404(People, pk=pk)
    updated = PeopleSerializer(people, data=request.data, partial=True) #What does partial true mean?
    if updated.is_valid():
        updated.save()
        #if updated is valid then we want to save 
        return Response(updated.data)
    else:
        return Response(updated.errors, status=status.TTP_400_Bad_Request)
        #if there are any errors, return 404 status error

  def delete(self, request, pk):
    #Delete request
    print(request)
    people = get_object_or_404(People, pk=pk)
    people.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)