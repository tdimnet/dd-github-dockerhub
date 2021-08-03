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
            'url': 'http://foobar'
        })
    
    with pytest.raises(ConfigurationError):
        c.check({
            'search_string': 'foo'
        })
    
    c.check({
        'url': 'http://foobar',
        'search_string': 'foo'
    })
