"""API authentication middleware."""
import functools
import os

API_KEY = os.environ.get("HYPERNOVA_API_KEY", "dev-key")

def require_auth(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("X-API-Key", "")
        if key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated
