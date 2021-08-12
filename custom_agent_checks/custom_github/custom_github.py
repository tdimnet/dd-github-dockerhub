import requests

from datadog_checks.base import AgentCheck


class GithubRepoCheck(AgentCheck):
    def get_pull_requests_list(self, access_token, username, repository):
        r = requests.get(
            f'https://api.github.com/repos/{username}/{repository}/pulls',
            headers={'Authorization': f'token {access_token}'}
        )

        if r.status_code == 200:
            return len(r.json())

    def get_issues_list(self, access_token, username, repository):
        r = requests.get(
            f'https://api.github.com/repos/{username}/{repository}/issues',
            headers={'Authorization': f'token {access_token}'}
        )

        if r.status_code == 200:
            return len(r.json())

    def check(self, instance):
        access_token = self.init_config.get('access_token')
        username = self.init_config.get('username')
        repository = self.init_config.get('repository')

        number_of_issues = self.get_issues_list(access_token, username, repository)
        number_of_pull_requests = self.get_pull_requests_list(access_token, username, repository)

        self.gauge('github.numberOfIssues', number_of_issues, tags=['TAG_KEY:TAG_VALUE'] + self.instance.get('tags', []))
        self.gauge('github.numberOfPR', number_of_pull_requests, tags=['TAG_KEY:TAG_VALUE'] + self.instance.get('tags', []))