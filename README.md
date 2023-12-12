# Intern_career_Tasks

# Task1- Retrieving Camera Information from Flipkart Website

In the first task of this project, I implemented a web scraping approach to gather details about cameras available on the Flipkart website. After entering the Flipkart URL, I selected the following key details for each camera from the loaded webpage:

1. Camera Name
2. Price
3. Features
4. Effective Pixels
5. Sensor Type

Subsequently, this selected data was organized into a structured format by creating a data frame. This data frame served as the foundation for further analysis and processing in the subsequent tasks of the project.

In subsequent steps, each attribute of the selected data, including camera name, price, features, effective pixels and sensor type underwent a meticulous cleaning process. This ensured that the final dataset was refined and ready for downstream analysis and utilization.

This methodology allowed for the extraction of meaningful insights from the camera data, facilitating a more efficient and informed decision-making process for users interested in purchasing cameras from Flipkart.

url= "https://www.flipkart.com/search?q=camera&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_6_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_6_na_na_na&as-pos=4&as-type=RECENT&suggestionId=camera&requestId=c47f1865-d7a5-45c2-94d3-944b5486d93f&as-searchtext=camera"

# Task2- Data Processing Script
Data Processing Script Documentation

Introduction:
This Python script serves as a flexible tool for performing fundamental data processing tasks on datasets, exemplified with the Iris dataset. Its functionality encompasses data reading, summarization, filtering, visualization, and storage. Ensure the installation of necessary dependencies: pandas, matplotlib, seaborn, numpy, and scipy.

How to Use:
1. Load Required Libraries:
   Import essential libraries such as pandas, matplotlib, seaborn, and scipy.

2. Load the Iris Dataset:
   Utilize the script with the example Iris dataset or substitute it with your own.

3. Summary Statistics Calculation:
   Calculate mean, median, and mode for numeric columns in the dataset.

4. Data Processing Functions:
   - read_dataset(file_path): Read a dataset from a CSV file.
   - calculate_summary_statistics(data): Compute and display summary statistics.
   - filter_data(data, column_name, criteria): Filter data based on specific criteria.
   - generate_histogram(data, column_name): Generate a histogram for a given column.
   - save_processed_data(data, output_file): Save processed data to a new CSV file.

5. Example Usage:
   Use the provided example to understand how to read data, calculate statistics, filter based on criteria, generate histograms, and save processed data.

6. Inspect Outputs:
   Review printed summary statistics, filtered data, and histograms. The processed data is stored in the specified output file.

7. Customize as Needed:
   Tailor the script to your requirements by adjusting criteria, column names, or histogram settings.

8. Repeat for Different Datasets:
   This script is adaptable and can be seamlessly integrated with various datasets. Simply replace the example dataset and file paths.

