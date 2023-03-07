# print("Hello world")
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Pune, India',
    'salary':1000000
  },
    {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':2000000
  },
    {
    'id':3,
    'title':'Frontend dev',
    'location':'Remote',
    'salary':3000000
  },
    {
    'id':4,
    'title':'Backend dev',
    'location':'Nagpur, India',
    'salary':4000000
  }
]

@app.route("/")
def helloWorld():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)