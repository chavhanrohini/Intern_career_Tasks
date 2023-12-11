#!/usr/bin/env python
# coding: utf-8

# In[28]:


pip install bs4


# In[29]:


pip install requests


# In[30]:


from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from bs4 import BeautifulSoup
import requests
import pandas as pd


# # Data exploration

# In[31]:


# Function to scrap the camera details
def scrape_flipkart_camera_details():
    url="https://www.flipkart.com/search?q=camera&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_6_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_6_na_na_na&as-pos=4&as-type=RECENT&suggestionId=camera&requestId=c47f1865-d7a5-45c2-94d3-944b5486d93f&as-searchtext=camera"


# In[32]:


url="https://www.flipkart.com/search?q=camera&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_6_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_6_na_na_na&as-pos=4&as-type=RECENT&suggestionId=camera&requestId=c47f1865-d7a5-45c2-94d3-944b5486d93f&as-searchtext=camera"


# In[33]:


r=requests.get(url)


# In[34]:


r


# In[35]:


soup=BeautifulSoup(r.text)
camera_name=soup.select("._4rR01T")
camera_name=camera_name[:14]
all_names_of_camera=[]
for i in camera_name:
    all_names_of_camera.append(i.text)


# In[36]:


all_names_of_camera


# In[37]:


price=soup.select("._30jeq3")
price = price[:14]
camera_price=[]
for i in price:
    camera_price.append(i.text)


# In[38]:


camera_price


# In[39]:


features=soup.select(".rgWa7D")
features=features[:14]
camera_features=[]
for i in features:
    camera_features.append(i.text)


# In[40]:


camera_features


# In[41]:


effective_pixels=soup.select(".rgWa7D:nth-child(2)")
effective_pixels=effective_pixels[:14]
effective_pixels_all_cameras=[]
for i in effective_pixels:
    effective_pixels_all_cameras.append(i.text)


# In[42]:


effective_pixels_all_cameras


# In[43]:


sensor_type=soup.select(".rgWa7D:nth-child(3)")
sensor_type=sensor_type[:14]
sensor_type_of_all_cameras=[]
for i in sensor_type:
    sensor_type_of_all_cameras.append(i.text)
    


# In[44]:


sensor_type_of_all_cameras


# In[45]:


resolution=soup.select(".rgWa7D:nth-child(5)")
resolution=resolution[:14]
resolutions=[]
for i in resolution:
    resolutions.append(i.text)


# In[46]:


resolutions


# warranty=soup.select(".rgWa7D:nth-child(6)")
# warranty=warranty[:14]
# warranties=[]
# for i in warranty:
#     warranties.append(i.text)

# # DataFrame Creation

# In[47]:


import pandas as pd

camera_dataset = pd.DataFrame({'camera_name': camera_name})


# In[49]:


# Ensure lengths are the same
max_length = max(len(camera_name), len(price), len(features), len(effective_pixels), len(sensor_type), len(resolution))

# Create Series with NaN values and set common index
camera_name = pd.Series(camera_name, index=range(max_length))
price = pd.Series(price, index=range(max_length))
features = pd.Series(features, index=range(max_length))
effective_pixels = pd.Series(effective_pixels, index=range(max_length))
sensor_type = pd.Series(sensor_type, index=range(max_length))
resolution = pd.Series(resolution, index=range(max_length))

# Create DataFrame by concatenating Series
camera_dataset = pd.DataFrame({
    'camera_name': camera_name,
    'price': price,
    'features': features, 
    'effective_pixels': effective_pixels,
    'sensor_type': sensor_type,
    'resolution': resolution
})


# In[50]:


camera_dataset


# # Excel file creation

# In[51]:


datatoexcel=pd.ExcelWriter("Cameraflip.xlsx",engine='xlsxwriter')


# In[52]:


camera_dataset.to_excel(datatoexcel, sheet_name='sheet1')


# In[53]:


datatoexcel.save()


# # Data cleaning and Organization

# In[54]:


if __name__ == '__main__':
    camera_dataset = pd.read_excel('Cameraflip.xlsx')
    print(camera_dataset)
    print(type(camera_dataset))

camera_dataset['features']=camera_dataset['features'].str.replace(r'\W', "")
print(camera_dataset)
    


# In[55]:


camera_dataset['camera_name']=camera_dataset['camera_name'].str.replace(r'\W', "", regex=True)
camera_dataset['effective_pixels']=camera_dataset['effective_pixels'].str.replace(r'\W', "", regex=True)
camera_dataset['sensor_type']=camera_dataset['sensor_type'].str.replace(r'\W', "", regex=True)
camera_dataset['resolution']=camera_dataset['resolution'].str.replace(r'\W', "", regex=True)
camera_dataset['camera_name']=camera_dataset['camera_name'].str.replace('divclass_4rR01T', "", regex=True)
camera_dataset['camera_name']=camera_dataset['camera_name'].str.replace('div', "", regex=True)
camera_dataset['price']=camera_dataset['price'].str.replace('<div class="_30jeq3 _1_WHN1">', "", regex=True)
camera_dataset['price']=camera_dataset['price'].str.replace('</div>', "",regex=True)
camera_dataset['price']=camera_dataset['price'].str.replace('₹', "",regex=True)
camera_dataset['features']=camera_dataset['features'].str.replace('liclassrgWa7D', "",regex=True)
camera_dataset['features']=camera_dataset['features'].str.replace('li', "",regex=True)
camera_dataset['effective_pixels']=camera_dataset['effective_pixels'].str.replace('liclassrgWa7DEffectivePixels', "",regex=True)
camera_dataset['effective_pixels']=camera_dataset['effective_pixels'].str.replace('li', "",regex=True)
camera_dataset['effective_pixels']=camera_dataset['effective_pixels'].str.replace('liclassrgWa7D', "",regex=True)
camera_dataset['effective_pixels']=camera_dataset['effective_pixels'].str.replace('classrgWa7D', "",regex=True)
camera_dataset['sensor_type']=camera_dataset['sensor_type'].str.replace('liclassrgWa7DSensorType', "",regex=True)
camera_dataset['sensor_type']=camera_dataset['sensor_type'].str.replace('li', "",regex=True)
camera_dataset['sensor_type']=camera_dataset['sensor_type'].str.replace('classrgWa7D', "",regex=True)
camera_dataset['resolution']=camera_dataset['resolution'].str.replace('liclassrgWa7D', "",regex=True)
print(camera_dataset)


# In[56]:


camera_dataset


# In[57]:


cleaned_data=camera_dataset


# # Creating the Excel file of cleaned data

# In[58]:


import pandas as pd
output_file_path = 'Cleaned_Cameraflip.xlsx'

# Save the DataFrame to an Excel file
cleaned_data.to_excel(output_file_path, index=False)

print(f"Cleaned data saved to '{output_file_path}'.")


# # Automation

# In[59]:


pip install apscheduler


# In[60]:


# Schedule the scraping job to run every hour
scheduler = BackgroundScheduler()
scheduler.add_job(scrape_flipkart_camera_details, trigger=IntervalTrigger(hours=1))

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass


# In[61]:


import pandas as pd

# Specify the file path
file_path = 'Cleaned_Cameraflip.xlsx'

# Load data using Pandas
cleaned_data = pd.read_excel(file_path)

# Display the first few rows of the loaded data
cleaned_data.head()

