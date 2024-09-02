# This is a sample Python script.
import random

import numpy as np
import matplotlib


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(matplotlib.matplotlib_fname())
    from matplotlib.font_manager import findSystemFonts, FontProperties

    for font in findSystemFonts(fontpaths=None, fontext='ttf'):
        print(FontProperties(fname=font).get_name())

    r = random.randrange(0,5)
    print(r)
    # 原始数据
    data = [30, 20, 30, 40, 50,6000]

    # 使用NumPy计算方差和标准差
    variance = np.var(data)
    std_deviation = np.std(data)

    # 计算标准化方差
    standardized_variance = (variance - np.mean(data)) / std_deviation

    print("原始数据的方差：", variance)
    print("原始数据的标准差：", std_deviation)
    print("标准化方差：", standardized_variance)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

