import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['ram', 'hari', 'sita', 'panna', 'raj'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Age': [30, 28, 35, 40, 25],
    'Salary': [70000, 60000, 80000, 90000, 55000],
    'JoinDate': pd.to_datetime(['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01']),
    'ExperienceYears': [5, 3, 7, 11, 2]
}

df = pd.DataFrame(data)

print("\nName and Salary:\n", df[['Name', 'Salary']])

print("\nEmployees in IT:\n", df[df['Department'] == 'IT'])

print("\nEmployees older than 30:\n", df[df['Age'] > 30])
print("\nAverage Salary per Department:\n", df.groupby('Department')['Salary'].mean())

print("\nEmployee count per Department:\n", df['Department'].value_counts())

df['Bonus'] = df['Salary'] * 0.10
print("\nWith Bonus Column:\n", df)

df['Department'] = df['Department'].replace('HR', 'Human Resources')
print("\nDepartment Replaced:\n", df)

longest_tenure = df[df['JoinDate'] == df['JoinDate'].min()]
print("\nEmployee with Longest Tenure:\n", longest_tenure)

df['SalaryCategory'] = df['Salary'].apply(lambda x: 'High' if x > 75000 else 'Low')
print("\nWith Salary Category:\n", df)

df = df.drop_duplicates(subset='EmployeeID')
print("\nAfter Removing Duplicate EmployeeIDs:\n", df)

print("\nMedian Age:", df['Age'].median())
