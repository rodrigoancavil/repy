import re

def get_tag_attr(tag):
	"""
	Returns a dictionary with {tag : [attrs]}
	"""
	result = {}
	list_of_tags = re.findall('\w+\s+\w+=["|\'].*["|\']|\w+',tag) 
	if len(list_of_tags) >= 1:
		tags = re.split('\s*',list_of_tags[0])
		key = tags[0]
		values = []
		for t in tags[1:]:
			attr = re.search('\w+(?=\=.*)',t)
			if attr != None:
				values.append(attr.group())
		
		result[key] = values
		return result

def print_output(list_of_attr):
	"""
	Print the results in the STDOUT
	"""
	for tag in sorted(list_of_attr):
		line_output = tag+':'
		for attr in l[tag]:
			line_output = line_output + attr + ','
		if line_output.endswith(','):
			print line_output[0:len(line_output)-1]
		else:
			print line_output

N = int(raw_input())

if N>=1 and N <=100:
	results = []
	for i in range(0,N):
		W = raw_input()
		fragment = re.split('<\s*/\w+\s*>',W)
		for f in filter(lambda x : len(x)>=1,fragment):
			fl = filter(lambda x:len(x)>=1,re.split('<',f))
			for tag in fl:
				t1 = re.findall('\w+\s+\w+=["|\'].*["|\']\s*/?\s*>|^/*\w+\s*/?\s*>',tag)
				if len(t1) >= 1:
					t2 = re.split('>',t1[0])
					res = get_tag_attr(filter(lambda x:len(x)>=1,t2)[0])
					results.append(res)
	l = {}
	for p in sorted(results):
		k = p.keys()[0]
		v1 = p.values()[0]
		if k in l.keys():
			v2 = l[k]
			l[k] = sorted(v1 + [x for x in v2 if x not in v1])
		else:
			l[k] = sorted(v1)
	print_output(l)
