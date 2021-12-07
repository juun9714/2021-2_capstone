#!/usr/bin/env python
import rospy
import asyncio
from websocket import create_connection
import requests
import json
import socket
import datetime
import sys
import logging, os
import time
import threading
import ast

import pandas as pd
import numpy as np

from std_msgs.msg import String, Header, Float64
from sensor_msgs.msg import NavSatFix,TimeReference, BatteryState, Range, Temperature, FluidPressure
from mavros_msgs.msg import PositionTarget, State, ADSBVehicle, RCIn, RCOut

# Geometry message type
from geometry_msgs.msg import Twist, TwistStamped, Vector3, Pose, Point, PoseWithCovariance, Quaternion, PoseStamped
from nav_msgs.msg import Odometry


def get_now():
    return datetime.datetime.now()

def timedelta2float(td):
    res = td.microseconds/float(1000000) + (td.seconds + td.days * 24 * 3600)
    return res
    
global final_bat
global final_gpo
global final_tem

final_bat={}
final_gpo={}
final_tem={}


def battery_callback(data):
    #f = open("test.json","rb")
    #final_bat=json.loads(f.read())
    #f.close()
    global final_bat
    final_bat={
                "r1ID": "9e64",
                "value":str({
                    "battery":data.voltage
                    }),
                "timestamp":str(get_now())
            }

    #temp_data['Vehicle']['Battery'].append(newItem)

    #f=open("test.json","w")
    #f.write(json.dumps(temp_data))
    #f.close()


def globalP_local_callback(data):
    #f=open("test.json","rb")
    #temp_data=json.loads(f.read())
    #f.close()

    global final_gpo
    final_gpo={
            "r1ID": "9e64",
            "value":str(
                {"posex":data.pose.pose.position.x,
                    "posey":data.pose.pose.position.y,
                    "posez":data.pose.pose.position.z,
                    "orix":data.pose.pose.orientation.x,
                    "oriy":data.pose.pose.orientation.y,
                    "oriz":data.pose.pose.orientation.z,
                    "oriw":data.pose.pose.orientation.w}
                ),
            "timestamp":str(get_now())
            }

    # temp_data['Vehicle']['Gposition'].append(newItem)
    
    # f=open("test.json","w")
    # f.write(json.dumps(temp_data))
    # f.close()

def temperature_baro_callback(data):
    f=open("test.json","rb")
    temp_data=json.loads(f.read())
    f.close()

    global final_tem
    final_tem={
            "r1ID": "9e64",
            "value":str(
                {"temperature":data.temperature,
                    "variance":data.variance
                }
                ),
            "timestamp":str(get_now())
            }

    if final_tem is not {}:
        temp_data['Vehicle']['Temperature'].append(final_tem)
    
    if final_gpo is not {}:
        temp_data['Vehicle']['Gposition'].append(final_gpo)
    if final_bat is not {}:
        temp_data['Vehicle']['Battery'].append(final_bat)

    print(temp_data)
    f=open("test.json","w")
    f.write(json.dumps(temp_data))
    f.close()


def listener(rospy):
    rospy.Subscriber("/mavros/battery", BatteryState, battery_callback)
    rospy.Subscriber("/mavros/imu/temperature_baro", Temperature, temperature_baro_callback)
    rospy.Subscriber("/mavros/global_position/local",Odometry,globalP_local_callback)
    rospy.spin()

def receiver():
    client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,1)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    client.bind(("",37020))

    server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)



    v2i_total_delay = 0.0
    v2i_cnt = 1
    v2i_delay_list = []
    v2v_total_delay = 0.0
    v2v_cnt = 1
    v2v_delay_list = []
    while True:
        #data, addr=client.recvfrom(1024)
        #print("received")
        #server.sendto(data,('255.255.255.255',37021))
        #print("sent")
        #v2v_rcv_time=ast.literal_eval(data.decode("UTF-8"))["timestamp"]
        #print("[RECEIVED_V2V] "+ast.literal_eval(data.decode("UTF-8"))["timestamp"])
        #v2v_delay = get_now() - datetime.datetime.strptime(v2v_rcv_time, "%Y-%m-%d %H:%M:%S.%f")
        #v2v_total_delay += v2v_delay.total_seconds()
        #v2v_cnt += 1
        #print("[V2V_avg_Delay]",end='')
        #print(v2v_delay, end='[avg]')
        #print(v2v_total_delay/v2v_cnt)
        
        #time.sleep(1)
        response = requests.get("http://18.222.149.253:5056/battery")
        received_time = response.json()[-1]['timestamp']


        print(get_now(), datetime.datetime.strptime(received_time, "%Y-%m-%d %H:%M:%S.%f"))
        delay = get_now() - datetime.datetime.strptime(received_time, "%Y-%m-%d %H:%M:%S.%f")
        v2i_total_delay += delay.total_seconds()
        v2i_cnt += 1
        v2i_delay_list.append(v2i_total_delay/v2v_cnt)

                #if(v2i_cnt >= 100):
                #	v2i_df = pd.DataFrame(v2i_delay_list, columns = ['Delay'])
                #	v2i_df.to_csv("v2i_delay.csv")


        print("[V2I_Delay]",end='')
        print(delay, end=' [avg] ')
        print(v2i_total_delay/v2i_cnt)


                #receiving broadcast message from another vehicle
        
	

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    sender = threading.Thread(target=listener, args=(rospy,))
    #receiver = threading.Thread(target=receiver)
    sender.start()
    #receiver.start()
