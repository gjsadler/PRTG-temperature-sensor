import requests
import json
from prtg.sensor.result import CustomSensorResult
from prtg.sensor.units import ValueUnit



response = requests.get("http://10.61.1.191/api/dev")


data = json.loads(response.text)
temp = data['data']['DF049162895E78C3']['entity']['0']['measurement']['0']['value']
#print(temp)


channel = {}
channel["prtg"] = {"result":[{"channel" : "Temp","value" : temp,"float" : 1,"DecimalMode" : "All","unit" :"custom","customunit":"F","LimitMaxError": "80","LimitMaxWarning" : "75","LimitMode": 1}]}

print(json.dumps(channel))
