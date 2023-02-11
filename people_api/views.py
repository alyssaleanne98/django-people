from django.shortcuts import render


from rest_framework.views import APIView    # <- as super to your class
from rest_framework.response import Response  # <- to send data to the frontend
from rest_framework import status # <- to include status codes in your response

from .serializers import PeopleSerializer # <- to format data to and from the database, enforces schema

from .models import People


# class (People)

#  GET     /people - index
#  POST    /people - create

# class  (PeopleDetail) - use primary key (pk) as argument to access id

#  GET     /people/:id - show
#  PUT     /people/:id - update
#  DELETE  /people/:id - delete

class persons(APIView):

   def get(self, request):
    # Index Request
    print(request)
    # Get all books from the book table
    persons = People.objects.all()
    # Use serializer to format table data to JSON
    data = PeopleSerializer(persons, many=True).data
    return Response(data)