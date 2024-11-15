"""
    Create and plot graphs in windows console using plotly
    To use, enter line:
    from my_pyplot import omit_plot as _O, plot as _P, print_chrome as _PC, clear as _PP, print_lines as _PL

    Example:
    _P(df)
    i_col = 0
    _O(df.iloc[:, i_col])

    @author: Eddy Abzah
    @last update: 16/01/2024
"""


import plotly
import inspect
import pathlib
import smtplib
import pandas as pd
import plotly.graph_objects as go
from enum import Enum
from matplotlib import pyplot as plt
from plotly.subplots import make_subplots

label_prefix = 'Plot'
label_index = 1


def print_lines(df):
    for d in df:
        print(f'{d}')


def print_chrome(df, labels='', path='', file_name='', title='', auto_open=True):
    global label_index
    fig = make_subplots(rows=1, cols=1, shared_xaxes=False)
    if path == '':
        path = str(pathlib.Path().resolve())
    if file_name == '':
        file_name = f'print_chrome {label_index:03}.html'
    else:
        file_name = file_name + '.html'
    path = path + '\\' + file_name
    if title == '':
        title = f'print_chrome {label_index:03}'
    if isinstance(df, pd.DataFrame):
        if df.iloc[:, 0].diff().sum() + 1 == len(df):
            df = df.set_index(list(df.head(0))[0])
        for index, (info, trace) in enumerate(df.items()):
            fig.add_trace(go.Scatter(x=list(df.index), y=trace, name=info), col=1, row=1)
    else:
        if labels == '':
            if isinstance(df, pd.Series):
                labels = [df.name]
            else:
                labels = [f'Trace {n}' for n in range(len(df))]
        for index, (info, trace) in enumerate(zip(labels, df)):
            fig.add_trace(go.Scatter(y=trace, name=info), col=1, row=1)
    fig.update_layout(title=title, title_font_color="#407294", title_font_size=40, legend_title="Plots:")
    plotly.offline.plot(fig, config={'scrollZoom': True, 'editable': True}, filename=path, auto_open=auto_open)
    label_index = label_index + 1


def omit_plot(df, label=''):
    clear()
    plot(df, label)


def plot(df, label=''):
    global label_index
    if label == '':
        if isinstance(df, pd.DataFrame):
            label = list(df.head(0))
        elif isinstance(df, pd.Series):
            label = df.name
        else:
            try:
                callers_local_vars = inspect.currentframe().f_back.f_locals.items()
                label = [var_name for var_name, var_val in callers_local_vars if var_val is df][0]
            except (Exception,):
                label = 'unnamed'
    else:
        label = f'{label_prefix} {label_index:03} → {label}'
    plt.plot(df, label=label)
    # ## Place a legend above this subplot, expanding itself to fully use the given bounding box.
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    # ## Place a legend to the right of this smaller subplot.
    # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    label_index = label_index + 1


def clear():
    global label_index
    try:
        plt.cla()
    except (Exception,):
        pass
    finally:
        label_index = 1
