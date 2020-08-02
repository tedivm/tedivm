import yaml
import requests
from jinja2 import Template


def get_project_data():
    r = requests.get("https://raw.githubusercontent.com/tedivm/portfolio/master/_data/projects.yaml")
    return yaml.safe_load(r.text)


def pretty_print(data):
    print(yaml.dump(data, sort_keys=False))


def get_template(name):
    with open("templates/%s.md" % (name,)) as fp:
        template = Template(fp.read())
    return template




class PortfolioBuilder:

    def __init__(self, data):
        self.data = data
        self.columns = 3
        self.project_template = get_template('project')
        self.category_template = get_template('category')
        self.readme_template = get_template('readme')


    def get_project_element(self, project):
        return self.project_template.render(project=project)


    def get_project_grid(self, projects):
        output = "<table>\n\n"
        element = 0
        for project in projects:
            element += 1
            if element == 1:
                output += "<tr>\n\n"
            output += "<td valign=\"top\">\n"
            output += self.get_project_element(project) + "\n"
            output += "</td>\n\n"
            if element == self.columns:
                output += "</tr>\n"
                element = 0
        if element > 0:
            while element < self.columns:
                element += 1
                output += "<td> </td>\n"
                if element == self.columns:
                    output += "</tr>\n\n"
        output += "</table>\n"
        return output


    def get_category(self, category):
        project_grid = self.get_project_grid(category['projects'])
        return self.category_template.render(category=category, project_grid=project_grid)


    def get_portfolio(self):
        output = ""
        for category in self.data:
            output += self.get_category(category)
            output += "\n\n"
        return output


    def get_readme(self):
        portfolio = self.get_portfolio()
        return self.readme_template.render(portfolio=portfolio)




#pretty_print(get_project_data())
pb = PortfolioBuilder(get_project_data())
print(pb.get_readme())
