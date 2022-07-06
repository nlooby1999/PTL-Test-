import requests

URL = http://192.168.1.250/esls_new/associate/updateScreen
PARAMS = {'sales_order': }

r = requests.get(url  = URL , params=PARAMS)
data = r.json

work_order = data['results'][0]
sales_order = data['results'][0]
model = data['results'][0]
part = data['results'][0]
quantity = data['results'][0]


{
	[{"mac":"99.96.19.64",
    "mappingtype":515,
    "styleid":44,
    "WO:":"",
    "PART:":"",
    "MODEL:":"",
    "QUANTITY:":"",
    " ":"",
    "SO:":"",
    "ledrgb":"ff00",
    "ledstate":"0",
    "outtime":"30"}]
}

