from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def inicial():
    return render_template('template.html')


@app.route('/exemplos')
def exemplos():
    return render_template('exemplos.html')


@app.route('/exercicios')
def exercicios():
    return render_template('exercicios.html')


@app.route('/Curriculo')
def Curriculo():
    return render_template('Curriculo.html')


@app.route('/Ex1')
def Ex1():
    return render_template('Ex1.html')


@app.route('/Ex2')
def Ex2():
    return render_template('Ex2.html')


@app.route('/Ex3')
def Ex3():
    return render_template('Ex3.html')





@app.route('/exemplos/Divs')
def exemplos_Divs():
    return render_template('Divs.html')


@app.route('/exemplos/Formulario')
def exemplos_Formulario():
    return render_template('Formulario.html')


@app.route('/exemplos/Midia')
def exemplos_Midia():
    return render_template('Midia.html')


@app.route('/exemplos/Texto')
def exemplos_Texto():
    return render_template('Texto.html')



if __name__ == '__main__':
    app.run(debug=True)


