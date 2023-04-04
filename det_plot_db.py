import pyodbc
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from _utils.helpers import *


def plot_line(object_id, reduce_step):
    df = object_data(object_id).iloc[::reduce_step]
    print(df)

    # # Split the x and y coordinates into separate lists
    x = range(len(df[['DeltaTime']]))
    y = df[['DeltaTime']]

    plt.plot(x, y)

    # # Add labels and title
    plt.xlabel('Points')
    plt.ylabel('DeltaTime')
    plt.title('DeltaTime at Point')


# plot_line(10,20)
# plot_line(20,20)
# plot_line(30,20)


df = object_data(1).iloc[::1]

sns.kdeplot(data=df[['DeltaTime']], x='DeltaTime')

# Show plot
plt.show()
