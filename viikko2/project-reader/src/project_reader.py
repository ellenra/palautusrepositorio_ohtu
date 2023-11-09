import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        return Project("Test name", "Test description", [], [])
