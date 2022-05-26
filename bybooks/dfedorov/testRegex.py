import re

str = 'content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl/ContentServiceSqlOracle.java'
match = re.search('(?P<email>\w+[\.*\w*]*@\w+[\.*\w*]*)', str)
if match is not None:
    print(match['email'])
