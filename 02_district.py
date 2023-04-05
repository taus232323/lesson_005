# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as central_room1
from district.central_street.house1.room2 import folks as central_room2
from district.soviet_street.house1.room1 import folks as soviet_room1
from district.soviet_street.house1.room2 import folks as soviet_room2

inhabitants = [str(central_room1), str(central_room2), str(soviet_room1), str(soviet_room2)]
inhabitants_str = ','.join(inhabitants)
print('На районе живут: ', inhabitants_str)
