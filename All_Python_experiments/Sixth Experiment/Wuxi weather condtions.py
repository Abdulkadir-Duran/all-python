
import pandas

data = pandas.read_csv("Wuxi_weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()


print('average temperature is ', data["temp"].mean())
print('Maximum temperature is ',data["temp"].max())
print('Minimum temperature is ',data["temp"].min())

#Get Data in Columns
print('Name\t\tcondition')
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


