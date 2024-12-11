from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        # Mengambil data dari form
        user_input = request.form.get('user_input')
        result = f'Anda memasukkan: {user_input}'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)