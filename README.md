# URL Shortener
A simple url shortener. API consisting of two GET endpoints: /encode and /decode.
Input: takes required "url" string parameter for each endpoint.
Output: JSON object with "short" or "long" properties.
Stores urls in memory, so any restart erases all but one example url.

#### Sidenote
Limited test to GET method, but can easily be expanded to POST and/or other methods as needed.
Also since this is only three functions, decided against creating a class.
If expanded further, recommend making a class and a module.
I would test the limiter a bit more to make sure it is working as desired.
(2 requests per second limit is a bit vague, it could be interpreted as per ip, or per endpoint, or per endpoint per ip)

## Requirements
- Python 3 (used 3.11)
- Pip (used 23.3.1)

## Usage
1. Install dependencies: `pip install -r requirements.prod`
    - (or `pip install -r requirements.dev` for dev environment)
1. Then run the app `flask --app main run`
1. Query the api with `url` parameter to encode or decode:
    - http://127.0.0.1:5000/encode?url=http://example.com/dir1/dir2
    - http://127.0.0.1:5000/decode?url=http://example.org/AbCd7E

## Tests
1. Install dependencies: `pip install -r requirements.dev`
1. Run all tests with `pytest`
1. Run pylint with `pylint *.py`
1. Tests should also run on Github Actions automatically on every push to main branch
