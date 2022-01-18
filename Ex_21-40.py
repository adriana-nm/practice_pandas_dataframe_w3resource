import pandas as pd
import numpy as np


# 21. Write a Pandas program to iterate over rows in a DataFrame.
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
df = pd.DataFrame(exam_data)
df

for i in range(3):
   print(df.loc[i,:]) #it print it in a serie (columns are index now)

for i in range(3):
    print(df.loc[[i]])   #it will print the index & column for each data

for index,row in df.iterrows():
    print(row)        #it print it in a serie (columns are index now)

for index,row in df.iterrows():
    print(row['name'],row['score'])   #it prints it in a line (without index/column)


# 22. Write a Pandas program to get list from DataFrame column headers.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                      'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                      'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                      'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)

list(df.columns.values)

# 23. Write a Pandas program to rename columns of a given DataFrame
data = [[1,4,7],[2,5,8],[3,6,9]]
df = pd.DataFrame (data, columns=['col1','col2','col3'])
df

df.rename(columns={'col1' : 'Column1','col2':'Column2','col3':'Column3'},inplace=True)
df

# 24. Write a Pandas program to select rows from a given DataFrame based on values in some columns.
data = [[1,4,7],[4,5,8],[3,6,9],[4,7,0],[5,8,1]]
df = pd.DataFrame (data, columns=['col1','col2','col3'])
df

df[df['col1'].isin([4])]

# 25. Write a Pandas program to change the order of a DataFrame columns.
data = [[1,4,7],[4,5,8],[3,6,9],[4,7,0],[5,8,1]]
df = pd.DataFrame (data, columns=['col1','col2','col3'])
df

df = df[['col3','col2','col1']]
df

# 26. Write a Pandas program to add one row in an existing DataFrame.
data = [[1,4,7],[4,5,8],[3,6,9],[4,7,0],[5,8,1]]
df = pd.DataFrame (data, columns=['col1','col2','col3'])
df

# Solution A
new_row = pd.DataFrame([[10,11,12]],columns = ['col1','col2','col3'],index=[5])
df.append(new_row)
df

# Solution B
new_row = {'col1': 10, 'col2': 11, 'col3': 12}
df = df.append(new_row, ignore_index=True)
df

# 27. Write a Pandas program to write a DataFrame to CSV file using tab separator.
data = [[1,4,7],[4,5,8],[3,6,9],[4,7,0],[5,8,1]]
df = pd.DataFrame (data, columns=['col1','col2','col3'])
df

df.to_csv('new_file.csv', sep='\t', index=False)
new_df = pd.read_csv('new_file.csv', sep='\t')
new_df

# 28. Write a Pandas program to count city wise number of people from a given of data set (city, name of the person).
city_names= {'city': ['California', 'Los Angeles', 'California', 'Georgia', 'Los Angeles', 'California', 'Los Angeles', 'Georgia', 'Los Angeles', 'California'],
             'names': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas']}
df = pd.DataFrame(city_names)

# Solution 1
df = df.groupby(by='city').count()
df.columns = df.columns.str.replace('names','Number of people')

# Solution 2
df.groupby(by='city').size().reset_index(name='Number of people')

# 29. Write a Pandas program to delete DataFrame row(s) based on given column value.
# Everything in Col2 != 5
data = [[1,4,7],[4,5,8],[3,6,9],[4,7,0],[5,8,1]]
df = pd.DataFrame (data, columns=['col1','col2','col3'])

df = df[df['col2'] != 5]
df


# 30. Write a Pandas program to widen output display to see more columns.
data = [[1,4,7],[4,5,8],[3,6,9],[4,7,0],[5,8,1]]
df = pd.DataFrame (data, columns=['col1','col2','col3'])

pd.set_option('display.max_columns', 300)
pd.set_option('display.max_rows', 300)
pd.set_option('display.width',None)
