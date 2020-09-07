from jinja2 import Template;
import configparser;

conf = configparser.ConfigParser()
conf.read("config.cfg")

t = Template("Ciao {{ who }}!")
s = t.render(who=conf["default"]["name"])
print(s)
