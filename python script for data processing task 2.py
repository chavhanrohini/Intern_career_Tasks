#!/usr/bin/env python
# coding: utf-8

# In[35]:


pip install cufflinks


# In[36]:


import cufflinks as cf
import numpy as np
import pandas as pd 
import seaborn as sns
from scipy import stats


# In[37]:


iris=sns.load_dataset('iris')


# In[38]:


data=iris


# In[39]:


data


# In[40]:


import seaborn as sns
import pandas as pd

# Load the Iris dataset
iris = sns.load_dataset('iris')
data = iris

# Select only numeric columns
numeric_data = data.select_dtypes(include='number')

# Calculate mean, median, and mode
mean_values = numeric_data.mean()
median_values = numeric_data.median()
mode_values = numeric_data.mode().iloc[0]  # Mode for each column

# Display the results
print("Mean values:\n", mean_values)
print("\nMedian values:\n", median_values)
print("\nMode values:\n", mode_values)


# In[41]:


import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt


# In[42]:


import pandas as pd
import matplotlib.pyplot as plt

def read_dataset(file_path):
    return pd.read_csv(file_path)

def calculate_summary_statistics(data):
    summary_stats = data.describe()
    print("Summary Statistics:\n", summary_stats)
    return summary_stats

def filter_data(data, column_name, criteria):
    filtered_data = data[data[column_name] > criteria]
    print(f"Filtered Data (where {column_name} > {criteria}):\n", filtered_data)
    return filtered_data

def generate_histogram(data, column_name):
    plt.hist(data[column_name], bins=20, edgecolor='black')
    plt.title(f'Histogram - {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()

def save_processed_data(data, output_file):
    data.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    # Example Usage
    input_file_path = 'C:/Users/Dell/Iris.csv'  # Replace with the actual path to your Iris dataset CSV file
    output_file_path = 'C:/Users/Dell/processed_data.csv'

    # Read the dataset
    iris_data = read_dataset(input_file_path)

    # Calculate summary statistics
    calculate_summary_statistics(iris_data)
    
    # Save processed data to a new file
    save_processed_data(iris_data, output_file_path)


# In[43]:


if __name__ == "__main__":
    # Example Usage
    input_file_path = 'C:/Users/Dell/Iris.csv'  
    output_file_path = 'C:/Users/Dell/processed_data.csv'

    # Read the dataset
    iris_data = read_dataset(input_file_path)

    # Filter data based on specific criteria
    filtered_data = filter_data(iris_data, 'SepalLengthCm', 5.0)
    filtered_data = filter_data(iris_data, 'SepalWidthCm', 5.0)
    filtered_data = filter_data(iris_data, 'PetalLengthCm', 5.0)
    filtered_data = filter_data(iris_data, 'PetalWidthCm', 5.0)

    # Generate histogram for a specific column
    generate_histogram(iris_data, 'SepalLengthCm')
    generate_histogram(iris_data, 'SepalWidthCm')
    generate_histogram(iris_data, 'PetalLengthCm')
    generate_histogram(iris_data, 'PetalWidthCm')
    

    # Save processed data to a new file
    save_processed_data(filtered_data, output_file_path)

