import toml
from urllib import request
from project import Project

class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        
    def _stringify_dependencies(self, dependencies):
        for i in dependencies:
            return "\n".join([' - ' + str(name) for name in i])
    
    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: \n{self._stringify_dependencies(self.authors)}"
            f"\n\nDependencies: \n{self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: \n{self._stringify_dependencies(self.dev_dependencies)}"
        )

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)
        
        name = data['tool']['poetry']['name']
        description = data['tool']['poetry']['description']
        dependencies = data['tool']['poetry']['dependencies']
        dev_dependencies = data['tool']['poetry']['group']['dev']['dependencies']
        authors = data['tool']['poetry']['authors']
        license = data['tool']['poetry']['license']
        

        return Project(name, description, license, [authors], [dependencies], [dev_dependencies])
