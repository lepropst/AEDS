from flask import Blueprint,request, render_template
import json
server_blueprint = Blueprint(import_name="server", name="server")




@server_blueprint.route("/login", methods=["GET", "POST"])
def get_login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        print(request.data)
        return request.form.get("password")


@server_blueprint.route("/logout", methods=["GET","POST"])
def logout():
    if request.method == "GET":
        return json.dumps({"username":'null', 'password':'null'})
    else:
        return f"post request sent {request.referrer}"

# @server_blueprint.route("/refresh_token", methods=["GET","POST"])
# def login():
#     if request.method == "GET":
#         return json.dumps({"username":'null', 'password':'null'})
#     else:
#         return f"post request sent {request.referrer}"

# @server_blueprint.route("/obtain_token", methods=["GET","POST"])
# def login():
#     if request.method == "GET":
#         return json.dumps({"username":'null', 'password':'null'})
#     else:
#         return f"post request sent {request.referrer}"

@server_blueprint.route("/callback", methods=["GET","POST"])
def cssallback():
    if request.method == "GET":
        return json.dumps({"username":'null', 'password':'null'})
    else:
        return f"post request sent {request.referrer}"
