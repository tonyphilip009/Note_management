from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken

class RegistrationView(APIView):

    def post(self,request):

        serializer_instance=RegisterSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={"message":"Registration is successful"})
        else:
            return Response(data=serializer_instance.errors)

class ListNotes(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request):

        note=NoteDb.objects.filter(user=request.user)
        serializer_instance=NoteSerializer(note,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data=request.data
        serializer_instance=NoteSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class NoteRetriveUpdateDelete(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request,note_id):

        note_object=get_object_or_404(NoteDb,id=note_id,user=request.user)
        serializer_instance=NoteSerializer(note_object)
        return Response(data=serializer_instance.data)

    def put(self,request,note_id):

        note_object=get_object_or_404(NoteDb,id=note_id,user=request.user)

        serializer_instance=NoteSerializer(note_object,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,note_id):

        note_object=get_object_or_404(NoteDb,id=note_id,user=request.user)
        note_object.delete()
        return Response(data={"message":"note is deleted"})

class LogOut(APIView):

    permission_classes=[IsAuthenticated]

    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message":"Logout success.."})

class TaskListCreate(APIView):

    permission_classes=[IsAuthenticated]


    def get(self,request):

        task_object=TaskDb.objects.filter(user=request.user)
        serializer_instance=TaskSerializer(task_object,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data=request.data
        serializer_instance=TaskSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(data=serializer_instance.data,status=201)
        else:
            return Response(data=serializer_instance.errors)

class RetriveUpdateDelete(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request,pk):

        task_object=get_object_or_404(TaskDb,id=pk,user=request.user)

        serializer_instance=TaskSerializer(task_object)

        return Response(data=serializer_instance.data,status=200)

    def put(self,request,pk):

        form_data=request.data
        task_object=get_object_or_404(TaskDb,id=pk,user=request.user)

        serializer_instance=TaskSerializer(task_object,data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):

        task_object=get_object_or_404(TaskDb,id=pk,user=request.user)
        task_object.delete()
        return Response(data={"message":"deleted"})

class jwt_logout(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            refresh_token=request.data.get("refresh")
            token=RefreshToken(refresh_token).blacklist()
            return Response(data={"message":"logged out"})
        except Exception:
            return Response("invalid refresh token")