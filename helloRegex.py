import re

'''
s = 'stage.scaleMode = StageScaleMode.NO_SCALE'
match = re.search('(\w+)\.',s)
print(match.groups())
'''

s = 'panelClass = ProfilePanel   ;'
match = re.search('=\s*(?P<clazz>\w+)\W*',s)
print(match['clazz'])
