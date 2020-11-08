from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<page_name>')
def page_route(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter='|', quotechar='',
                                quoting=csv.QUOTE_NONE, escapechar='|')
        csv_writer.writerow([email, subject, message])
