import numpy as np
import matplotlib.pyplot as plot


# ##   True   or   False   ## #
continue_if_error = True
enable_plot = True
plot_sin_cos = 0    # 0 = both, 1 = sin, 2 = cos


time = np.arange(0, 10, 0.1)   # Get x values of the sine wave
data = []
data.append(np.sin(time) * 45.54643)
data.append(np.cos(time) * 45.54643)


loop_index = 0
for sub_data in data:
    print(f'This is loop number {loop_index}:')
    print('max = ' + str(max(sub_data)))
    print(f'min = {min(sub_data)}')
    print('avg =', sub_data.mean())
    print()
    loop_index += 1


if enable_plot:
    if plot_sin_cos == 0 or plot_sin_cos == 1:
        plot.plot(time, data[-2], label='Sin wave')   # Plot a sine wave using time and amplitude obtained for the sine wave
    if plot_sin_cos != 1:
        plot.plot(time, data[-1], label='Cos wave')   # Plot a sine wave using time and amplitude obtained for the sine wave
    plot.title('Lesson 01 - Waves')   # Give a title for the sine wave plot
    plot.xlabel('Time')   # Give x-axis label for the sine wave plot
    plot.ylabel('Amplitude')   # Give y-axis label for the sine wave plot
    plot.legend()
    plot.grid(True, which='both')
    plot.show()
