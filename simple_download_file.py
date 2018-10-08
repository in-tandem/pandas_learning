import pandas as panda

remote_location = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

data = panda.read_csv(remote_location)

print(data.describe)

print(data.columns)

features = ['1.4','Iris-setosa']

print(data[features])
print(data.tail())
print(data[35:60])
print(data.iloc[35:60, 1].values)
print(list(data.iloc[35:60, 1].values))
print(type(list(data.iloc[35:60, 1].values)))
print(type(data.iloc[35:60, 1].values))