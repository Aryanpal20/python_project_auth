from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from social_django.models import UserSocialAuth
from rest_framework.response import Response

# Create your views here.

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')



class GetAllUser(APIView):
    def get(self, request, pk=None):
        users = UserSocialAuth.objects.get(pk=pk)
        # UserSocialAuth.
        dict = {}
        # dict['user'] = users
        dict["user_id"] = users.user.id
        dict['provider'] = users.provider
        dict['token'] = users.extra_data['access_token']
        
        return Response (dict) 
        
