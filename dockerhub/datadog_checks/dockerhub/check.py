import requests
import os

from datadog_checks.base import AgentCheck, ConfigurationError


USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')


class DockerhubCheck(AgentCheck):
    def get_authentication_header(self):
        r = requests.post(
            "https://hub.docker.com/v2/users/login",
            data={
                "username": USERNAME,
                "password": PASSWORD
            }
        )

        if r.status_code == 200:
            token = r.json()["token"]

            if token is not None:
                return {"Authorization": "Bearer {}".format(token)}
            else:
                raise ValueError("Something went wrong, not valid token")

    def get_repository_image_statistics(self, namespace, repository):
        r = requests.get(
            f'https://hub.docker.com/v2/namespaces/{namespace}/repositories/{repository}/images-summary',
            headers=self.get_authentication_header()
        )

        if r.status_code == 200:
            try:
                return r.json()["statistics"]
            except Exception as e:
                raise ValueError('unabled to retrieve image summary')

    def check(self, instance):
        namespace = instance.get('namespace')
        repository = instance.get('repository')

        if not namespace or not repository:
            raise ConfigurationError('Configuration error, unable to find namespae or/and repository properties')

        statistics = self.get_repository_image_statistics(namespace, repository)

        self.gauge('dockerhub.totalInstances', statistics['total'], self.OK)
        # self.gauge('dockerhub.activeInstances', statistics['active'])
        # self.gauge('dockerhub.inactiveInstances', statistics['inactive'])

