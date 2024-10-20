
from app import app


def test_app_server_homepage():
    app.testing = True
    client = app.test_client()

    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data


def test_initial_results():
    app.testing = True
    client = app.test_client()

    response = client.get('/results')
    assert response.status_code == 200
    assert response.json['yes'] == 0
    assert response.json['no'] == 0


def test_can_post_vote():
    app.testing = True
    client = app.test_client()

    response = client.post('/vote', json={'vote': 'yes'})
    assert response.status_code == 200
    assert response.json['yes'] == 1
    assert response.json['no'] == 0


def test_bad_vote_message_body():
    app.testing = True
    client = app.test_client()

    response = client.post('/vote', json={})
    assert response.status_code == 400
    assert response.data == b'Invalid body'


def test_bad_vote_message_vote():
    app.testing = True
    client = app.test_client()

    response = client.post('/vote', json={'vote': 'void'})
    assert response.status_code == 400
    assert response.data == b'Invalid vote'