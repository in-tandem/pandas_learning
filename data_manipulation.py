
import pandas as panda

remote_location = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


data = panda.read_csv(remote_location, header = None)

data.columns = headers

##describe wihtout args gives you statistical summary of only numeric data type
## include all gives you for all panda datatype including object, hence we can get NaN
""" print(data.describe(include = 'all'))
print(data.dtypes)
print(data.info) """
# print(data['price'].isnull().unique())
""" print(data['price'])
print(type(data)) """

print(data['price'].describe())


""" This was not working since there is a ? in the price values leading 
to datatype being considered as object. hence had to be qouted to
make it work
data['price'].replace(to_replace = '22625', value = '25000', inplace = True)
 """

data['price'].replace(to_replace = '22625', value = '25000', inplace = True)

print(data.tail(10))
# print(data['price'])

print(data['drive-wheels'].value_counts())

print(data.head(10))