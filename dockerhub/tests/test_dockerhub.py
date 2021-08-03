import pytest

from datadog_checks.base import ConfigurationError

from datadog_checks.dockerhub import DockerhubCheck


@pytest.mark.unit
def test_config():
    instance = {}
    c = DockerhubCheck('dockerhub', {}, [instance])

    with pytest.raises(ConfigurationError):
        c.check(instance)
    
    with pytest.raises(ConfigurationError):
        c.check({
            'namespace': 'tdimnet'
        })
    
    with pytest.raises(ConfigurationError):
        c.check({
            'repository': 'front-dd'
        })

