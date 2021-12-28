from flask import Flask, render_template, request, redirect
from view import *

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    url=''
    if request.method == 'POST':
        url=request.form['url']
        ok = True
    else:
        ok = False
    resp = repeated_word_counter(words_into_url(url))
    return render_template('home.html',url=url,response=resp,ok=ok)

@app.route('/github')
def github():
    return render_template('github.html')

if __name__ == '__main__':
    app.run(debug=True)