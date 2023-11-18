# URL Shortener
A simple url shortener. API consisting of two GET endpoints: /encode and /decode.
Input: takes required "url" string parameter for each endpoint.
Output: JSON object with "short" or "long" properties.
Stores urls in memory, so any restart erases all but one example url.

#### Sidenotes/Ideas
- Currently uses GET method, but can be expanded to POST and/or other methods as needed.
- Can be converted into a class and/or package if expanded further
- Logging can be customized more
- Redis or another data store can be added

## Requirements
- Python 3 (used 3.11)
- Pip (used 23.3.1)

## Usage
#### Prod
1. Install dependencies: `make`
1. Then run the app `make run`
1. Query the api with `url` parameter to encode or decode:
    - http://127.0.0.1:8080/encode?url=http://example.com/dir1/dir2
    - http://127.0.0.1:8080/decode?url=http://example.org/AbCd7E

#### Dev
1. Install dependencies: `make install-dev`
1. Then run the app `make run-dev`
1. Query the api with `url` parameter to encode or decode:
    - http://127.0.0.1:5000/encode?url=http://example.com/dir1/dir2
    - http://127.0.0.1:5000/decode?url=http://example.org/AbCd7E

## Tests
1. Install dependencies: `make install-dev`
1. Run all tests with `make test`
1. Run pylint with `make lint`
1. Tests should also run on Github Actions automatically on every push
1. Lint also runs automatically on pre-commit git hook
