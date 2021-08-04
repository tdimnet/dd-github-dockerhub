import requests

from datadog_checks.base import AgentCheck


class GithubProjectsCheck(AgentCheck):
    def get_projects_cards(self, column_id, access_token):
        r = requests.get(
            f'https://api.github.com/projects/columns/{column_id}/cards?access_token={access_token}',
            headers={"Accept": "application/vnd.github.inertia-preview+json"}
        )

        if r.status_code == 200:
            return len(r.json())

    def check(self, instance):
        access_token = self.init_config.get('access_token')
        columns = instance.get('columns')

        if columns is not None:
            for column in columns:
                number_of_cards = self.get_projects_cards(column['id'], access_token)

                self.gauge(f'githubProjects.{column["name"]}', number_of_cards, tags=['TAG_KEY:TAG_VALUE'] + self.instance.get('tags', []))
