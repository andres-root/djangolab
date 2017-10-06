# from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User


def index(request):
    if request.method == 'GET':
        first_name = request.GET.get('first_name', '')
        last_name = request.GET.get('last_name', '')
        email = request.GET.get('email', '')
        mobile_phone = request.GET.get('mobile_phone', '')
        password = request.GET.get('password', '')

        if first_name is not '' and last_name is not '' and email is not '' and mobile_phone is not '' and password is not '':
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                is_staff=False,
                is_superuser=False
            )



    response = {'status': '200'}
    return JsonResponse(response)
