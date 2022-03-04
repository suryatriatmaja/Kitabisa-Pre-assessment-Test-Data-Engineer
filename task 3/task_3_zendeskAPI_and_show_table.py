import json
import requests
import pandas as pd

#Config get api from zendesk
url = "https://kitabisa3290.zendesk.com/api/v2/tickets.json"

payload={}
headers = {
  'Authorization': 'Basic bGFkb3BhZGVoYmFuYUBnbWFpbC5jb206U3VyeWEyMjEyOTYh',
  'Cookie': '__cfruid=dc997818e2a06df4b742235c86a032cea325b5d1-1646354537; _zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
}
#GET response request
response = requests.request("GET", url, headers=headers, data=payload)

#Transform response to data json
json_data = json.loads(response.text)

#Transform data json to Dataframe using pandas for show tables
df = pd.DataFrame.from_dict(json_data['tickets'][0], orient="index")
print(df)
#Save table to csv for show table using other tools
df.to_csv('zendeskAPI_and_show_table.csv')