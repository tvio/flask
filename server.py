from flask import Flask, redirect, session,url_for,request,render_template
app = Flask(__name__, static_url_path='/static')


@app.route('/success/<name>')
def success(name):
    return "<html><body><p><Welcome %s</p></body></html>" %name

@app.route('/index', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        #return render_template('login.html')
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))



@app.route('/test')
def post():
    if request.method=='POST' and 'jmeno' in request.form:
     jmeno = request.form['jmeno']
     return render_template("test.html",jmeno=jmeno)     
    else:
     return render_template("test.html")
if __name__ == '__main__':
    app.run(debug = True)

