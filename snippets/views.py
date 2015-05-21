# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# Create your views here.

# class JSONResponse(HttpResponse):
#     """
#     A HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)


# @api_view(['GET', 'POST'])
# @csrf_exempt
# def snippet_list(request, format=None):
class SnippetList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    # if request.method == 'GET':
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     # return JSONResponse(serializer.data)
    #     return Response(serializer.data)

    # elif request.method == 'POST':
    #     # data = JSONParser().parse(request)
    #     # serializer = SnippetSerializer(data=data)
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     #     return JSONResponse(serializer.data, status=201)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # return JSONResponse(serializer.errors, status=400)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
# def snippet_detail(request, pk, format=None):
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            # return HttpResponse(status=404)
            # return Response(status=status.HTTP_404_NOT_FOUND)
            raise Http404

    # if request.method == 'GET':
    #     serializer = SnippetSerializer(snippet)
    #     # return JSONResponse(serializer.data)
    #     return Response(serializer.data)

    # elif request.method == 'PUT':
    #     # data = JSONParser().parse(request)
    #     # serializer = SnippetSerializer(snippet, data=data)
    #     serializer - SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     #     return JSONResponse(serializer.data)
    #         return Response(serializer.data)
    #     # return JSONResponse(serializer.errors, status=400)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     # return HttpResponse(status=204)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

