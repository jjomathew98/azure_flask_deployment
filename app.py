from flask import Flask, render_template
import pandas as pd
import random
import faker 

#small change 
app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/random')
def randomnumber():
    number_var = random.randint(1 , 100000)
    return render_template('randomnumber.html', single_number = number_var)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
