import yaml
import requests
from jinja2 import Template


def get_project_data():
    r = requests.get("https://raw.githubusercontent.com/tedivm/portfolio/master/_data/projects.yaml")
    return yaml.safe_load(r.text)


def get_avert_data():
    with open("adverts.yaml") as fp:
        return yaml.safe_load(fp.read())


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
        self.projectnav_template = get_template('projectnav')
        self.category_template = get_template('category')
        self.readme_template = get_template('readme')
        self.adverts = get_avert_data()
        self.adverts_index = 0


    def get_project_description(self, category, project):
        return self.project_template.render(project=project, category=category)


    def get_project_navigation(self, category, project):
        return self.projectnav_template.render(project=project, category=category)


    def get_project_grid(self, category):
        output = ""
        element = 0

        header_row = ""
        description_row = ""
        nav_row = ""

        for project in category['projects']:
            element += 1
            if element == 1:
                header_row = "<thead><tr>\n\n"
                description_row = "<tr>\n\n"
                nav_row = "<tr>\n\n"

            header_row += "<th valign=\"top\">\n"
            header_row += project['name'] + "\n"
            header_row += "</th>\n\n"

            description_row += "<td valign=\"top\">\n"
            description_row += self.get_project_description(category, project) + "\n"
            description_row += "</td>\n\n"

            nav_row += "<td valign=\"top\">\n"
            nav_row += self.get_project_navigation(category, project) + "\n"
            nav_row += "</td>\n\n"


            if element == self.columns:
                header_row += "</tr></thead>\n"
                description_row += "</tr>\n"
                nav_row += "</tr>\n"
                output += "<table>" + header_row + description_row + nav_row + "</table>"
                element = 0
        #
        #
        # if element > 0:
        #     header_row += "</tr></thead>\n"
        #     description_row += "</tr>\n"
        #     nav_row += "</tr>\n"
        #     output += "<table>" + header_row + description_row + nav_row + "</table>"
        #     element = 0



        if element > 0:
            while element < self.columns:
                element += 1

                advert = self.get_advert_project()

                header_row += "<th valign=\"top\">\n"
                header_row += "❤️" + advert['name'] + "❤️\n"
                header_row += "</th>\n\n"

                description_row += "<td valign=\"top\">\n"
                description_row += self.get_project_description(category, advert) + "\n"
                description_row += "</td>\n\n"

                nav_row += "<td valign=\"top\">\n"
                nav_row += self.get_project_navigation(category, advert) + "\n"
                nav_row += "</td>\n\n"

                if element == self.columns:
                    header_row += "</tr></thead>\n"
                    description_row += "</tr>\n"
                    nav_row += "</tr>\n"
                    output += "<table>" + header_row + description_row + nav_row + "</table>"

        return output


    def get_advert_project(self):
        current_index = self.adverts_index % len(self.adverts)
        self.adverts_index += 1
        return self.adverts[current_index]


    def get_category(self, category):
        project_grid = self.get_project_grid(category)
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
