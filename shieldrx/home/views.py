from django.shortcuts import render, HttpResponse
import mysql.connector as sql


def index(request):
    return render(request, 'index.html')

