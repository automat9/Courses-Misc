import pandas as pd
import matplotlib as plt

# Load data from GitHub URL
url = "https://github.com/automat9/Business-Analytics/raw/aadac54eaf6f4ca76c4970a1d317ad355a7fe051/Semester%201/Programming%20for%20Business%20Analytics/Midterm%20Project/Coffee_company.csv"
data = pd.read_csv(url)

# removes extra space in column names
data.columns = data.columns.str.strip()

data.head()

# floats into whole numbers
data('Units Sold') = data('Units Sold').astype(int)


print(data.columns) # to check the excact names of each column
