from flask import Flask

app = Flask(__name__)

@app.route('/2')
def hello_word():
    return 'Helo Word'

if __name__ == '__main__':
    app.run()