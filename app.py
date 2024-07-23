# File: app.py
from flask import Flask, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

BASE_URL = 'http://127.0.0.1:5000'

def add_exclusion(data):
    url = f"{BASE_URL}/exclusions"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)
    return response.json(), response.status_code

def get_exclusion(id_number):
    url = f"{BASE_URL}/exclusions/{id_number}"
    response = requests.get(url)
    return response.json(), response.status_code

def view_exclusions():
    url = f"{BASE_URL}/exclusions"
    response = requests.get(url)
    return response.json(), response.status_code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_exclusion', methods=['GET', 'POST'])
def add_exclusion_page():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "date_of_birth": request.form['date_of_birth'],
            "gender": request.form['gender'],
            "street": request.form['street'],
            "city": request.form['city'],
            "state": request.form['state'],
            "zip": request.form['zip'],
            "reason": request.form['reason'],
            "start_date": request.form['start_date'],
            "end_date": request.form['end_date'],
            "exclusion_authority": request.form['exclusion_authority'],
            "notes": request.form['notes'],
            "id_type": request.form['id_type'],
            "id_number": request.form['id_number']
        }
        response, status_code = add_exclusion(data)
        if status_code == 201:
            flash('Exclusion added successfully!', 'success')
        else:
            flash(f'Error: {response["message"]}', 'danger')
        return redirect(url_for('add_exclusion_page'))
    return render_template('add_exclusion.html')

@app.route('/view_exclusions', methods=['GET'])
def view_exclusions_page():
    exclusions, status_code = view_exclusions()
    return render_template('view_exclusions.html', exclusions=exclusions)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
