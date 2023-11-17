import main, json, pytest, time

existing_long = "http://example.com/dir1/dir2"
existing_short = "http://example.org/AbCd7E"
new_long = "http://example.com/new/dir/for/testing"
new_short = "http://example.org/doesnotexist"

# To avoid getting rate limited we sleep between tests
@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1)

def test_generate_short_url():
    assert type(main.generate_short_url()) is str
    assert len(main.generate_short_url()) == len(main.short_url_domain) + main.short_url_length

def test_without_parameter():
    response = main.app.test_client().get('/encode')
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("error") == "Missing url parameter"
    assert response.status_code == 400
    response = main.app.test_client().get('/decode')
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("error") == "Missing url parameter"
    assert response.status_code == 400

def test_encode_with_existing():
    response = main.app.test_client().get('/encode?url=' + existing_long)
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("short") == existing_short

def test_decode_with_existing():
    response = main.app.test_client().get('/decode?url=' + existing_short)
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("long") == existing_long

def test_new_long():
    # Test encoding new long url
    response = main.app.test_client().get('/encode?url=' + new_long)
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))
    new_temp_short = json.loads(response.data.decode('utf-8')).get("short")
    assert len(new_temp_short) == len(main.short_url_domain) + main.short_url_length
    # And test decoding it
    response = main.app.test_client().get('/decode?url=' + new_temp_short)
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("long") == new_long

def test_new_short():
    response = main.app.test_client().get('/decode?url=' + new_short)
    assert response.status_code == 404
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("error") == "Could not find shortened url"
