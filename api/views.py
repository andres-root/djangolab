# from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    response = {'status': '200'}
    return JsonResponse(response)
