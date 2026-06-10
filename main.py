from flask import Flask

#flask instance
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


@app.route('/products')
def products():
    return "product section"


app.run()