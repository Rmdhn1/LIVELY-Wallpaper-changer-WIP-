import argparse
import datetime
import json
import os
import subprocess
import sys
import time
import traceback
import urllib.error
import urllib.parse

from itertools import product
from urllib.request import urlopen

import Desktop

import socket
REMOTE_SERVER = "www.google.com"

def get_time_of_day(level=2, hour=None):
    """
    For detail level 2:
    06 to 20: day
    20 to 06: night

    For detail level 3:
    06 to 17: day
    17 to 20: evening
    20 to 06: night

    For detail level 4:
    06 to 08: morning
    08 to 17: day
    17 to 20: evening
    20 to 06: night
    """
    if hour is None:
        current_hour = datetime.datetime.now().hour
    else:
        current_hour = hour

    if level == 2:
        labels = ['day', 'night']
        thres = [5, 19]
    elif level == 3:
        labels = ['day', 'evening', 'night']
        thres = [5, 16, 19]
    elif level == 4:
        labels = ['morning', 'day', 'evening', 'night']
        thres = [5, 7, 16, 19]
    else:
        raise ValueError('Invalid time level.')

    thres.append(current_hour)
    thres.sort()
    day_index = thres.index(current_hour)
    return labels[day_index - 1]
 

def get_weather_summary(weather_name):
    summaries = {'rain': ['drizzle', 'rain', 'shower'],
                 'wind': ['breez', 'gale', 'wind'],  # breez matches both breeze and breezy
                 'thunder': ['thunder'],
                 'snow': ['snow'],
                 'cloudy': ['cloud']}

    for summary, options in summaries.items():
        for option in options:
            if option in weather_name:
                return summary
    return 'normal'


def get_current_weather(location):
    weather_json_url = 'https://api.openweathermap.org/data/2.5/weather?q=Yogyakarta&appid=05ce61391f2d1703d33398e8d715ddec'

    weather_json = json.loads(urlopen(weather_json_url).read().decode('utf-8'))

    weather = str(weather_json['weather'][0]['main']).lower()

    city_with_area = str(weather_json['name']) + ', ' + str(weather_json['sys']['country'])

    return weather, city_with_area

def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
        return False

def running_bat :
    if weather is 'rain':
        subprocess.call([r'D:\Documents\lively_command_utility\Rain.bat'])
        elif weather is 'wind':
            subprocess.call([r'D:\Documents\lively_command_utility\Clear.bat'])
            elif weather is 'thunder':
                subprocess.call([r'D:\Documents\lively_command_utility\Rain.bat'])
                elif weather is 'snow':
                    subprocess.call([r'D:\Documents\lively_command_utility\Rain.bat'])
                    elif weather is 'cloudy':
                        subprocess.call([r'D:\Documents\lively_command_utility\Clear.bat'])
                        elif weather is 'normal':
                            subprocess.call([r'D:\Documents\lively_command_utility\Clear.bat'])
