from flask import Flask, render_template, request, redirect, flash
import os
from formulario import form_ponto, csrf
from models import Usuarios, Pontos, Pontuacao, Charadas
import utils
from sqlalchemy.sql import select


# auth = HTTPBasicAuth()
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)


@app.route("/pontos/", methods=['GET', 'POST'])
def home():
    form = form_ponto()
    try:
        if form.validate_on_submit():
            if verificaPonto(request.form['latitude'], request.form['longitude']):
                ponto = Pontos(latitude=request.form['latitude'], longitude=request.form['longitude'])
                ponto.save()
                flash("Localização cadastrada")
            else:
                flash("Localização inválida!")
    except:
        flash("Entradas inválidas!")

    return render_template('CadastroPontos.html', form=form)


def verificaPonto(latitude, longitude):
    p1 = 0 <= abs(float(latitude)) <= 90
    p2 = 0 <= abs(float(longitude)) <= 180
    if p1 and p2:
        return True
    return False

if __name__ == '__main__':
    app.run(debug=True)