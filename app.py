from flask import Flask, render_template

app = Flask(__name__)

# --- HALAMAN WEB --- #

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/limbah-b3')
def limbah_b3():
    return render_template('limbah_b3.html')

@app.route('/ipal')
def ipal():
    return render_template('ipal.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
