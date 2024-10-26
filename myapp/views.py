# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer

@api_view(['GET', 'POST'])
def leave_requests(request):
    if request.method == 'GET':
        leaves = LeaveRequest.objects.all()
        serializer = LeaveRequestSerializer(leaves, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = LeaveRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
