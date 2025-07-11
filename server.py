# imports
from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

@app.route('/')
def default_page():
    return redirect('index.html')

# one method route with variable
@app.route('/<string:path>')
def page(path = 'index.html'):
    return render_template(path)

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    # sends data from contact form to the server
    # form fields have name attribute that is needed for access later
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # grabs data from form to dictionary
            store_data_csv(data)
            return render_template('thankyou.html', name = data['name'])
        except:
            return 'did not save to database'
    else:
        return 'error'

def store_data(data):
    with open('./database.txt', 'a') as db:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f'\nMessage from {name} ({email}) with subject "{subject}" \n\t{message}')


def store_data_csv(data):
    with open('./database.csv', 'a') as db:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(db, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([name, email, subject, message])

