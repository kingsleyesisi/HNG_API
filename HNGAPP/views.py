from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import Info

from datetime import datetime

All_Info = Info.objects.all()

class GetInfo(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        for info in All_Info:
            email = info.email
            github_url = info.github_url
            date_time = datetime.now()
            data = {
                "email": email,
                "current_datetime": date_time,
                "github_url" : github_url
                }
            
        return Response(data, status=status.HTTP_200_OK)