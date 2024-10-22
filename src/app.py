from flask import Flask, render_template, request
import json

app = Flask(__name__)

users = ""
posts = ""

with open("./data/users.json") as u:
  users = json.load(u)["users"]

with open("./data/posts.json") as p:
  posts = json.load(p)["posts"]

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/post")
def getPost():
  id = int(request.args.get('id'))

  post = {}

  # Get content of post
  for p in posts:
    if p["id"] == id:
      post = p
      break

  return render_template("post.html", post=post)

@app.route("/user")
def getUser():
  id = int(request.args.get('id'))

  user = {}

  # Get content of user
  for u in users:
    if u["id"] == id:
      user = u
      break

  return render_template("user.html", user=user)