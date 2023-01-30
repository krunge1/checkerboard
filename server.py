from flask import Flask, render_template

app= Flask(__name__)

@app.route('/checkerboard/<int:x>/<int:y>/<string:primary>/<string:secondary>')

def checkerboard(x, y, primary, secondary):
    return render_template("index.html",x=x, y=y, primary=primary, secondary=secondary)

app.run(debug=True)