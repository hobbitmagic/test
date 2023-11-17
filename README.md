# URL Shortener

A simple url shortener. API consisting of two GET endpoints: /encode and /decode.
Input: takes required "url" string parameter for each endpoint.
Output: JSON object with "short" or "long" properties.
Stores urls in memory, so cannot be scaled much, and any restart erases all but one example url.

#### Sidenote
Limited test to GET method, but can easily be expanded to POST and/or other methods as needed.
Also since this is only three functions, decided against creating a class.
If expanded further, recommend making a class and a module. For now manual tests, but considering automating them.
I would test the limiter a bit more to make sure it is working as desired. (2 requests per second limit is vague, it could be interpreted as per ip, or per endpoint, or per endpoint per ip)

## Requirements
- Python 3 (used 3.11)
- Pip (used 23.3.1)

## Usage
1. Install dependencies: `pip install -r requirements.txt`
1. Then run the app `flask --app main run`

## Tests
1. Encode existing example url "http://127.0.0.1:5000/encode?url=http://example.com/dir1/dir2"
1. Decode existing example url "http://127.0.0.1:5000/decode?url=http://example.org/AbCd7E"
1. Encode non-existing url "http://127.0.0.1:5000/encode?url=http://example.com/dir1/dir2"
1. Decode non-existing url "http://127.0.0.1:5000/decode?url=doesnotexist"
1. Encode error missing url "http://127.0.0.1:5000/encode"
1. Decode error missing url "http://127.0.0.1:5000/decode"
