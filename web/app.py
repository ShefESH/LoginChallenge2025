from flask import Flask
from flask import render_template, jsonify, make_response, redirect, request, session, render_template_string
from flask_bootstrap import Bootstrap
import random as rnd
from faker import Faker
from faker.providers import internet

app = Flask(__name__)
Bootstrap(app)
fake = Faker()

# no need for sqlite authentication, just store uname/password
#add alternative option to guess easy creds
uname = "admin"
pwd = "password"

app.secret_key = "pinrg8gns#arjg;/-]]"

app.config["JWT_SECRET_KEY"] = ";nod87b;/dfub6vaz.knib"
app.config['JWT_TOKEN_LOCATION'] = ['cookies']


@app.route("/")
def index():
    success = request.args.get("loginSuccessful")
    if success is not None and success.lower() == "true":
        return redirect(f"/users/{rnd.randint(1, 300)}")
    elif success is not None:
        return render_template('home.html', login="Failed")
    else:
        return render_template('home.html')

@app.route("/verify-login", methods=["POST"])
def verify_login():
    if request.form.get('username') == uname and request.form.get('password') == pwd:
        return redirect("/?loginSuccessful=True")
    else:
        return redirect("/?loginSuccessful=False")

    # resp = make_response(render_template("hungry.html"))
    # resp.set_cookie('is_admin', "false")
    # return resp

@app.route("/users/<int:user_id>")
def user_profile(user_id):
    """Render fake user profile with data consistent based on user_id"""
    if user_id != 1:
        Faker.seed(user_id)
        rnd.seed(user_id)

        user = {
            "name": fake.name(),
            "username": fake.user_name(),
            "profile_img": f"https://picsum.photos/seed/{user_id}/400/400",
            "bio": fake.text(),
            "website": fake.url(),
            "follow": {
                "ers" : rnd.randint(0, 2**8),
                "ing" : rnd.randint(0, 2**8)
            },
            "email": fake.safe_email(),
            "posts": {
                "1":  f"https://picsum.photos/seed/{user_id}/400/400",
                "2":  f"https://picsum.photos/seed/{user_id}/400/400",
                "3":  f"https://picsum.photos/seed/{user_id}/400/400",
                "4":  f"https://picsum.photos/seed/{user_id}/400/400",
                "5":  f"https://picsum.photos/seed/{user_id}/400/400",
            }
        }

        return render_template("user-profile.html", user=user)
    
    user = {
        "name": "Admin",
            "username": "Admin",
            "profile_img": "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y",
            "bio": "This is the admin user for ShefESH HTS",
            "follow": {
                "ers" : 0,
                "ing" : 0
            },
            "email": "admin@shefesh.com",
    }

    return render_template("user-profile.html", user=user, is_admin=True)


@app.route("/admin-console")
def admin_console():
    is_admin = request.cookies.get('is_admin')
    if is_admin is None:
        is_admin = "false"
        resp = make_response(redirect(request.url))
        resp.set_cookie('is_admin', 'false')
        return resp

    if is_admin == "true":
        welcome = "Congratulations! You hacked this site!"
        return render_template("admin-console.html", welcome_msg=welcome, win=True)
    else:
        msg = "Error: only admins are allowed to access the admin console."
        welcome = render_template_string(msg)
        return render_template("admin-console.html", welcome_msg=welcome)

@app.route("/cleanup")
def cleanup():
    """clear cookies and any temp variables"""
    resp = make_response(redirect('/'))
    resp.set_cookie('access_token_cookie', '', expires=0)
    resp.set_cookie('Authorization', '', expires=0)
    resp.set_cookie('is_admin', 'false')
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2346, debug=True)