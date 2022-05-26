import cssutils

weatherBackgrounds = {}
parsedCSS = cssutils.parseFile('tmp.css')
for rule in parsedCSS.cssRules:
	if rule.selectorText == '.fact__theme_day-clear:before':
		weatherBackgrounds['fact__theme_day-clear'] = rule.style.backgroundImage[4:-1]
	if rule.selectorText == '.fact__theme_day-partly:before':
		weatherBackgrounds['fact__theme_day-partly'] = rule.style.backgroundImage[4:-1]
	if rule.selectorText == '.fact__theme_day-cloudy:before':
		weatherBackgrounds['fact__theme_day-cloudy'] = rule.style.backgroundImage[4:-1]

	if rule.selectorText == '.fact__theme_dawn-clear:before':
		weatherBackgrounds['fact__theme_dawn-clear'] = rule.style.backgroundImage[4:-1]
	if rule.selectorText == '.fact__theme_dawn-partly:before':
		weatherBackgrounds['fact__theme_dawn-partly'] = rule.style.backgroundImage[4:-1]
	if rule.selectorText == '.fact__theme_dawn-cloudy:before':
		weatherBackgrounds['fact__theme_dawn-cloudy'] = rule.style.backgroundImage[4:-1]

	if rule.selectorText == '.fact__theme_night-clear:before':
		weatherBackgrounds['fact__theme_night-clear'] = rule.style.backgroundImage[4:-1]
	if rule.selectorText == '.fact__theme_night-partly:before':
		weatherBackgrounds['fact__theme_night-partly'] = rule.style.backgroundImage[4:-1]
	if rule.selectorText == '.fact__theme_night-cloudy:before':
		weatherBackgrounds['fact__theme_night-cloudy'] = rule.style.backgroundImage[4:-1]
