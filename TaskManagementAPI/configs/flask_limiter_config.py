from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from TaskManagementAPI import app
from flask_limiter.errors import RateLimitExceeded
from TaskManagementAPI.constants.messages import RATE_LIMIT

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

@app.errorhandler(RateLimitExceeded)
def handle_rate_limit_exceeded(e):
    return {'Unsuccessful': RATE_LIMIT, 'message': str(e.description)}, 429



