from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from .forms import FormAuthForm
import json
import ast
import jwt
import environ


env = environ.Env()
# Create your views here.
def home(request):
  return render(request,'index.html')
  
def login(request):
  return render(request,'login.html')
  
def signup(request):
  return render(request,'signup.html')

@csrf_exempt
def loginapi(request):
  body= ast.literal_eval(request.body.decode())
  
  print(env('jwt_key'))
  jwt=body.get("jwt")
  return HttpResponse("done")
  
@csrf_exempt
def signupapi(request):
  """
  body= ast.literal_eval(request.body.decode())
  print(body)
  email =body.get("email")
  password =body.get("password")
  """
  
  form= FormAuthForm(request.POST)
  if form.is_valid():
    print(form.is_valid)
    form.save()
    return JsonResponse({"success":True})
  else:
    return JsonResponse({"success":False,"email":"email"})