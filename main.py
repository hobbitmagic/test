from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import string, random

# Options
short_url_length = 6
short_url_domain = "http://example.org/"

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["2 per second"],
    storage_uri="memory://",
)

memory_store = [
    {"long": "http://example.com/dir1/dir2", "short": "http://example.org/AbCd7E"}
]

# Short url generator
def generate_short_url():
    new_short_url = ''.join(random.choices(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits
        , k=short_url_length))
    # Check if exists, and generate another if it already does
    if next((item for item in memory_store if item["short"] == new_short_url), None):
        return generate_short_url()
    else:
        return short_url_domain + new_short_url


# Encode route
# Input Parameters:
#   url (string) (required) - long url user wants to encode
# Output: (json object) - short url {"short": "http://example.org/ABCDEF"}
@app.route("/encode", methods=['GET'])
def encode():
    passed_url = request.args.get('url', None)
    if (passed_url is None):
       return jsonify({"error": "Missing url parameter"})
    # Check for existing, and return existing if found. Otherwise create and save new.
    existing_match = next((item["short"] for item in memory_store if item["long"] == passed_url), None)
    if (existing_match):
        return jsonify({"short": existing_match})
    else:
        new_short_url = generate_short_url()
        memory_store.append({"long": passed_url, "short": new_short_url })
        return jsonify({"short": new_short_url })

# Decode route
# Input Parameters:
#   url (string) (required) - short url user wants to decode
# Output: (json object) - long url {"long": "http://example.com/dir1/dir2"}
@app.route("/decode", methods=['GET'])
def decode():
    passed_url = request.args.get('url', None)
    if (passed_url is None):
       return jsonify({"error": "Missing url parameter"})
    # Check for existing, and return existing if found. Otherwise error out.
    existing_match = next((item["long"] for item in memory_store if item["short"] == passed_url), None)
    if (existing_match):
        return jsonify({"long": existing_match})
    else:
        return jsonify({"error": "Could not find shortened url"})

# Run the Waitress server
from waitress import serve
serve(app, listen='*:5000')
