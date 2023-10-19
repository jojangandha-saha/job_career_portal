from flask import Flask

# create object of the class
app = Flask(__name__)


#create route - registering route after domain name and define function under this router
@app.route('/')
def hello():
  return 'Hello World!'

#to run locally
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
