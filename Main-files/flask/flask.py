import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username= request.form['username']
    data_username= {'nom': username}

    mail = request.form['mail']
    data_mail = {'mail': mail}

    password = request.form['password']
    data_password = {'password': password}

    with open('data.json', 'w') as outfile:
        json.dump(data_username, outfile)
        outfile.write('\n')
        json.dump(data_mail, outfile)
        outfile.write('\n')
        json.dump(data_password, outfile)
        outfile.write('\n')
        
    return render_template('result.html', username=username, mail=mail, password=password)

if __name__ == '__main__':
    app.run(debug=True)