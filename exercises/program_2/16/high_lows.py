import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = input("csv filename: ")

#filename = 'kunming_2020-8-16_to_2021-8-16.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date_index = header_row.index('DATE') 
    high_index = header_row.index('TMAX') 
    low_index = header_row.index('TMIN') 
    name_index = header_row.index('NAME')
    avg_index = header_row.index('TAVG')
    
    dates, highs, lows, avgs = [], [], [], []
    for row in reader:
        place_name = row[name_index]
        current_date = datetime.strptime(row[date_index], '%Y/%m/%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            avg = int(row[avg_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            avgs.append(avg)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, avgs, c='purple', alpha=0.3)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = f"Daily high and low temperatures - 2020\n{place_name}, CHINA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.savefig(f"{place_name}'s temperatures.png", bbox_inches='tight')
