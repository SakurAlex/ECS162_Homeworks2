import os
from app import app

def test_api_key_returns_key():
    # stub out environment API key
    os.environ['NYT_API_KEY'] = 'dummy_key'
    app.config['TESTING'] = True
    client = app.test_client()

    rv = client.get('/api/key')
    assert rv.status_code == 200
    payload = rv.get_json()
    assert payload.get('api_key') == 'dummy_key'