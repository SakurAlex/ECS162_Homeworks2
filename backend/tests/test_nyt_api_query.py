import pytest
from app import app
from unittest.mock import patch

@patch('app.requests.get')
def test_nyt_api_url_uses_ucdavis_and_apikey(mock_get):
    mock_get.return_value.json.return_value = {'response': {'docs': []}}
    app.config['TESTING'] = True
    client = app.test_client()

    client.get('/api/ucdavis-news')
    called_url = mock_get.call_args[0][0]
    assert 'api-key=' in called_url
    assert 'q=%22UC%20Davis%22' in called_url