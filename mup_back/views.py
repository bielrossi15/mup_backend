from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from .serializers import AboutSerializer, GeneralSerializer, BoletimSerializer
from .models import About, General, Boletim
from django.shortcuts import get_object_or_404



class AboutViewSet(ModelViewSet):
    """
    A viewset for viewing and deleting about instances
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = (permissions.AllowAny,)

    def retrieve(self, request, pk=None):
        text = get_object_or_404(self.queryset, pk=pk)
        if text:
            serializer = AboutSerializer(text)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data="Text deleted")



class BoletimViewSet(ModelViewSet):
    """
    A viewset for viewing and deleting about instances
    """
    queryset = Boletim.objects.all()
    serializer_class = BoletimSerializer
    permission_classes = (permissions.AllowAny,)

    def retrieve(self, request, pk=None):
        text = get_object_or_404(self.queryset, pk=pk)
        if text:
            serializer = BoletimSerializer(text)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data="Text deleted")


class GeneralViewSet(ModelViewSet):
    """
    A viewset for viewing and editing about instances
    """
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
    permission_classes = (permissions.AllowAny,)
    
    def retrieve(self, request, pk=None):
        text = get_object_or_404(self.queryset, pk=pk)
        if text:
            serializer = GeneralSerializer(text)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data="Text deleted")

    def post(self, validated_data):
        return self.create(request, *args, **kwargs)



@api_view(["POST"],)
def post_about(request):
    if request.method == "POST":
        serializer = AboutSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"],)
def post_boletim(request):
    if request.method == "POST":
        serializer = BoletimSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"],)
def post_general(request):
    if request.method == "POST":
        serializer = GeneralSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

