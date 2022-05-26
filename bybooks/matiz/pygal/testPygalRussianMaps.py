import pygal.maps.ru

map = pygal.maps.ru.Regions()
map.add('Data', {'MOW': 10000})
map.render_to_file('test.svg')