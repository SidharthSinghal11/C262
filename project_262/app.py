from flask import  Flask, request, redirect, url_for, render_template
import requests

app = Flask(__name__)
@app.route('/')
def main():
	return render_template('index.html')

@app.route('/gray',methods=['POST'])
def math_operations():
	equation=request.form['text']
	operation=request.form['operation']
	result='https://newton.now.sh/api/v2//'+operation+'/'+equation
	data=requests.get(result).json()
	answer=data['result']
	return render_template("index.html",result=answer,equation=equation)

if __name__=='__main__':
	app.run()