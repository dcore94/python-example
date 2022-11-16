from jinja2 import Template;
import configparser;
import os;

conf = configparser.ConfigParser()
conf.read("config.cfg")

t = Template("Ciao {{ who }}!")
s = t.render(who=conf["default"]["name"])

f = open("file.txt", "a")
f.write(s + "\n")
for k in os.environ: 
	if k.startswith("ccp"):
		f.write("%s = %s\n" % (k,os.environ[k])) 

f = open("file.xml", "w")
f.write("<text>" + s + "</text>")

f = open("file.json", "w")
f.write('{ "text" : "' + s + '"}')

f = open("file.csv", "w")
f.writelines(["row,content\n","1,"+s])

d = os.mkdir("testdir")
f = open("testdir/file.csv", "w")
f.writelines(["row,content\n","1,"+s])

print(s)
