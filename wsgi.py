from flask import Flask, render_template, request, session
from flask_session import Session
from longest_word.game import Game

app = Flask(__name__)
# add configuration
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid)


@app.route('/check', methods=['POST'])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    # init. score if missing
    if 'score' not in session:
        # init session score
        session['score'] = 0
    if is_valid:
        # increment global score
        session['score'] += 1
    return render_template(
        'check.html', is_valid=is_valid, grid=game.grid,
        word=word, score=session['score']
        )
