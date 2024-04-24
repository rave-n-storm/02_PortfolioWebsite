import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

GITHUB_USER = "rave-n-storm"

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    # access GitHub page of GITHUB_USER and get the list of their public repositories
    github_url = f"https://api.github.com/users/{GITHUB_USER}/repos"
    headers = {"accept": "application/vnd.github+json"}
    params = {"type": "owner",
              "sort": "full_name",
              "direction": "asc"}
    response = requests.get(url=github_url,
                            headers=headers,
                            params=params)
    response.raise_for_status()
    data = response.json()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
