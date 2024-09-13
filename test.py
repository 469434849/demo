import matplotlib.font_manager as fm

fonts = fm.findSystemFonts()

for font in fonts:
    font_name = fm.FontProperties(fname=font).get_name()
    print(font_name)