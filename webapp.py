from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
from operator import itemgetter
from analyse_file import openFile

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template(
        'home.html',
        title='Word Associations',
        header='Select A File to examine'
    )


@app.route('/checkfile', methods=['POST'])
def checkfile():
    if not request.files['file']:
        return redirect(url_for("homepage"))
    choice = int(request.form['option'])
    f = request.files['file']
    f.save('uploadedFiles/' + secure_filename(f.filename))
    return render_template(
        'results.html',
        index=choice,
        basicData=sorted(
            openFile('uploadedFiles/' + f.filename, choice),
            key=itemgetter('frequency'),
            reverse=True
        ),
        advancedData=sorted(
            openFile('uploadedFiles/' + f.filename, choice),
            key=itemgetter('score'),
            reverse=True
        )
    )


if __name__ == '__main__':
    app.run(debug=True)
