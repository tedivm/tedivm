import os
import sys
import urllib
from unicodedata import category

import requests
import yaml
from github import Github
from jinja2 import Template

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
gh = Github(GITHUB_TOKEN)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_project_data():
    r = requests.get("https://raw.githubusercontent.com/tedivm/portfolio/master/_data/projects.yaml")
    return yaml.safe_load(r.text)


def get_avert_data():
    with open("adverts.yaml") as fp:
        return yaml.safe_load(fp.read())

def get_repo_commit_count(project):
    """
    Return the number of commits to a project
    Source: https://stackoverflow.com/a/55873469/212774
    """
    url = f'https://api.github.com/repos/{project}/commits'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'token {GITHUB_TOKEN}',
    }
    params = {'per_page': 1}
    resp = requests.request('GET', url, params=params, headers=headers)
    if (resp.status_code // 100) != 2:
        raise Exception(f'invalid github response: {resp.content}')
    # check the resp count, just in case there are 0 commits
    commit_count = len(resp.json())
    last_page = resp.links.get('last')
    # if there are no more pages, the count must be 0 or 1
    if last_page:
        # extract the query string from the last page url
        qs = urllib.parse.urlparse(last_page['url']).query
        # extract the page number from the query string
        commit_count = int(dict(urllib.parse.parse_qsl(qs))['page'])
    return commit_count

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
        self.project_template = get_template("project")
        self.projectnav_template = get_template("projectnav")
        self.category_template = get_template("category")
        self.readme_template = get_template("readme")
        self.adverts = get_avert_data()
        self.adverts_index = 0

    def get_stats(self):
        stats = {
            "repositories": 0,
            "forks": 0,
            "watchers": 0,
            "stargazers": 0,
            "commits": 0
        }

        for category in self.data:
            for project in category['projects']:
                if not 'github' in project:
                    continue
                eprint(f"Getting stats for {project['github']}")
                repo = gh.get_repo(project['github'])
                stats['forks'] += repo.forks_count
                stats['watchers'] += repo.subscribers_count
                stats['stargazers'] += repo.stargazers_count
                stats['commits'] += get_repo_commit_count(project['github'])
                stats['repositories'] += 1

        return stats

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

        for project in category["projects"]:
            element += 1
            if element == 1:
                header_row = "<thead><tr>\n\n"
                description_row = "<tr>\n\n"
                nav_row = "<tr>\n\n"

            header_row += '<th valign="top">\n'
            header_row += project["name"] + "\n"
            header_row += "</th>\n\n"

            description_row += '<td valign="top">\n'
            description_row += self.get_project_description(category, project) + "\n"
            description_row += "</td>\n\n"

            nav_row += '<td valign="top">\n'
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

                header_row += '<th valign="top">\n'
                header_row += "❤️" + advert["name"] + "❤️\n"
                header_row += "</th>\n\n"

                description_row += '<td valign="top">\n'
                description_row += self.get_project_description(category, advert) + "\n"
                description_row += "</td>\n\n"

                nav_row += '<td valign="top">\n'
                nav_row += self.get_project_navigation(category, advert) + "\n"
                nav_row += "</td>\n\n"

                if element == self.columns:
                    header_row += "</tr></thead>\n"
                    description_row += "</tr>\n"
                    nav_row += "</tr>\n"
                    output += "<table>" + header_row + description_row + nav_row + "</table>"

        return output

    def get_project_list(self, category):
        output = ""
        for project in category["projects"]:
            github_url = f"https://github.com/{ project['github'] }"
            output += self.get_project_list_entry(project, category)
            # output += (
            #    f"* [{project['name']}]({github_url}) - {project['description']}\n"
            # )
        return output

    def get_project_list_entry(self, project, category):
        image_url = self.get_image_url(project)
        if not image_url:
            image_url = self.get_image_url(category)
        if image_url:
            image_markdown = f'<img src="{image_url}" alt="{project["name"]}" title="{project["name"]}" width="20"/>'
        else:
            image_markdown = ""

        github_url = f"https://github.com/{ project['github'] }"
        return f"* {image_markdown} [{project['name']}]({github_url}) - {project['description']}\n"

    def get_image_url(self, object):
        if "image" in object:
            return f"https://projects.tedivm.com/assets/images/projects/{ object['image'] }"
        if "image_url" in object:
            return object["image_url"]
        if "icon" in object:
            return f"https://raw.githubusercontent.com/tedivm/tedivm/main/images/{ object['icon'].replace('fab fa-', '').replace('fas fa-', '') }.png"
        return False

    def get_advert_project(self):
        current_index = self.adverts_index % len(self.adverts)
        self.adverts_index += 1
        return self.adverts[current_index]

    def get_category(self, category):
        if os.environ.get("PROJECT_FORMAT", "grid") == "grid":
            project_display = self.get_project_grid(category)
        else:
            project_display = self.get_project_list(category)

        return self.category_template.render(category=category, project_display=project_display)

    def get_portfolio(self):
        output = ""
        for category in self.data:
            output += self.get_category(category)
            output += "\n\n"
        return output

    def get_readme(self):
        portfolio = self.get_portfolio()
        stats = self.get_stats()
        return self.readme_template.render(portfolio=portfolio, stats=stats)


# pretty_print(get_project_data())
pb = PortfolioBuilder(get_project_data())
print(pb.get_readme())
