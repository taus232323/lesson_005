# -*- coding: utf-8 -*-
from pprint import pprint

import my_burger
# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# print(my_burger.bum1())
# print(my_burger.cheese())
# print(my_burger.rissole())
# print(my_burger.sauce())
# print(my_burger.tomatoes())
# print(my_burger.onion())
# print(my_burger.letucce())
# print(my_burger.sauce())
# print(my_burger.bum2())

receipt = [my_burger.bum1(), my_burger.cheese(), my_burger.rissole(), my_burger.sauce(),
           my_burger.tomatoes(), my_burger.onion(), my_burger.letucce(), my_burger.sauce(), my_burger.bum2()]

pprint(receipt)
