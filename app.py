from flask import request,Flask,jsonify #pylint: disable=F0401
from flask_cors import CORS
import secrets
import PikuAi as bot
from time import gmtime, strftime
import json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbpiku.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(80))  
    


def verifyApi(key):
    user = User.query.filter_by(api_key=key).first()
    if user:
        return True
    return False    

def userExist(username):
    user_v = User.query.filter_by(username=username).first()
    if user_v:
        return True
    return False 


@app.route('/conv/<key>',methods=['GET'])
def replyBypiku(key):
    if verifyApi(key):
        q= str(request.args['getReply'])
        res = bot.PikuAi.getBot().response(q)
        return jsonify({"reply":res})
    return jsonify({"reply":"Invalid api key! visit website to get one."})

@app.route('/')
def index():
    return "server running fine"

@app.route('/info/<key>',methods=['GET'])
def userinfo(key):

    user = User.query.filter_by(api_key=key).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user_data = {}
    user_data['api_key'] = user.api_key
    user_data['username'] = user.username
    user_data['password'] = user.password

    return jsonify({'user' : user_data})

@app.route('/reg',methods=['POST'])
def register():
   
    uname = str(request.args['uname'])
    pwd=str(request.args['password'])
    if len(uname)<4 and len(pwd)<6:
        return jsonify({'message' : 'failed! Please check length of username is min 4 char and length of password is min 6 char content'})  
    api_predict=str(secrets.token_urlsafe(20))
    api_filter=User.query.filter_by(api_key=api_predict).first()
    if not api_filter:
        if not userExist(uname):
            api_final = api_predict
            new_user = User(api_key=api_final, username=uname, password=pwd)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message' : 'user created!','api':api_final})
        else:
            return jsonify({'message' : 'username already exist'})
    else:
        api_predict = str(secrets.token_urlsafe(20))
        
    return jsonify({'message' : 'failed! Please check parameters or contact support'})  


@app.route('/getapi',methods=['GET'])
def getInfoByidpass():
    uname = str(request.args['uname'])
    pwd=str(request.args['password'])

    user = User.query.filter_by(username=uname,password=pwd).first()

    if not user:
        return jsonify({'message' : 'No user found!'})

    user_data = {}
    user_data['api_key'] = user.api_key
    user_data['username'] = user.username
    user_data['password'] = user.password

    return jsonify({'user' : user_data})

if __name__ == '__main__':
    app.run(host= '0.0.0.0')