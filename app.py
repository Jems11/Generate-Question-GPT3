from flask import Flask,render_template,request
from time import time,sleep
import generate_que

app = Flask(__name__)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
		
def save_file(filepath, content):
	with open(filepath, 'w', encoding='utf-8') as outfile:
		outfile.write(content)

@app.route('/',methods=["GET","POST"])
def Index():
    return render_template("index.html",**locals())

@app.route('/result',methods=["GET","POST"])
def Generate_result():
    if request.method == 'POST':
        data = request.get_json()
        print("first: ",data)
        keyword = data[0]['para']
        para = data[0]['para']
        response = generate_que.GenerateParQuestions(keyword,para)
        filename = 'gpt3_que.txt'
        save_file( filename, '\n\n================\n\n' + response)
    return response

if __name__ == '__main__':
    app.run(port=8888,debug=True)