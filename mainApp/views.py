from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import auth 
from rest_framework.authtoken.models import Token



def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'articles/year_archive.html', context)



class LoginApi(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    def post(self,request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if User is not None:
            token = Token.objects.get(user=user)
            u_serializer = UserSerializer(user,many=False)
            return Response({"token":str(token), "user":u_serializer.data},status=status.HTTP_200_OK)
        else : return Response(status=status.HTTP_401_UNAUTHORIZED)