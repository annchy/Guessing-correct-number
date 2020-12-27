from flask import Flask, render_template ,request, url_for, redirect
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/predict',methods=['POST','GET'])
def random():
    import random
    rand_num = random.randint(0,10)
    values=[x for x in request.form.values()] 
    values = "". join(values)
    values = int(values)
    if values == rand_num:
        return render_template('index.html', pred = 'Congratulations, you predicted correct value')
    else:
        return render_template('index.html', pred = 'wrong value, correct value was {} and your value was {}'.format(rand_num,values))

    
if __name__=='__main__':
    app.run(debug=True)