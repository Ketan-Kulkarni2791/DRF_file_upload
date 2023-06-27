from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser


def home(request):
    return render(request ,'home.html')


def download(request , uid):
    return render(request , 'download.html' , context = {'uid' : uid})


class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "Status": 200,
                        "Message": "Files uploaded successfully",
                        'data' : serializer.data
                    }
                )
            return Response(
                {
                    "Status": 400,
                    "Message": "Something went wrong",
                    "Data": serializer.errors
                }
            )
        except Exception as e:
            return Response(
                {"Message": e}
            )
