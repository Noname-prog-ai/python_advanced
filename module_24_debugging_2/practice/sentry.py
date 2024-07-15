import sentry_sdk
from flask import Flask

sentry_sdk.init(
    dsn="https://e7980321894702a1b751d67adbca5550@o4507605909438464.ingest.de.sentry.io/4507605922021456",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    1/0  # raises an error
    return "<p>Hello, World!</p>"