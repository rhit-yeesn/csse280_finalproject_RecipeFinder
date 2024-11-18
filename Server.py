
# Resources:
# https://stackoverflow.com/questions/78352966/react-js-api-calls-using-axios
# https://forum.freecodecamp.org/t/jsx-js-and-html/489239/4
# https://legacy.reactjs.org/docs/introducing-jsx.html
# https://stackoverflow.com/questions/48414834/installing-babel-to-use-with-react-and-jsx
# https://stackoverflow.com/questions/5640916/set-a-forms-action-attribute-when-submitting
# https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
# https://stackoverflow.com/questions/62851874/passing-variables-between-pages-using-localstorage-and-passing-variables-in-a-li
# https://wiki.smartsimple.com/wiki/Passing_Values_Using_Parameters#:~:text=Values%20can%20be%20sent%20from,receiving%20page%20back%20into%20values.
# https://www.geeksforgeeks.org/flask-app-routing/#
# https://flask.palletsprojects.com/en/stable/quickstart/
# https://www.w3schools.com/html/html_form_input_types.asp
# https://stackoverflow.com/questions/8824831/make-div-stay-at-bottom-of-pages-content-all-the-time-even-when-there-are-scrol
# https://medium.com/codex/getting-started-with-axios-3d7836ab555e#:~:text=Writing%20a%20Get%20Request,you%20are%20requesting%20data%20from.
# https://www.w3schools.com/tags/att_script_src.asp
# https://www.themealdb.com/api.php
# https://stackoverflow.com/questions/70067751/usestate-and-usehooks-in-html
# https://stackoverflow.com/questions/54018182/how-to-make-script-type-both-text-babel-and-module
# https://codedamn.com/news/javascript/fix-require-is-not-defined
# https://stackoverflow.com/questions/38219311/reactjs-uncaught-referenceerror-require-is-not-defined
# https://the-meal-db-rex.netlify.app/home
# https://react.dev/learn/start-a-new-react-project
# https://flask.palletsprojects.com/en/stable/api/#flask.redirect
# https://flask-session.readthedocs.io/en/latest/introduction.html#client-side-vs-server-side-sessions
# ZyBooks
# Course Materials
# ChatGPT
# 


import os
import hashlib
from flask import Flask, flash, request, redirect, url_for, send_from_directory, Request, jsonify, Response, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import pickledb
from datetime import datetime

app = Flask(__name__, static_folder='public', static_url_path='')
app.secret_key = 'dev-key'



db = pickledb.load('users.db', True)
if not db.get('users'):
   db.dcreate('users')


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return jsonify({"error" : "Username and password are required and cannot be empty"}), 400

    hashed_password = generate_password_hash(password)

    if db.dexists('users', username):
        return jsonify({"error" : "User already exists"}), 400
    
    db.dadd('users', (username, {
        "password" : hashed_password,
        "saved_recipes" : []
        }))
    return jsonify({"message" : "User registered"}), 200

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({"error" : "Username and password are required and cannot be empty"}), 400

    if db.dexists('users', username):
        user_data = db.dget('users', username)
        stored_hashed_password = user_data.get("password")
        if(check_password_hash(stored_hashed_password, password)):
            session['username'] = username
            return jsonify({"message" : "Login successful"}), 200
        else:
            return jsonify({"error" : "Incorrect Password"}), 401
    else:
        return jsonify({"error" : "User not found"}), 404

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return send_from_directory(app.static_folder, 'Login.html')

@app.route('/check_login', methods=['GET'])
def check_login():
    if 'username' in session:
        return jsonify({"loggedIn" : True, "username" : session['username']})
    return jsonify({"loggedIn" : False})

@app.route("/Search", methods=['GET'])
def showSearch():
    return send_from_directory(app.static_folder, 'SearchResults.html')

@app.route('/Recipe', methods=['GET'])
def getRecipeAndDetails():
    return send_from_directory(app.static_folder, 'Recipe.html')
    
@app.route('/save-recipe', methods=['POST'])
def saveRecipe():
    if 'username' not in session:
        return jsonify({"error" : "not logged in"}), 401
    
    data = request.json
    meal_id = data.get("mealId")

    if not meal_id:
        return jsonify({"message" : "Missing recipe information"}), 400

    username = session['username']
    
    user_data = db.dget('users', username)
    if not user_data:
        return jsonify({"error" : "user not found"}), 404
    

    saved_recipes = user_data.get("saved_recipes", [])

    if meal_id not in saved_recipes:
        saved_recipes.append(meal_id)
    else:
        return jsonify({"message" : "Recipe already saved"}), 200

    user_data["saved_recipes"] = saved_recipes
    db.dadd('users', (username, user_data))

    return jsonify({"message" : "Recipe saved successfully"}), 200


@app.route('/Home', methods=['GET'])
def showHome():
    return send_from_directory(app.static_folder, 'Home.html')

@app.route('/Saved', methods=['GET'])
def showSaved():
    return send_from_directory(app.static_folder, 'Saved.html')

@app.route('/api/saved-recipes', methods=['GET'])
def get_saved_recipes():
    username = session.get('username')
    if not username:
        return jsonify({"error" : "User not logged in"}), 401
    
    user_data = db.dget('users', username)

    if not user_data:
        return jsonify({"error" : "User not found"}), 404
    
    saved_recipes = user_data.get("saved_recipes", [])

    return jsonify(saved_recipes)
    


@app.route('/')
def start():
    return send_from_directory(app.static_folder, 'Login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22029, debug=True)
