from flask import Flask, request, url_for

from src.server.router import server_blueprint
from src.encryption.router import encryption_blueprint

app = Flask(__name__)

# Load the first router from the `/api` subfolder.
api_router = app.register_blueprint(
    import_name="encryption", blueprint=encryption_blueprint, url_prefix="/encryption"
)
# Load the second router from the `/admin` subfolder.
admin_router = app.register_blueprint(
    import_name="server",blueprint=server_blueprint, url_prefix="/"
)



def graceful_shutdown_handler(signum, frame):
    app.logger.info("Gracefully shutting down...")
    app.stop()

def get_all_endpoints():
    endpoints = []
    for rule in app.url_map.iter_rules():
        if not rule.arguments:
            url = url_for(rule.endpoint)
            endpoints.append(url)
    return endpoints

# Get all endpoints and print them


# Implement a signal for reloading the application.
@app.route("/reload", methods=['POST'])
def reload():
    if request.method == "POST":
        app.logger.info("Reloading application...")
        app.run()
    else:
        return "Invalid request."

@app.route("/")
def catch_all():
    app.logger.info("Caught random route")
    return get_all_endpoints()
