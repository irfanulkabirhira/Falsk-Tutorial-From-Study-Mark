from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # Home page
def home():
    return render_template('index.html')

@app.route('/about')  # About page
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
