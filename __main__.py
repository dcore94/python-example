import configparser;
conf = configparser.ConfigParser()
conf.read("config.cfg")
print("Hello " + conf["default"]["name"])
