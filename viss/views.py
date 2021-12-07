import random
import json
import copy
#from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse, response


from viss.lib import *

# VISSv2 & VSSv2.1

def Vehicle_Battery(request):
    print("IN Vehicle_Battery")
    with open('viss/test.json') as generated_data:  # without children directory
        vehicle_data = json.loads(generated_data.read())
        response_data=vehicle_data['Vehicle']['Battery'][-1]
            
    ########AFTER RETURN response_data#########        
    if "error" in response_data:
        # error 반환시, 404 status로 client에 응답
        return JsonResponse(response_data, status=404)
    else:
        # response data에 error없을시, 200 status로 client에 응답
        return JsonResponse(response_data, status=200)

def Vehicle_temper(request):
    print("IN Vehicle_Battery")
    with open('viss/test.json') as generated_data:  # without children directory
        vehicle_data = json.loads(generated_data.read())
        response_data=vehicle_data['Vehicle']['Temperature'][-1]
            
    ########AFTER RETURN response_data#########        
    if "error" in response_data:
        # error 반환시, 404 status로 client에 응답
        return JsonResponse(response_data, status=404)
    else:
        # response data에 error없을시, 200 status로 client에 응답
        return JsonResponse(response_data, status=200)

def Vehicle_Gposition(request):
    print("IN Vehicle_Battery")
    with open('viss/test.json') as generated_data:  # without children directory
        vehicle_data = json.loads(generated_data.read())
        response_data=vehicle_data['Vehicle']['Gposition'][-1]
            
    ########AFTER RETURN response_data#########        
    if "error" in response_data:
        # error 반환시, 404 status로 client에 응답
        return JsonResponse(response_data, status=404)
    else:
        # response data에 error없을시, 200 status로 client에 응답
        return JsonResponse(response_data, status=200)
