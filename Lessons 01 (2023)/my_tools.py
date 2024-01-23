import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot


def find_important_values(data, names=None):
    if not any(isinstance(i, list) for i in data) and not isinstance(data, pd.DataFrame):
        data = [data]
    for i_data, sub_data in enumerate(data):
        if isinstance(data, pd.DataFrame):
            sub_data = data[sub_data]
        if names is not None:
            print(f'Label = ' + str(names[i_data]))
        print('max = ' + str(max(sub_data)))
        print(f'min = {min(sub_data)}')
        print('avg =', statistics.mean(sub_data))
        print()


def plot_graph(data, names=None, x_axis=None, title=None, labels=None):
    if not any(isinstance(i, list) for i in data):
        data = [data]
    if names is None:
        names = [f"Plot number {i}" for i in range(1, len(data) + 1)]
    elif not any(isinstance(i, list) for i in data):
        names = [names]
    for d, n in zip(data, names):
        if x_axis is None:
            plot.plot(d, label=n)
        else:
            plot.plot(x_axis, d, label=n)

    if title is None:
        plot.title('my_tools.plot')
    else:
        plot.title(title)
    if labels is not None:
        plot.xlabel(labels[0])
        plot.ylabel(labels[1])
    plot.legend()
    plot.grid(True, which='both')
    plot.show()
