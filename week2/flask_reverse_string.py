from flask import Flask
from reverse_string import reverse_string

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'hello world from Flask!!!'

@app.route('/reverse')
def do_reverse() -> str:
    return reverse_string('live long and prosper')

app.run()