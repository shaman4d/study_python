from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	'''Returns for country its country 2-letters code for using in Pygal'''
	for code,name in COUNTRIES.items():
		if name == country_name:
			return code
	return None

if __name__ == '__main__':
	print(get_country_code('Andorra'))