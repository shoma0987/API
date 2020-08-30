import requests
import pprint
url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
params = {}
params['keyid'] = 'd40fa9adc026143e6293f15b24750e2b'
params['freeword'] = '新橋駅,焼鳥'
print(params)
response = requests.get(url, params)
# print(response)
# print(response.json())

results = response.json()
# print(results)
print(len(results['rest']))
restaurant = results['rest']
print(restaurant[2]['name'])