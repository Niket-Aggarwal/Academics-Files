from rest_framework.decorators import api_view
from rest_framework.response import Response
from Main.models import Room
from .serializer import RoomSerializer

@api_view(['GET'])
def getroutes(request):
    routes=[
        'GET/api',
        'GET/api/room',
        'GET/api/rooms/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getrooms(request):
    room=Room.objects.all()
    serialiser=RoomSerializer(room,many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def getroomno(request,pk):
    room=Room.objects.filter(id=pk)
    serialiser=RoomSerializer(room,many=True)
    return Response(serialiser.data)