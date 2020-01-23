import os
import time

import requests
import prometheus_client

auth_req = dict(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
    grant_type='password',
    scope='read_homecoach'
)


temperature = prometheus_client.Gauge('homecoach_temperature', 'temperature (in °C)')
co2 = prometheus_client.Gauge('homecoach_co2', 'CO2 level (in ppm)')
humidity = prometheus_client.Gauge('homecoach_humidity', 'humidity (in %)')
noise = prometheus_client.Gauge('homecoach_noise', 'noise (in dB)')
pressure = prometheus_client.Gauge('homecoach_pressure', 'surface pressure in mbar')
absolute_pressure = prometheus_client.Gauge('homecoach_absolute_pressure', 'sea-level pressure in mbar')
health_index = prometheus_client.Gauge('homecoach_health_index', 'health_index')


def main():
    prometheus_client.start_http_server(5000)
    print('prometheus started')
    print(auth_req)
    while True:
        access_token = requests.post(
            'https://api.netatmo.com/oauth2/token', data=auth_req
        ).json()['access_token']
        print('got access token')
        homecoaches_data = requests.get(
            'https://api.netatmo.com/api/gethomecoachsdata',
            headers={'Authorization': f'Bearer {access_token}',
                     'accept': 'application/json'}
        ).json()['body']['devices'][0]['dashboard_data']
        print('got data')
        temperature.set(homecoaches_data['Temperature'])
        co2.set(homecoaches_data['CO2'])
        humidity.set(homecoaches_data['Humidity'])
        noise.set(homecoaches_data['Noise'])
        pressure.set(homecoaches_data['Pressure'])
        absolute_pressure.set(homecoaches_data['AbsolutePressure'])
        health_index.set(homecoaches_data['health_idx'])
        print('metrics updated, sleeping')
        time.sleep(15)


if __name__ == '__main__':
    main()
