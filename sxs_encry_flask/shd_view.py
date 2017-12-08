#coding:utf-8
from flask import Flask
from flask import request
from flask import render_template
import ts
import shd_code
import shd_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('test1.html')



@app.route('/signin', methods=['POST'])
def signin():
	
	sss = request.form['shd_str']
	mobile = request.form['mobile']
	return shd_code.dec(sss,shd_model.get_auth(mobile))

if __name__ == '__main__':
	
	app.run(host='0.0.0.0',port=5001,debug=True)
	