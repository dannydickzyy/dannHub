from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def profile_form():
    return render_template('form.html')

@app.route('/profile', methods=['POST'])
def profile():
    profile_data = {
        'firstname': request.form['firstname'],
        'lastname': request.form['lastname'],
        'sex': request.form.get('sex', ''),
        'status': request.form['status'],
        'location': request.form['location']
    }
    return render_template('profile.html', profile=profile_data)

if __name__ == '__main__':
    app.run(debug=True)
