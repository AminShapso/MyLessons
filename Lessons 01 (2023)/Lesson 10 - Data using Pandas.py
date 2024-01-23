import pandas as pd
import my_tools as _MT


file_in = r'C:\Users\USER\Documents\Pycharm\Lessons23\Lesson 04.csv'
delimiter = ","

df = pd.read_csv(file_in, sep=delimiter)
df["Sin wave 2"] = df["Sin wave"] * 10
df = df.set_index("Time")
_MT.find_important_values(df, names=df.columns)
_MT.plot_graph(df, names=df.columns)
# plot.plot(df, label=df.columns)
# plot.legend()
# plot.show()
