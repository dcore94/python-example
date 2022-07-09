from jinja2 import Template;
import configparser;

conf = configparser.ConfigParser()
conf.read("config.cfg")

t = Template("Ciao {{ who }}!")
s = t.render(who=conf["default"]["name"])

f = open("file.txt", "a")
f.write(s + "\n")

f = open("file.xml", "w")
f.write("<text>" + s + "</text>")

f = open("file.json", "w")
f.write('{ "text" : "' + s + '"}')

print(s)


