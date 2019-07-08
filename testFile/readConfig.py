import os
import configparser
import sys

sys.path.append("./")
from testFile import getPathInfo

path = getPathInfo.get_Path()
config_path = os.path.join(path, "config.ini")
config = configparser.ConfigParser()
config.read(config_path, encoding="utf-8")


class readConfig:
    def get_http(self, name):
        value = config.get("HTTP", name)
        return value

    def get_email(self, name):
        value = config.get("EMAIL", name)
        return value

    def get_mysql(self, name):
        value = config.get("DATABASE", name)
        return value


if __name__ == "__main__":
    print("HTTP中的baseurl值为：", readConfig().get_http("baseurl"))
    print("EMAIL中的开关on_off值为：", readConfig().get_email("on_off"))
