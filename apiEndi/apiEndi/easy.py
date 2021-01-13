from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.contrib.auth.models import User
import time
import json
import pytz

jsonDec = json.decoder.JSONDecoder()

ist_tz = pytz.timezone("Asia/Kolkata")

def list_to_str(value):
    return json.dumps(value)

def str_to_list(value):
    return jsonDec.decode(value)

def getUserFromUsername(username):
    return User.objects.get(username=username)

def getUserFromId(id):
    return User.objects.get(id=id)

def UTCtoITC(value):
    return value.replace(tzinfo=pytz.utc).astimezone(ist_tz)




