# with open("weather_data.csv") as weatherFile:
#     weather= weatherFile.readlines()
#     print(weather)



# import csv
# with open("weather_data.csv") as data_file:
#     data =csv.reader(data_file)
#     tempreture=[]
#     for row in data:
#         if row[1]!='temp':
#             tempreture.append(int(row[1]))
#     print(tempreture)




# import pandas

# data =pandas.read_csv("weather_data.csv")
# temp_list=data["temp"].to_list()
# # sum=0
# # for i in temp_list:
# #     sum=sum+i
# # print(sum/len(temp_list))

# # avg=sum(temp_list)/len(temp_list)
# # print(avg)



# avg=data["temp"].mean()
# print(avg)

# print(data["temp"].max())



# # get data in coloums
# data["condition"]
# print (data.condition)


# # get data in row
# print (data[data.temp==data.temp.max()])











import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])

print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}
df=pandas.DataFrame(data_dict)
print(df.to_csv("squirrel_count.csv"))