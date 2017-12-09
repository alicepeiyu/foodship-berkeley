from flask import Flask, render_template, request, session, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import requests
import os
import json
import datetime

app = Flask(__name__, static_url_path="/static")
CORS(app)
app.config.update(
    SECRET_KEY = 'secret_foodship'
)
# =================== login =================== 
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, data):
        self.id = data[3]
        self.name = data[0]
        self.password = data[1]
        self.gender = data[2]
        self.email = data[3]
        self.major = data[4]
        self.pref1 = data[5]
        self.pref2 = data[6]
        self.pref3 = data[7]
        self.about = data[8]

@login_manager.user_loader
def load_user(user_id):
    data = {"email": user_id}
    result, info = query_api_user(data)
    if result:
        return User(info)
    else:
        return None

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("login.html", message="You've logged out.")

# =================== login =================== 

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/login',methods=['GET'])
def show_login():
    return render_template('login.html')

@app.route('/register',methods=['GET'])
def show_register():
    return render_template('register.html')

def query_api_user(data):
    '''
    returns:
        is_sucess, message (data if success)
    '''
    r = requests.post(
        "https://berkeley-foodship-api.herokuapp.com/getuser",
        json=data
    )
    # print('r.status code', r.status_code)
    message = r.json()
    info = message["message"]
    if info == 'success':
        return True, message["data"]
    else:
        return False, info

@app.route('/login', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = request.form.get("remember")
    is_remember = True if remember is not None else False
    data = {"email":email}
    result, info = query_api_user(data)
    if result:
        true_password = info[1]
        if password == true_password:
            user = User(info)
            login_user(user, remember=is_remember)
            return redirect(url_for('browse'))
        else:
            return render_template("login.html", message="Your password is not correct.")
    else:
        return render_template("login.html", message=info)

@app.route('/register', methods=["POST"])
def register():
    username = request.form.get("usr")
    password = request.form.get("password")
    gender = request.form.get("gender")
    major = request.form.get("major")
    email = request.form.get("email")
    pref1 = request.form.get("pref1")
    pref2 = request.form.get("pref2")
    pref3 = request.form.get("pref3")
    notes = request.form.get("notes")
    data = {
        "username": username,
        "password": password,
        "gender": gender,
        "major": major,
        "email": email,
        "pref1": pref1,
        "pref2": pref2,
        "pref3": pref3,
        "notes": notes
    }
    r = requests.post("https://berkeley-foodship-api.herokuapp.com/adduser", json=data)
    return redirect(url_for('show_login'))

@app.route('/browse',methods=['GET'])
@login_required
def browse():
    email = current_user.email
    para = {"email":email}
    r = requests.get("https://berkeley-foodship-api.herokuapp.com/browse",json=para)
    data = r.json()
    para2 = {"user":email}
    data2 = requests.get('https://berkeley-foodship-api.herokuapp.com/username',params=para2)
    info = data2.json()
    username = info['firstname']
    return render_template("browse.html",pic1=data["1"],pic2=data["2"],pic3=data["3"],pic4=data["4"],pic5=data["5"],user=username)

@app.route('/browse',methods=['POST'])
@login_required
def send_email():
    r=requests.get(url='https://berkeley-foodship.herokuapp.com/static/email.html')
    email_html=r.text
    email = current_user.email
    #retrieving current username
    para = {'user':email}
    data2 = requests.get('https://berkeley-foodship-api.herokuapp.com/username',params=para)
    info = data2.json()
    username = info['firstname']
    sequence = request.form.get("sequence")
    r = requests.get("https://berkeley-foodship-api.herokuapp.com/{}".format(sequence))
    data = r.json()
    email = data[0]      # email of dining starter
    starter = data[1]  # name of dining starter
    day = data[4]
    meal = data[5]
    # restaurant info
    restaurant = data[6]
    address = data[7]
    url = data[-2]
    image_url = data[-1]
    para2 = {'emai2':current_user.email,'username':username,'resto':restaurant}
    status_change = requests.post("https://berkeley-foodship-api.herokuapp.com/{}".format(sequence),json=para2)
    #send email
    if status_change.status_code == requests.codes.ok:

        from_email = "<postmaster@sandboxede1ea44faf74d1894b975b73169110e.mailgun.org>"
        to_email = current_user.email
        to_email1 = email

        content = email_html.format(username,starter,meal,day,url,image_url,restaurant,address)

        data = {
            'from': 'Foodship'+from_email,
            'to': to_email,
            'subject': "Foodship Paired",
            'html': content,
        }

        content2 = email_html.format(starter,username,meal,day,url,image_url,restaurant,address)

        data2 = {
            'from': 'Foodship'+from_email,
            'to': to_email1,
            'subject': "Foodship Paired",
            'html': content2,
        }

        auth = ("api", "key-6fb9192ef025cc28412f6f1a99e7b4ce")
        domain = "sandbox988190694510461691814d424bef6805.mailgun.org"
        r = requests.post(
            'https://api.mailgun.net/v3/{}/messages'.format(domain),
            auth=auth,
            data=data)

        r2 = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(domain),
        auth=auth,
        data=data2)
        return render_template("match.html",user=username)
    else:
        return render_template("fail.html",user=username)

@app.route('/own')
@login_required
def own():
    email = current_user.email
    para = {'user':email}
    data = requests.get('https://berkeley-foodship-api.herokuapp.com/username',params=para)
    info = data.json()
    username = info['firstname']
    return render_template("own.html",user=username)

@app.route('/history')
@login_required
def history():
    email = current_user.email
    para = {'user':email}
    data = requests.get('https://berkeley-foodship-api.herokuapp.com/history',params=para)
    if data.status_code == requests.codes.ok:
        history = data.json()
        data2 = requests.get('https://berkeley-foodship-api.herokuapp.com/username',params=para)
        info = data2.json()
        username = info['firstname']
        return render_template("history.html",notifications=history,user=username)
    else:
        return ("<h1>Error</h1>")

@app.route('/create',methods=['GET'])
@login_required
def getStaticInfo():
    email = current_user.email
    para = {'user':email}
    data = requests.get('https://berkeley-foodship-api.herokuapp.com/username',params=para)
    if data.status_code == requests.codes.ok:
        info = data.json()
        username = info['firstname']
    return render_template("create.html",user=username)

#receiving the request for finding a match
@app.route('/create',methods=['POST'])
@login_required
def getInfo():
    email = current_user.email
    para = {'user':email}
    data = requests.get('https://berkeley-foodship-api.herokuapp.com/username',params=para)
    info = data.json()
    username = info['firstname']
    cuisine = request.form.get("pref")
    date = request.form.get("date")
    day =""
    today = datetime.date.today()
    tomorrow = today+datetime.timedelta(days=1)
    if date=="Today":
        year = str(today.year)
        day = str(today.month)+'/'+str(today.day)+'/'+year[2:]
    else:
        year = str(tomorrow.year)
        day = str(tomorrow.month)+'/'+str(tomorrow.day)+'/'+year[2:]
    meal = request.form.get("mealtime")
    budget= request.form.get("price")
    para = {'cuisine':cuisine,'date':day,'meal':meal,'budget':budget}
    data = requests.get('https://berkeley-foodship-api.herokuapp.com/match',params = para)
    options = data.json()
    userinfo = options["userInfo"]
    key = list(options.keys())
    key.remove("userInfo")
    option1 = options[key[0]]
    option2 = options[key[1]]
    option3 = options[key[2]]
    money={"1":"$",
            "2":"$$",
            "3":"$$$"}
    pic1={}
    sequence1 = key[0]
    pic1["name"]= option1["initiator"]
    pic1["price"] = money[option1["budget"]]
    pic1["food"] = option1["cuisine"]
    pic1["time"] = option1["day"]
    pic1["meal"] = option1["meal"]
    pic2={}
    sequence2 = key[1]
    pic2["name"]= option2["initiator"]
    pic2["price"] = money[option2["budget"]]
    pic2["food"] = option2["cuisine"]
    pic2["time"] = option2["day"]
    pic2["meal"] = option2["meal"]
    pic3={}
    sequence3 = key[2]
    pic3["name"]= option3["initiator"]
    pic3["price"] = money[option3["budget"]]
    pic3["food"] = option3["cuisine"]
    pic3["time"] = option3["day"]
    pic3["meal"] = option3["meal"]
    cuisine = userinfo["cuisine"]
    day = userinfo["date"]
    meal = userinfo["meal"]
    budget = userinfo["budget"]
    return render_template("recommendation.html", pic1=pic1,pic2=pic2,pic3=pic3,
        sequence1=sequence1,sequence2=sequence2,sequence3=sequence3,
        cuisine=cuisine,day=day,meal=meal,budget=budget,
        user=username)



#receiving the request for creating a new record
@app.route('/new',methods=['POST'])
@login_required
def createNew():
    email = current_user.email
    para = {'user':email}
    data = requests.get('https://berkeley-foodship-api.herokuapp.com/username',params=para)
    info = data.json()
    username = info['firstname']
    cuisine = request.form.get("cuisine")
    day = request.form.get("day")
    meal = request.form.get("meal")
    budget = request.form.get("budget")
    data = {"email":email,"cuisine":cuisine,"day":day,"meal":meal,"budget":budget}
    r = requests.post('https://berkeley-foodship-api.herokuapp.com/create',json = data)
    if r.status_code == requests.codes.ok:
        return render_template("success.html",user=username)
    else:
        return render_template("fail.html",user=username)

