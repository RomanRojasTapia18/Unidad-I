from Satelite import satelite_orbita
from Satelite import Fuerza
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html',
                           the_title='Bienvenido')


@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    G = float(request.form['G'])
    M = float(request.form['M'])
    r = float(request.form['r'])
    m = float(request.form['m'])
    a = float(request.form['a'])
    result = satelite_orbita(G, M, r)
    resultF = Fuerza(m, a)
    title = "Satelite Orbita result and result force"
    return render_template('result.html',
                           the_G=G,
                           the_M=M,
                           the_r=r,
                           the_m=m,
                           the_a=a,
                           the_result=result,
                           the_resultF=resultF,
                           the_title=title)


app.run(debug=True)
