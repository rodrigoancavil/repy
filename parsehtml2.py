import re

def find_attr(tag):
	attrs = re.findall('[a-zA-Z0-9\-_]+(?=\=)',tag)
	return attrs

c = re.compile('<([^/][a-zA-Z0-9\-_]*)(?:(\s*[a-zA-Z0-9\-_]+\s*)(=(?:\s*["|\']\s*[a-zA-Z0-9\-_\\.:/*\s*]+\s*["|\']))?\s*)*\s*/?>')

line_html = raw_input()

result = {}
for match in c.finditer(line_html):
	tag = match.group()
	tag_name = re.search('^<\s*([a-zA-Z0-9\-_]+)(?:\s*.*?)/?>',tag).group(1)
	result[tag_name] = sorted(find_attr(tag))

print result
