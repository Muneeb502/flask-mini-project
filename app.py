from flask import Flask ,render_template,request


app = Flask(__name__)


app = Flask(__name__)

@app.route("/")
def app_rout():
  return render_template("app.html")
@app.route("/submitted" ,  methods=['POST'])
def submitted():
    return 'Form submitted successfully!'

if __name__ == ("__main__"):
    app.run(debug= True, port = 4001 )
    