# app.py (Flask example)
from flask import Flask, render_template
from games import get_games

app = Flask(__name__)

@app.route('/')
def index():
    games = get_games()
    return render_template('index.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)
