from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Home(APIView):
    items = ['hola mundo']

    def get(self, request):
        return Response(self.items)

    def post(self, request):
        data = request.data
        if 'name' in data:
            new_item = {'name': data['name']}
            self.items.append(new_item)
            return Response(new_item, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Missing "name" field in the request data'}, status=status.HTTP_400_BAD_REQUEST)
