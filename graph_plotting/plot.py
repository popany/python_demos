from datetime import datetime, timedelta, date
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.dates import DayLocator, HourLocator, MinuteLocator, DateFormatter
import numpy as np

def plotTwelve(axes, day):
    twelve = day + timedelta(hours=12)
    x = [twelve, twelve]
    y = [-1, 1]
    axes.plot_date(x, y, 'b-')
    axes.text(x[0], 0.7, 'twelve', fontsize=30)

def plot(day):

    s = np.arange(0.0, 100.0, 0.4)
    y = np.sin(0.1 * np.pi * s) * np.exp(-s * 0.01)
    x = np.arange(day, day + timedelta(days=1), timedelta(days=1)/len(y)).astype(datetime)
    
    fig= plt.figure(figsize=(40,5))
    axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])
    
    axes.yaxis.set_major_locator(MultipleLocator(0.2))
    axes.yaxis.set_major_formatter(FormatStrFormatter('%02f'))
    axes.yaxis.set_minor_locator(MultipleLocator(0.05))
    axes.set_ylim(-1, 1)
    
    axes.xaxis.set_major_locator(MinuteLocator(interval=30))
    axes.xaxis.set_minor_locator(MinuteLocator(interval=10))
    axes.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
    axes.xaxis.set_tick_params(rotation=30, labelsize=10)
    axes.set_xlim(day, day + timedelta(days=1))
    
    fig.suptitle(day.strftime('%Y-%m-%d'), fontsize=40)
    plt.xlabel('time', fontsize=16)
    plt.ylabel('value', fontsize=16)

    plt.grid(True)

    fig.autofmt_xdate()
    
    plotTwelve(axes, day)
    
    axes.plot_date(x, y, 'ro')

    plt.show()

plot(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
