import requests

from datadog_checks.base import AgentCheck, ConfigurationError


class DockerhubCheck(AgentCheck):
    def check(self, instance):
        url = instance.get('url')
        search_string = instance.get('search_string')

        if not url or not search_string:
            raise ConfigurationError('Configuration error, please fix dockerhub.yaml')
        

        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            self.service_check('dockerhub.search', self.CRITICAL, message=str(e))
        else:
            if search_string in response.text:
                self.service_check('dockerhub.search', self.OK)
            else:
                self.service_check('dockerhub.search', self.WARNING)
