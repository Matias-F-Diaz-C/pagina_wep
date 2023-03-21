from flask import Flask, render_template,  request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/form_sent', methods=['POST','GET'])
def form_sent():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            with open('database.csv', 'a', newline="\n") as db:
                csv_write=csv.writer(db, delimiter=',', quotechar = '"', quoting =csv.QUOTE_MINIMAL)
                csv_write.writerow(data.values())
            return redirect('/thx.html')
        else: print('error')
    except: return 'Something went wrong, please try again :('