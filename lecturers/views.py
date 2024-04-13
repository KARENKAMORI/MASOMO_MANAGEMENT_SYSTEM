from django.http import JsonResponse
from .models import Lecturer
from .serializers import LecturerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def lecturer_list(request, format=None):
    if request.method == 'GET':
        # get all the lecturers
        lecturers = Lecturer.objects.all()
        # swrialize them
        serializer = LecturerSerializer(lecturers, many=True)
        #return json
        return JsonResponse({"lecturers": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = LecturerSerializer(data=request.data)
        # check if data sent is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])       
def lecturer_details(request, id, format=None):
    # check if it's a valid request
    try:
        lecturer = Lecturer.objects.get(pk=id)
    except Lecturer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LecturerSerializer(lecturer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LecturerSerializer(lecturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lecturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
