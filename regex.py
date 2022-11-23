import re   #imports regular expression module

with open ("EMUPage.txt", "r+", encoding = 'utf-8', errors = 'ignore') as f:
    contents = f.read()
    #print(contents[:100])
    #print(contents.find("love"))

pattern = re.compile(r'[\w._-]+@[\w]+\.[\w]{2,3}')
match = pattern.findall(contents)
print(match)
#print(set(match))



