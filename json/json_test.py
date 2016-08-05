import json

def readData(filepath):
	f = open(filepath, 'r')
	js = json.loads(f.read())
	f.close()
	return js

data = readData("test.json")
url = data['snapshot']['url']
print url