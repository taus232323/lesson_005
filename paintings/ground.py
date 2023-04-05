import simple_draw as sd
sd.resolution = (1200, 600)

def ground():
    sd.rectangle(left_bottom=sd.get_point(0, 0), right_top=sd.get_point(1200, 100), color=sd.COLOR_DARK_ORANGE,
                 width=0)


sd.pause()