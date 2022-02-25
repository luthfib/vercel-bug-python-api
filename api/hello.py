from flask import Flask, jsonify, _request_ctx_stack
from flask_cors import cross_origin


app = Flask(__name__)


@app.route("/<path:path>", methods=["GET", "POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
def nav_links(path=""):
    NAV_PAGES = ["Manage Registration", "Manage Users"]

    return jsonify({"data": NAV_PAGES})
