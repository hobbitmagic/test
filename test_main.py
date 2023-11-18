"""Tests for main.py"""

import json
import time
import pytest
import main

EXISTING_LONG = "http://example.com/dir1/dir2"
EXISTING_SHORT = "http://example.org/AbCd7E"
NEW_LONG = "http://example.com/new/dir/for/testing"
NEW_SHORT = "http://example.org/doesnotexist"

@pytest.fixture(autouse=True)
def slow_down_tests():
    """Pauses one second between tests to avoid getting rate limited"""
    yield
    time.sleep(1)

def test_generate_short_url():
    """Tests generation of new short url"""
    assert isinstance(main.generate_short_url(), str)
    assert len(main.generate_short_url()) == len(main.SHORT_URL_DOMAIN) + main.SHORT_URL_LENGTH

def test_without_parameter():
    """Tests error if required parameter is missing"""
    response = main.app.test_client().get('/encode')
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("error") == "Missing url parameter"
    assert response.status_code == 400
    response = main.app.test_client().get('/decode')
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("error") == "Missing url parameter"
    assert response.status_code == 400

def test_encode_with_existing():
    """Tests existing long url is reused and not overwritten"""
    response = main.app.test_client().get('/encode?url=' + EXISTING_LONG)
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("short") == EXISTING_SHORT

def test_decode_with_existing():
    """Tests existing short url is found and decoded properly"""
    response = main.app.test_client().get('/decode?url=' + EXISTING_SHORT)
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("long") == EXISTING_LONG

def test_new_long():
    """Tests encoding and encoding of a new url"""
    # Test encoding new long url
    response = main.app.test_client().get('/encode?url=' + NEW_LONG)
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8'))
    new_temp_short = json.loads(response.data.decode('utf-8')).get("short")
    assert len(new_temp_short) == len(main.SHORT_URL_DOMAIN) + main.SHORT_URL_LENGTH
    # And test decoding it
    response = main.app.test_client().get('/decode?url=' + new_temp_short)
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("long") == NEW_LONG

def test_new_short():
    """Tests error if unknown short url is passed"""
    response = main.app.test_client().get('/decode?url=' + NEW_SHORT)
    assert response.status_code == 404
    assert json.loads(response.data.decode('utf-8'))
    assert json.loads(response.data.decode('utf-8')).get("error") == "Could not find shortened url"
