import os
import json
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/rolemodels.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", rolemodels=data)


@app.route("/about/<rolemodel_name>")
def about_rolemodel(rolemodel_name):
    rolemodel = {}
    with open("data/rolemodels.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == rolemodel_name:
                rolemodel = obj
    return render_template("rolemodel.html", rolemodel=rolemodel)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
