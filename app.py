from flask import Flask,request, render_template
import datetime
import random

app = Flask(__name__)


# function to generate content
def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Strive not to be a success, but rather to be of value. - Albert Einstein"
    ]
    return random.choice(quotes)
def store_submission(name, email):
    with open('data_store.txt', 'a') as file:
        file.write(f'{name}, {email}\n')


@app.route('/')
def index():
    # get current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # get a random quote
    random_quote = get_random_quote()


    return render_template('index.html', current_time=current_time, random_quote=random_quote)
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']


        store_submission(name, email)


        return f'Thank you, {name}! Your email ({email}) has been submitted.'

@app.route('/view_submissions')
def view_submissions():
    # read and display stored form submissions
    with open('data_store.txt', 'r') as file:
        submissions = [line.strip() for line in file.readlines()]

    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
