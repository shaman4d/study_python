import json
from country_codes import get_country_code
import pygal.maps.world
from pygal.style import RotateStyle, LightColorizedStyle

cc_pop2010 = {}
filename = 'data/population_data.json'
with open(filename) as f:
    pdata = json.load(f)
    for pop_dict in pdata:
        if pop_dict['Year'] == '2010':
            cname = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(cname)
            if code:
                cc_pop2010[code] = population
cc_group1, cc_group2, cc_group3 = {}, {}, {}

for cc,pop in cc_pop2010.items():
    if pop < 10000000:
        cc_group1[cc] = pop
    elif pop < 1000000000:
        cc_group2[cc] = pop
    else:
        cc_group3[cc] = pop

wm_style = RotateStyle('#336699',base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country (millions)'

'''
wm.add('2010', cc_pop2010)
wm.render_to_file('wp2010.svg')
'''
wm.add('0-10m', cc_group1)
wm.add('10m-1bn', cc_group2)
wm.add('>1bn', cc_group3)
wm.render_to_file('wp2010.svg')
