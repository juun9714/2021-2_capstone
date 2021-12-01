import random
import json
import copy
#from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse, response

#from rest_framework.decorators import api_view, permission_classes, authentication_classes, throttle_classes
#from rest_framework.decorators import api_view

from viss.lib import *
from viss.data_generator import *

# VISSv2 & VSSv2.1

# authorization이 아닌 경우 실행
#@api_view(['GET', 'POST'])

def Vehicle(request):
    # print("IN VEHICLE")
    with open('viss/vss_final.json') as generated_data:  # without children directory
        vehicle_data = json.loads(generated_data.read())
        # data_generator로 만든 vehicle data -> 추후에 각 함수에 전달

    with open('viss/vss_metadata.json') as generated_data:  # without children directory
        vehicle_metadata = json.loads(generated_data.read())
        # data_generator로 만든 vehicle data -> 추후에 각 함수에 전달
    query_params = request.query_params.dict()

    url_path = request.path[1:len(request.path)]
    if request.method == 'GET':
        if url_path[len(url_path)-1] == "/":  # set url end without slash
            url_path = url_path[0:len(url_path)-1]

        # GET data
        if "filter" not in query_params:  # GET && no filter ex. GET /Vehicle/Speed HTTP/1.1
            # just return single data & no filter
            response_data = read(url_path, vehicle_data) 
            
    ########AFTER RETURN response_data#########        
    if "error" in response_data:
        # error 반환시, 404 status로 client에 응답
        return JsonResponse(response_data, status=404)
    else:
        # response data에 error없을시, 200 status로 client에 응답
        return JsonResponse(response_data, status=200)


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
