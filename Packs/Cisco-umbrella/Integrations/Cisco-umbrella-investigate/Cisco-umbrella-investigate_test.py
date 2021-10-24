import demistomock as demisto
import importlib
from CommonServerPython import outputPaths, DBotScoreReliability

Cisco_umbrella_investigate = importlib.import_module('Cisco-umbrella-investigate')


def test_reliability_in_get_domain_security_command(mocker):
    """
        Given:
            - The user reliability param
        When:
            - Running get_domain_security_command
        Then:
            - Verify reliability as excepted
    """
    params = {
        'APIToken': '12345678',
        'baseURL': 'https://test.com',
        'integrationReliability': DBotScoreReliability.B
    }

    mocker.patch.object(demisto, 'params', return_value=params)
    mocker.patch.object(demisto, 'args', return_value={'domain': 'test.com'})
    mocker.patch.object(Cisco_umbrella_investigate, 'http_request')

    results = Cisco_umbrella_investigate.get_domain_security_command()

    assert results[0]['EntryContext'][outputPaths['dbotscore']]['Reliability'] == 'B - Usually reliable'
