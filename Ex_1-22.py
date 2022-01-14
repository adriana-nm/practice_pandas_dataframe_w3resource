import pandas as pd
import numpy as np


# 1. Write a Pandas program to get the powers of an array values element-wise.
# Note: First array elements raised to powers from second array
# {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df1 =  pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]},index=[0,1,2,3,4])

#Solution A
df1['X'] ** df1['Y']

#Solution B
np.power(df1['X'],df1['Y'])

#Solution C
df1.apply(lambda row: row['X'] ** row['Y'], axis=1)


# 2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
# Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Solution
df = pd.DataFrame(exam_data,index=labels)


# 3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
df.describe()


# 4. Write a Pandas program to get the first 3 rows of a given DataFrame.
def first3_rows(df):
    print(df.iloc[0:3])

first3_rows(df)

# 5. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
df[['name','score']]


# 6. Write a Pandas program to select the specified columns and rows from a given data frame.
df[['score','attempts']].loc[['b','d','f','g']]


# 7. Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
df[df['attempts']>2]                #All the row
df['attempts'][df['attempts']>2]    #Only the number of attempts

# 8. Write a Pandas program to count the number of rows and columns of a DataFrame
numcol = len(df.columns)
numrow = len(df.index)
print('Number of Rows:{}'.format(numrow))
print('Number of Columns:{}'.format(numcol))

# 9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
df[df['score'].isnull()]


# 10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
df[(df['score'] >=15) & (df['score'] <= 20)]


# 11. Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
df[(df['attempts'] < 2) & (df['score'] > 15)]


# 12. Write a Pandas program to change the score in row 'd' to 11.5.
df['score'].loc['d'] = 11.5


# 13. Write a Pandas program to calculate the sum of the examination attempts by the students.
df['attempts'].sum()


# 14. Write a Pandas program to calculate the mean score for each different student in DataFrame.
df['score'].mean()


# 15. Write a Pandas program to append a new row 'k' to data frame with given values for each column.
# Now delete the new row and return the original DataFrame.
#name : "Suresh", score: 15.5, attempts: 1, qualify: "yes",
#label: "k"
new_row = pd.DataFrame([['Suresh',15.5,1,'yes']], columns=['name','score','attempts','qualify'] , index=['k'])
df = df.append(new_row)

df.drop('k',axis=0,inplace=True)
df

# 16. Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.



# 17. Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.



# 18. Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame.



# 19. Write a Pandas program to delete the 'attempts' column from the DataFrame.



# 20. Write a Pandas program to insert a new column in existing DataFrame



# 21. Write a Pandas program to iterate over rows in a DataFrame.



# 22. Write a Pandas program to get list from DataFrame column headers.




