from flask import Flask, render_template, request
from holiDay import inputDay

app = Flask(__name__)

@app.route('/HoliDay', methods=['GET', 'POST'])

def good():
    if request.method == 'GET':
        return render_template('inPage.html')
    
    elif request.method == 'POST':
        month=request.form['month']
        day=request.form['days']
        out = inputDay(month, day)
        return render_template('outPage', out=out)


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')

