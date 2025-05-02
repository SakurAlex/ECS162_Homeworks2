import pytest
from app import app
import requests

# Sample payloads for page 0 and page 1
PAGE0 = {'response': {'docs': ['a', 'b']}}
PAGE1 = {'response': {'docs': ['c']}}

@pytest.fixture
def client(monkeypatch):
    calls = []
    def fake_get(url):
        calls.append(url)
        class Dummy:
            def __init__(self, payload): self._payload = payload
            def json(self): return self._payload
        # Return PAGE1 if URL contains "&page=1" else PAGE0
        return Dummy(PAGE1 if 'page=1' in url else PAGE0)

    # Monkeypatch requests.get globally
    monkeypatch.setattr(requests, 'get', fake_get)
    app.config['TESTING'] = True
    client = app.test_client()
    client.calls = calls
    return client


def test_ucdavis_news_combines_docs_from_two_pages(client):
    rv = client.get('/api/ucdavis-news')
    assert rv.status_code == 200
    data = rv.get_json()
    docs = data['response']['docs']
    # docs should include entries from PAGE0 and PAGE1
    assert docs == ['a', 'b', 'c']
    # Ensure both endpoints called: default and page=1
    assert any('page=1' in url for url in client.calls)
    assert any('%22UC%20Davis%22' in url for url in client.calls)
