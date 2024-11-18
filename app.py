from flask import Flask

app = Flask(__name__)

@app.route('/')
def good_afternoon():
    return 'Good Afternoon, today is a wonderful day!'

@app.route('/forecast')  
def forecast():
    return 'Today will be sunny and windy'

@app.route('/')  
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
