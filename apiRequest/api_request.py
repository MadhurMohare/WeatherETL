import requests

api_key = 'API KEY HERE'
api_url = f'http://api.weatherstack.com/current?access_key={api_key}'
querystring = {"query":"London", "historical_date_start":"2025-05-25", "historical_date_end":"2025-06-25"}

def fetchData():
    print('Fetching Data from WeatherStack API ...')
    try:
        response = requests.get(api_url, params=querystring)
        response.raise_for_status()
        print('API Response Successful')
        return response.json()
    except requests.exceptions.RequestException as e:
        print('An Exception Occured : ', e)
        raise

def mockfetchData():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-06-23 14:15', 'localtime_epoch': 1750688100, 'utc_offset': '-4.0'}, 'current': {'observation_time': '06:15 PM', 'temperature': 37, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '05:26 AM', 'sunset': '08:31 PM', 'moonrise': '03:12 AM', 'moonset': '07:12 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 9}, 'air_quality': {'co': '451.4', 'no2': '24.605', 'o3': '139', 'so2': '5.735', 'pm2_5': '17.39', 'pm10': '17.945', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 5, 'wind_degree': 280, 'wind_dir': 'W', 'pressure': 1018, 'precip': 0, 'humidity': 45, 'cloudcover': 75, 'feelslike': 44, 'uv_index': 9, 'visibility': 16, 'is_day': 'yes'}}
