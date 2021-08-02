import requests

from datadog_checks.base import AgentCheck


class GithubRepoCheck(AgentCheck):
    def get_issues_list(self):

        r = requests.get(f'https://api.github.com/repos/tdimnet/front-dd/issues')

        if r.status_code == 200:
            return len(r.json())

    def check(self, instance):
        number_of_issues = self.get_issues_list()

        self.gauge('github.numberOfIssues', number_of_issues, tags=['TAG_KEY:TAG_VALUE'] + self.instance.get('tags', []))

