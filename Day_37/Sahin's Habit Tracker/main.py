import requests
from datetime import datetime
USERNAME="sahin"
TOKEN="nciuasfjkaadno"
GRAPH_ID="graph1"
pixel_endpoint="https://pixe.la/v1/users"

user_params={
"token":TOKEN,
"username":USERNAME,
"agreeTermsOfService":"yes",
"notMinor":"yes"
}

# response=requests.post(url=pixel_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixel_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"Working Geaph",
    "unit":"hrs",
    "type":"float",
    "color":"kuro",
}
headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

today=datetime.now()
put_pixel_endpoint=f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How much work you have done today?")
}
respons=requests.post(url=put_pixel_endpoint,json=pixel_config,headers=headers)
print(respons.text)


