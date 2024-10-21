import requests
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def get_prices():
    URL = f'https://dataportal-api.nordpoolgroup.com/api/DayAheadPrices?date={(datetime.today() + pd.Timedelta(days = 1)).strftime("%Y-%m-%d")}&market=DayAhead&deliveryArea=AT,SE3&currency=SEK'
    
    response = requests.get(URL)
    data = response.json()
    
    entries = []

    for entry in data['multiAreaEntries']:
        entry_datetime = pd.to_datetime(f'{entry["deliveryStart"].split("T")[0]} {entry["deliveryStart"].split("T")[1][:-1]}')
        price = entry['entryPerArea']['SE3']
        entries.append({'datetime': entry_datetime, 'price': price})

    entries.append({'datetime': entries[-1]['datetime'] + pd.Timedelta(hours=1), 'price': entries[-1]['price']})
    return entries
    

def create_plot():
    df = pd.DataFrame(get_prices())
    df = df.set_index('datetime')

    plt.figure(figsize=(20, 10))
    plt.plot(df.index, df['price'], marker='o', linestyle='-', label='Price (SEK/MWh)')

    plt.title(f'Day Ahead Prices for SE3 on { df.index[0].strftime("%B") } {df.index[0].strftime("%d")} to {df.index[3].strftime("%B")} {df.index[3].strftime("%d %Y")}', fontsize=20)

    plt.xlabel('Time', fontsize=16)
    plt.ylabel('Price (SEK/MWh)', fontsize=16)

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Set major ticks every hour
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(nbins=20))  # Set major ticks on y-axis


    plt.axvline(x=df.index[2], color='gray', linestyle='--')

    plt.text(df.index[0] + pd.Timedelta(minutes=30), plt.ylim()[0], df.index[0].strftime('%Y-%m-%d'), verticalalignment='bottom', horizontalalignment='center', fontsize=12)

    plt.text(df.index[3] + pd.Timedelta(minutes=30), plt.ylim()[0], df.index[3].strftime('%Y-%m-%d'), verticalalignment='bottom', horizontalalignment='center', fontsize=12)

    plt.legend()

    plt.tight_layout()

    plt.style.use('tableau-colorblind10')

    plt.savefig('prices.png')