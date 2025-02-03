from flask import Flask

app = CEFlask(__name__)

@app.route('/')

def home():
    return "Welcome to Flask"  # Fixed the typo in "Welcome"

if __name__ == '__main__':  # Ensure proper indentation
    app.run(debug=True)