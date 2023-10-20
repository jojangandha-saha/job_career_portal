from flask import Flask, render_template, jsonify

# create object of the class
app = Flask(__name__)

#create route - registering route after domain name and define function under this router

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru,India',
    'salary': '20k'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi,India',
    'salary': '100k'
}, {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Bengaluru,India',
    'salary': '90k'
}, {
    'id': 4,
    'title': 'Frontend Engineer',
    'location': 'Remote',
}]


@app.route('/')
def hello():
  return render_template('home.html', jobs=JOBS, company_name='LinkIn')


# JSON endpoint - insteead rendering template , jsonify . this route doesn;t return html instead it returns json object daata
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


#to run locally
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
