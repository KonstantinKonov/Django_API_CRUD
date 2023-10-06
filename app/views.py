import traceback

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import Person
from .serializers import PersonSerializer

# Create your views here.


class PersonCreateListAPIView(APIView):
    # read
    def get(self, request):
        queryset = Person.objects.all()
        name_filter = request.query_params.get('name')
        if name_filter:
            queryset = queryset.filter(name__icontains=name_filter)
        data = PersonSerializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)

    # create
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonUpdateDeleteReadAPIView(APIView):
    def get(self, request, pk):
        person = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    # full update
    def put(self, request, pk):
        person = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        person = get_object_or_404(Person, id=pk)
        person.delete()
        return Response()
