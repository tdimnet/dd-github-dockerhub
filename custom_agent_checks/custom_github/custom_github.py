import requests
import os

from datadog_checks.base import AgentCheck


ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')


class GithubRepoCheck(AgentCheck):
    def get_pull_requests_list(self):
        r = requests.get(f'https://api.github.com/repos/tdimnet/front-dd/pulls?access_token={ACCESS_TOKEN}')

        if r.status_code == 200:
            return len(r.json())

    def get_issues_list(self):
        r = requests.get(f'https://api.github.com/repos/tdimnet/front-dd/issues?access_token={ACCESS_TOKEN}')

        if r.status_code == 200:
            return len(r.json())

    def check(self, instance):
        number_of_issues = self.get_issues_list()
        number_of_pull_requests = self.get_pull_requests_list()

        self.gauge('github.numberOfIssues', number_of_issues, tags=['TAG_KEY:TAG_VALUE'] + self.instance.get('tags', []))
        self.gauge('github.numberOfPR', number_of_pull_requests, tags=['TAG_KEY:TAG_VALUE'] + self.instance.get('tags', []))
