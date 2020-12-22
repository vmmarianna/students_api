from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def ping(request):
    data = request.data
    return Response({'message': 'pong', 'data': data})


@api_view(['POST'])
def simple_post(request):
    data = request.data
    return Response({'success': True, 'data': data})
