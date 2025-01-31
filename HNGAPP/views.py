from django.http import JsonResponse

from datetime import datetime

def get(request):
        data = {
            "email": "kingsleyesisi@yahoo.com",
            "current_datetime": datetime.now().replace(microsecond=0).isoformat()+"Z,
            "github_url" : "https://kingsleyesisi/HNG_API"
            }
        return JsonResponse(data)
