import pandas as pd

#drops any rows or columns where ALL data is missing and returns the dataframe
def drop_all_missing(df):
    # Your code here
    pass

#drops any rows or columns where ANY data is missing and returns the dataframe
def drop_any_missing(df):
    # Your code here
    pass

#Takes in the demographic data DataFrame, returns the sum of the salary
def find_salary_sum(df):
    pass
    

#Merge two dataframes based on a common feature
#Returns a dataframe where with any duplicate columns (i.e. same data) removed
def merge_dataframes(df_left, df_right):
    # Your code here
    pass

def main():
    #csv data loaded
    demo_data = {
        "Name": ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Hank"],
        "Age": ["30", "None", "25", "45", "38", "50", "29", "34"],
        "Salary": ["70000", "80000", "None", "120000", "90000", "None", "61000", "73000"],
        "Experience": ["5", "8", "2", "10", "9", "None", "3", "7"]
    }

    job_description = {
        "Employee_Name": ["Alice", "Dave", "Hank", "Bob", "Grace", "Eve", "Frank", "Carol"],
        "Department": ["HR", "Management", "Finance", "Marketing", "IT", "HR", "Finance", "IT"],
        "Location": ["New York", "Houston", "San Diego", "Los Angeles", "San Antonio", "Phoenix", "Philadelphia", "Chicago"],
        "Tenure": ["None", "None", "None", "None", "None", "None", "None", "None"]
    }

    print(f"The total spent on salaries is {find_salary_sum(demo_data)}")
    merged_data = merge_dataframes(salary_data, job_description)
    only_complete_data = drop_any_missing(merged_data)




    

if __name__ == "__main__":
        main()
