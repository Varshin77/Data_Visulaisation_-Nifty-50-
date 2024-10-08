

import pandas as pd


csv_files = ['/content/NIFTY 100-01-06-2019-to-01-06-2020.csv', '/content/NIFTY 100-02-06-2020-to-01-06-2021.csv', '/content/NIFTY 100-02-06-2021-to-01-06-2022.csv', '/content/NIFTY 100-02-06-2022-to-01-06-2023.csv','/content/NIFTY 100-02-06-2023-to-01-06-2024.csv']


df = pd.DataFrame()

for file in csv_files:
    df_file = pd.read_csv(file)
    df = pd.concat([df, df_file], ignore_index=True)

df.to_csv('Nifty100.csv', index=False)

from google.colab import files
files.download('Nifty100.csv')

csv_files = ['/content/NIFTY 500-01-06-2019-to-01-06-2020.csv', '/content/NIFTY 500-02-06-2020-to-01-06-2021.csv', '/content/NIFTY 500-02-06-2021-to-01-06-2022.csv', '/content/NIFTY 500-02-06-2022-to-01-06-2023.csv','/content/NIFTY 500-02-06-2023-to-01-06-2024.csv']

df = pd.DataFrame()

for file in csv_files:
    df_file = pd.read_csv(file)
    df = pd.concat([df, df_file], ignore_index=True)

df.to_csv('Nifty500.csv', index=False)

from google.colab import files
files.download('Nifty500.csv')

csv_files = ['/content/NIFTY AUTO-01-06-2019-to-01-06-2020.csv', '/content/NIFTY AUTO-02-06-2020-to-01-06-2021.csv', '/content/NIFTY AUTO-02-06-2021-to-01-06-2022.csv', '/content/NIFTY AUTO-02-06-2022-to-01-06-2023.csv','/content/NIFTY AUTO-02-06-2023-to-01-06-2024.csv']

df = pd.DataFrame()

for file in csv_files:
    df_file = pd.read_csv(file)
    df = pd.concat([df, df_file], ignore_index=True)
df.to_csv('Nifty Auto.csv', index=False)

from google.colab import files
files.download('Nifty Auto.csv')

from google.colab import drive
drive.mount('/content/drive')

csv_files = ['/content/NIFTY BANK-01-06-2019-to-01-06-2020.csv', '/content/NIFTY BANK-02-06-2020-to-01-06-2021.csv', '/content/NIFTY BANK-02-06-2021-to-01-06-2022.csv', '/content/NIFTY BANK-02-06-2022-to-01-06-2023.csv','/content/NIFTY BANK-02-06-2023-to-01-06-2024.csv']

df = pd.DataFrame()
for file in csv_files:
    df_file = pd.read_csv(file)
    df = pd.concat([df, df_file], ignore_index=True)

df.to_csv('Nifty BANK.csv', index=False)

from google.colab import files
files.download('Nifty BANK.csv')

csv_files = ['/content/NIFTY FMCG-01-06-2019-to-01-06-2020.csv', '/content/NIFTY FMCG-02-06-2020-to-01-06-2021.csv', '/content/NIFTY FMCG-02-06-2021-to-01-06-2022.csv', '/content/NIFTY FMCG-02-06-2022-to-01-06-2023.csv','/content/NIFTY FMCG-02-06-2023-to-01-06-2024.csv']

df = pd.DataFrame()

for file in csv_files:
    df_file = pd.read_csv(file)
    df = pd.concat([df, df_file], ignore_index=True)

df.to_csv('Nifty FMCG.csv', index=False)

from google.colab import files
files.download('Nifty FMCG.csv')

csv_files = ['/content/NIFTY IT-01-06-2019-to-01-06-2020.csv', '/content/NIFTY IT-02-06-2020-to-01-06-2021.csv', '/content/NIFTY IT-02-06-2021-to-01-06-2022.csv', '/content/NIFTY IT-02-06-2022-to-01-06-2023.csv','/content/NIFTY IT-02-06-2023-to-01-06-2024.csv']

df = pd.DataFrame()
for file in csv_files:
    df_file = pd.read_csv(file)
    df = pd.concat([df, df_file], ignore_index=True)

df.to_csv('Nifty IT.csv', index=False)

from google.colab import files
files.download('Nifty IT.csv')

csv_files = ['/content/NIFTY METAL-01-06-2019-to-01-06-2020.csv', '/content/NIFTY METAL-02-06-2020-to-01-06-2021.csv', '/content/NIFTY METAL-02-06-2021-to-01-06-2022.csv', '/content/NIFTY METAL-02-06-2022-to-01-06-2023.csv','/content/NIFTY METAL-02-06-2023-to-01-06-2024.csv']
df = pd.DataFrame()


for file in csv_files:
    df_file = pd.read_csv(file)
    df = pd.concat([df, df_file], ignore_index=True)

df.to_csv('Nifty METAL.csv', index=False)

from google.colab import files
files.download('Nifty METAL.csv')

csv_files = ['/content/NIFTY PHARMA-01-06-2019-to-01-06-2020.csv', '/content/NIFTY PHARMA-02-06-2020-to-01-06-2021.csv', '/content/NIFTY PHARMA-02-06-2021-to-01-06-2022.csv', '/content/NIFTY PHARMA-02-06-2022-to-01-06-2023.csv','/content/NIFTY PHARMA-02-06-2023-to-01-06-2024.csv']

df = pd.DataFrame()

for file in csv_files:
    df_file = pd.read_csv(file)
    df = pd.concat([df, df_file], ignore_index=True)

df.to_csv('Nifty PHARMA.csv', index=False)

from google.colab import files
files.download('Nifty PHARMA.csv')

nifty_50 = pd.read_csv('/content/Nifty50.csv')
nifty_50.head()

nifty_50.info()

nifty_50.isnull().sum()

nifty_50.fillna(method='ffill',inplace=True)

nifty_50.isnull().sum()

import numpy as np 
import pandas as pd 

!pip install chart_studio
import plotly.express as px
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot
import cufflinks
cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='pearl')

from datetime import datetime

nifty_50.columns

import matplotlib.pyplot as plt
import pandas as pd


file_path = '/content/Nifty50.csv'
nifty_50 = pd.read_csv(file_path)

nifty_50['Date '] = pd.to_datetime(nifty_50['Date '])


plt.figure(figsize=(10, 6))
plt.plot(nifty_50['Date '], nifty_50['High '], label='High Price', color='blue', alpha=0.8)
plt.plot(nifty_50['Date '], nifty_50['Low '], label='Low Price', color='orange', alpha=0.8)


plt.title('NIFTY 50 High vs Low Trend')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()


plt.gca().set_facecolor('#faf2f2')  
plt.grid(True)


plt.xticks(rotation=45)


plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd


nifty_50 = pd.read_csv('/content/Nifty50.csv') 

nifty_50['Date '] = pd.to_datetime(nifty_50['Date '])

plt.figure(figsize=(12, 6))
plt.plot(nifty_50['Date '], nifty_50['Close '], label='Close Price', color='blue', alpha=0.8)


plt.title('NIFTY 50 Closing Trend')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()


plt.gca().set_facecolor('#faf2f2')  
plt.grid(True, linestyle='--', alpha=0.5)


plt.xticks(rotation=45)


plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

nifty_50 = pd.read_csv('/content/Nifty50.csv')

nifty_50.columns = nifty_50.columns.str.strip()

nifty_50['Date'] = pd.to_datetime(nifty_50['Date'])


np.random.seed(0)  
nifty_50['EPS'] = np.random.uniform(100, 200, len(nifty_50))
nifty_50['BVPS'] = np.random.uniform(300, 400, len(nifty_50))

# Calculate P/E and P/B ratios
nifty_50['P/E'] = nifty_50['Close'] / nifty_50['EPS']
nifty_50['P/B'] = nifty_50['Close'] / nifty_50['BVPS']

# Plotting the P/E and P/B ratios
plt.figure(figsize=(12, 6))

# Plot P/E Ratio
plt.plot(nifty_50['Date'], nifty_50['P/E'], label='P/E Ratio', color='green', alpha=0.8)

# Plot P/B Ratio
plt.plot(nifty_50['Date'], nifty_50['P/B'], label='P/B Ratio', color='orange', alpha=0.8)

# Adding title and labels
plt.title('P/E vs P/B Ratio')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

# Customizing the plot background color
plt.gca().set_facecolor('#faf2f2')  # Using hexadecimal color code
plt.grid(True, linestyle='--', alpha=0.5)

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()

nifty_50_2022 = nifty_50[nifty_50['Date'] >= '2022-01-01']
nifty_50_2022.head()

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from mpl_toolkits.mplot3d import Axes3D

# Load the data from the uploaded file
nifty_50 = pd.read_csv('/content/Nifty50.csv')

# Strip any leading/trailing whitespace from column names
nifty_50.columns = nifty_50.columns.str.strip()

# Convert 'Date' column to datetime
nifty_50['Date'] = pd.to_datetime(nifty_50['Date'])

# Select data for the year 2019
nifty_50_2019 = nifty_50[nifty_50['Date'].dt.year == 2019]

# Prepare data for candlestick chart
nifty_50_2019['Date'] = nifty_50_2019['Date'].map(mdates.date2num)

# Plotting the candlestick chart
fig, ax = plt.subplots(figsize=(12, 6))

# Define width of candlestick elements
width = 0.6
width2 = 0.1

# Define up and down prices
up = nifty_50_2019[nifty_50_2019['Close'] >= nifty_50_2019['Open']]
down = nifty_50_2019[nifty_50_2019['Close'] < nifty_50_2019['Open']]

col1 = 'green'
col2 = 'red'

# Plot up prices
ax.bar(up['Date'], up['Close'] - up['Open'], width, bottom=up['Open'], color=col1)
ax.bar(up['Date'], up['High'] - up['Close'], width2, bottom=up['Close'], color=col1)
ax.bar(up['Date'], up['Low'] - up['Open'], width2, bottom=up['Open'], color=col1)

# Plot down prices
ax.bar(down['Date'], down['Close'] - down['Open'], width, bottom=down['Open'], color=col2)
ax.bar(down['Date'], down['High'] - down['Open'], width2, bottom=down['Open'], color=col2)
ax.bar(down['Date'], down['Low'] - down['Close'], width2, bottom=down['Close'], color=col2)

# Formatting the date axis
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Adding title and labels
plt.title('NIFTY 50 Candlestick Chart - 2019')
plt.xlabel('Date')
plt.ylabel('Price')

# Show plot
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Load the data from the uploaded file
nifty_50 = pd.read_csv('/content/Nifty50.csv')

# Strip any leading/trailing whitespace from column names
nifty_50.columns = nifty_50.columns.str.strip()

# Convert 'Date' column to datetime
nifty_50['Date'] = pd.to_datetime(nifty_50['Date'])

# Select data for the year 2019
nifty_50_2019 = nifty_50[nifty_50['Date'].dt.year >= 2019]

# Plotting the closing price
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(nifty_50_2019['Date'], nifty_50_2019['Close'], label='Close Price', color='blue')

# Highlight specific dates with vertical lines and add annotations
highlight_dates = {
    '2020-03-23': 'Lockdown Phase-1 announced',
    '2019-09-03': 'Multiple PSU Bank Merger Announcements',
    '2020-02-01': 'Union Budget, coronavirus pandemic',
    '2020-03-12': 'Coronavirus declared Pandemic by WHO'
}

for date, annotation in highlight_dates.items():
    ax.axvline(pd.to_datetime(date), color='red', linewidth=2, alpha=0.3)
    ax.text(pd.to_datetime(date), 0.95, annotation, transform=ax.get_xaxis_transform(),
            ha='left' if 'Lockdown' in annotation or 'Multiple' in annotation else 'right',
            color='red', fontsize=8)

# Formatting the date axis
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Adding title and labels
plt.title('NIFTY 50: Major Single Day Falls - 2019 Onwards')
plt.xlabel('Date')
plt.ylabel('NIFTY 50 Stock')

# Customizing the plot background color
#ax.set_facecolor('rgb(250, 242, 242)')
#ax.grid(True, linestyle='--', alpha=0.5)

# Show plot
plt.tight_layout()
plt.show()

nifty_auto = pd.read_csv('/content/Nifty Auto.csv')
nifty_bank = pd.read_csv('/content/Nifty BANK.csv')
nifty_fmcg = pd.read_csv('/content/Nifty FMCG.csv')
nifty_IT = pd.read_csv('/content/Nifty IT.csv')
nifty_metal = pd.read_csv('/content/Nifty METAL.csv')
nifty_pharma = pd.read_csv('/content/Nifty PHARMA.csv')


#Fill in missing values
nifty_auto.fillna(method='ffill',inplace=True)
nifty_bank.fillna(method='ffill',inplace=True)
nifty_fmcg.fillna(method='ffill',inplace=True)
nifty_IT.fillna(method='ffill',inplace=True)
nifty_metal.fillna(method='ffill',inplace=True)
nifty_pharma.fillna(method='ffill',inplace=True)

nifty_auto_2022 = nifty_auto[nifty_auto['Date '] > '2022-12-31']
nifty_bank_2022 = nifty_bank[nifty_bank['Date '] > '2022-12-31']
nifty_fmcg_2022 = nifty_fmcg[nifty_fmcg['Date '] > '2022-12-31']
nifty_IT_2022 = nifty_IT[nifty_IT['Date '] > '2022-12-31']
nifty_metal_2022 = nifty_metal[nifty_metal['Date '] > '2022-12-31']
nifty_pharma_2022= nifty_pharma[nifty_pharma['Date '] > '2022-12-31']

d = {'NIFTY Auto index': nifty_auto_2022['Close '].values,
     'NIFTY Bank index': nifty_bank_2022['Close '].values,
     'NIFTY FMCG index': nifty_fmcg_2022['Close '].values,
     'NIFTY IT index': nifty_IT_2022['Close '].values,
     'NIFTY Metal index': nifty_metal_2022['Close '].values,
     'NIFTY Pharma index': nifty_pharma_2022['Close '].values,
     }

df = pd.DataFrame(data=d)
df.index=nifty_auto_2022['Date ']
df.head()

import matplotlib.pyplot as plt

# Create a box plot using Matplotlib
df.plot(kind='box')

# Display the plot
plt.show()

import matplotlib.pyplot as plt

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=len(df.columns[:2]), figsize=(15, 5))

# Plot each column in a separate subplot
for i, col in enumerate(df.columns[:2]):
    df[col].plot(ax=axes[i], kind='line')
    axes[i].set_title(col)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()

import matplotlib.pyplot as plt

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=len(df.columns[3:]), figsize=(15, 5))

# Plot each column in a separate subplot
for i, col in enumerate(df.columns[3:]):
    df[col].plot(ax=axes[i], kind='line')
    axes[i].set_title(col)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()

import matplotlib.pyplot as plt

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
df.plot(ax=ax)

# Add horizontal lines
ax.axhline(y=2, color='r', linestyle='--')
ax.axhline(y=4, color='r', linestyle='--')

# Add vertical line
ax.axvline(x='2020-03-23', color='b', linestyle='--')

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Assuming df is your DataFrame
df_a = df['NIFTY Pharma index']
max_val = df_a.max()
min_val = df_a.min()
max_date = df_a[df_a == max_val].index[0]
min_date = df_a[df_a == min_val].index[0]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
df_a.plot(ax=ax)

# Add the line
ax.plot([max_date, min_date], [max_val, min_val], color='blue', linewidth=2)

# Add the rectangle
ax.fill_betweenx([min_val, max_val], max_date, min_date, color='gray', alpha=0.3)

# Display the plot
plt.show()
