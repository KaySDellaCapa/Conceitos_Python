from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST'])

def ola():
    return 'Olá, mundo'

if __name__ == '__main__':
    app.run()