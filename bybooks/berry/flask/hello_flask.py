from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/test')
def test_call() -> str:
    return '1 + 2 = 3 - it is just test function.'

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results)

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search letters app!')

#------------------------------------------------------------------------------
def search4letters(phrase:str, vowels:str):
    return set(vowels).intersection(set(phrase))


app.run(debug=True)
