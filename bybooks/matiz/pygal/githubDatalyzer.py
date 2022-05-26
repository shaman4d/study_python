import requests
import pygal

from pygal.style import LightColorizedStyle, LightenStyle

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
# print('Status code:', r.status_code)

responce_dict = r.json()

# print('Total repositories:', responce_dict['total_count'])

repo_dicts=responce_dict['items']

'''
names, stars = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])
	'''
	
names, plot_dicts = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict = {
		'value':repo_dict['stargazers_count'],
		'label':str(repo_dict['description']),
		'xlink':repo_dict['html_url']
	}
	plot_dicts.append(plot_dict)

my_style = LightenStyle('#333366', base_style=LightColorizedStyle)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
# chart.add('', stars)
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
