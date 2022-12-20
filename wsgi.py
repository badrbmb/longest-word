from flask import Flask, render_template, request, make_response
from longest_word.game import Game

app = Flask(__name__)
# add configuration
app.config.from_object(__name__)

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
    # get score
    score = int(request.cookies.get('score', 0))
    if is_valid:
        score += 1
    res = make_response(
        render_template(
            'check.html', is_valid=is_valid, grid=game.grid,
            word=word, score=score
            )
        )
    # save new score in cookies
    res.set_cookie('score', str(score))
    return res
