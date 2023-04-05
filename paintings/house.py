# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200, 600)
def wall():
    y2 = 100  # Верхний левый край кирпича. Равен 0 так как каждый цикл ряд должен подниматься
    row = 0  # Переменная для подсчёта циклов
    for y1 in range(100, 300, 20):  # Цикл для постройки кирпичей в высоту
        y2 += 20  # Поднимаем ряд кирпичей
        row += 1  # Кладём первый ряд кирпичей
        if row % 2 == 0:  # Условие. Если цикл нечётный, то сдвиг кирпичей. Если чётный - оставить на прежнем месте
            x2 = 300
            range_x = range(300, 700, 40)  # Диапазон выкладывания кирпичей для чётного ряда
        else:
            x2 = 280
            range_x = range(280, 660, 40)  # Диапазон выкладывания кирпичей для нечётного ряда
        for x1 in range_x:  # Кладём кирпичи в ширину
            x2 += 40
            sd.rectangle(left_bottom=sd.get_point(x1, y1), right_top=sd.get_point(x2, y2),
                         color=sd.COLOR_ORANGE, width=2)
            sd.rectangle(left_bottom=sd.get_point(280, 100), right_top=sd.get_point(700, 300),
                         color=sd.COLOR_ORANGE, width=2)
            if sd.user_want_exit():
                break
            sd.sleep(0.1)



def roof():
    point1 = sd.get_point(280, 300)
    point2 = sd.get_point(490, 400)
    point3 = sd.get_point(700, 300)
    sd.polygon([point1, point2, point3], color=sd.COLOR_DARK_RED, width=0)


sd.pause()

