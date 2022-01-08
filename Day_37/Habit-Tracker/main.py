import requests
from datetime import datetime
today=datetime.now()
USERNAME="sajda"
TOKEN="ndaeiu43798ewiohfdaskl"
GRAPH_ID="graph1"
TIME=today.strftime("%Y%m%d")
pixle_endpoint="https://pixe.la/v1/users"
user_parmas={
"token":TOKEN,
"username":USERNAME,
"agreeTermsOfService":"yes",
"notMinor":"yes"
}

# respons= requests.post(url=pixle_endpoint,json=user_parmas)
# print(respons.text)

graph_endpoint=f"{pixle_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"min",
    "type":"int",
    "color":"ajisai",
}
headers={
    "X-USER-TOKEN":TOKEN
}
# respons=requests.post(url=graph_endpoint,json=graph_config,headers=headers)

# print(today)
add_pixel_endpoint=f"{pixle_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config={
    "date":TIME,
    "quantity":"60"
}
# respons=requests.post(url=add_pixel_endpoint,json=pixel_config,headers=headers)
# print(respons.text)


pixel_update_endpoint=f"{pixle_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TIME}"

pixle_update_config={
   "quantity":"120"
}
# response=requests.put(url=pixel_update_endpoint,json=pixle_update_config,headers=headers)

response=requests.delete(url=pixel_update_endpoint,headers=headers)
print( response.text)