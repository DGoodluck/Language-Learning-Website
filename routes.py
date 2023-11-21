from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speech')
def speech():
    return render_template('speech.html')

@app.route('/listening')
def listening():
    return render_template('listening.html')

@app.route('/conversation')
def conversation():
    return render_template('conversation.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
