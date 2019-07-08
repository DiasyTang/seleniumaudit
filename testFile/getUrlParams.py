import sys

sys.path.append("./")
from testFile import readConfig

readConfig = readConfig.readConfig()


class getUrlParams:
    def get_Url(self):
        new_url = (
            readConfig.get_http("scheme")
            + "://"
            + readConfig.get_http("baseurl")
            + ":8888"
            + "/login"
            + "?"
        )
        return new_url


if __name__ == "__main__":
    print(getUrlParams().get_Url())
