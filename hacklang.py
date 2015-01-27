import re

valid_lang = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC'

lang_list = re.split(':\s*',valid_lang)

N = int(raw_input())

if N >= 1 and N <= 100:
	for i in range(0,N):
		line = raw_input()
		lang = re.split('\s+',line)
		api_id = int(lang[0])
		lang_name = lang[1]
		if api_id >= 10**4 and api_id <= 10**5 and lang_name in lang_list:
			print 'VALID'
		else:
			print 'INVALID'
		
