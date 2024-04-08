from flask import Flask ,render_template,request


app = Flask(__name__)


app = Flask(__name__)

@app.route("/")
def app_rout():
  return render_template("app.html")
@app.route("/submitted" ,  methods=['POST', 'GET'])
def submitted():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["messag"]
    if (name and email and message) != ("" and " "):
       return 'Form submitted successfully!'
    else:
       return 'kindly go back and fill the form !'

if __name__ == ("__main__"):
    app.run(debug= True, port = 4001 )
    