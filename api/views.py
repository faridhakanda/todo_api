from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoModelSerializer
from .models import TodoModel
from django.http import Http404

# Create your views here.

# testing api_view with learning
# serializer in restframework doc
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        todo_model = TodoModel.objects.all()
        serializer = TodoModelSerializer(todo_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        #todo_model = TodoModel.objects.all()
        serializer = TodoModelSerializer(data = request.data)
        #serializer1 = TodoModelSerializer1(data=request.data)
        if serializer.is_valid(): # and serializer1.is_valid():
            serializer.save()
            #serializer1.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



# testing class based views
# by restframework official docs
class TodoModelView(APIView):
    """"
        Retrive, update or delete a todo instance
    """
    def get_object(self, pk):
        try:
            return TodoModel.objects.get(pk=pk)
        except TodoModel.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        todo_model = TodoModel.objects.all()
        serializer = TodoModelSerializer(todo_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = TodoModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        todo_model = self.get_object(pk)
        serializer = TodoModelSerializer(todo_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, formate=None):
        todo_model = self.get_object(pk)
        todo_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)