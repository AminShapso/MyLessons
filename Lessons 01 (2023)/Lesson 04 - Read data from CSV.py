import my_tools
from my_tools import plot_graph as _P


file_in = r'C:\Users\USER\Documents\Pycharm\Lessons23\Lesson 04.csv'
delimiter = ","
break_if_error = True


def read_file(file_path):
    output_data = []
    with open(file_path, "r") as file:
        output_titles = file.readline().strip().split(delimiter)
        for t in output_titles:
            output_data.append([])
        for line_index, line in enumerate(file.readlines()):
            try:
                input = line.strip().split(delimiter)
                for i, l in enumerate(input):
                    output_data[i].append(float(l))
            except:
                print(f'ERROR! file_path = {file_path}, line_index = {line_index}: line = {line.strip()}')
                if break_if_error:
                    break
                else:
                    continue
    return output_data, output_titles


data, titles = read_file(file_in)
time, time_title = data[0], titles[0]
data = data[1:]
titles = titles[1:]

my_tools.find_important_values(data)
_P(data, names=titles, x_axis=time, title="Lesson 04: Waves", labels=[time_title, "Amplitude"])
