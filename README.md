# DC Virtual Tip Jar Random Sample
This is a simple way to randomly select a sample from the DC Virtual Tip Jar using Python.

## Background
This week, as D.C.'s bars and restaurants closed for on-site service due to coronavirus, [Ana Owens and her girlfriend Katie Gentsch](https://www.washingtonian.com/2020/03/17/how-to-help-struggling-restaurant-and-bar-workers-right-now/) created a "virtual tip jar" in a Google spreadsheet to enable giving directly to hospitality workers. As of 3/18/20 at 6:30 pm, over 2,100 people are listed.

This simple script using Python and Pandas allows you to take a random sample of five workers. You can also choose to sample just people with Venmo, just people with Paypal or Cash App, or just people without healthcare.

## Usage

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Import everything from the Google spreadsheet
url = 'https://docs.google.com/spreadsheets/d/1tz2uyhgy3MsBS68MHPzO8H455_879fqfIaRPyUUw3QE/htmlview?sle=true#gid=0'
response = requests.get(url)

# Find and parse the table
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all('table')

# Convert the HTML table to a dataframe
df1 = pd.read_html(str(table), header=0, flavor='html5lib')[0]
# df1.head()

# Clean up the dataframe
header = df1.iloc[2]
df2 = df1[4:]
df2.columns = header
df3 = df2.drop(columns=[3.0])
df4 = df3.dropna(axis='columns', how='all')
df4 = df4.reset_index(drop=True)
# df5 = df4.replace(np.nan, '', regex=True)
df4 = df4.rename_axis('#', axis='columns')
df4.head()

# Show a random sample of 5

df5 = df4.replace(np.nan, '', regex=True)
df5.sample(5)

# Only sample people with a Venmo

df6 = df4.dropna(subset=['Venmo'])
df6 = df6.replace(np.nan, '', regex=True)
df6.sample(5)

# Only sample people with a Paypal or Cash App

df7 = df4.dropna(subset=['Paypal or Cash App'])
df7 = df7.replace(np.nan, '', regex=True)
df7.sample(5)

# Only sample people with no healthcare

df8 = df4.loc[df4['Do you have healthcare?'] == 'No']
df8 = df8.replace(np.nan, '', regex=True)
df8.sample(5)
```
