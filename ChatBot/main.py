from flask import Flask, request, render_template
from chat import get_response
app = Flask(__name__)
L=[]
L1=[]
c=0
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        the_question = request.form['text']


        response = get_response(the_question)

        L.append(the_question)

        L1.append(response)

    return render_template("index.html",b="you: "+ the_question,a="AI: "+response)

app.run(debug=True)