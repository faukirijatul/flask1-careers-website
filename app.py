from flask import Flask, render_template, jsonify

app = Flask(__name__)

COMPANY_NAME = "Flask"

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Jakarta',
        'salary': 10000000
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bogor',
        'salary': 12000000
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Bekasi',
        'salary': 9000000
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Depok',
        'salary': 13000000
    }
]

@app.route("/")
def fisrt_template():
    return render_template("home.html", jobs=JOBS, company_name=COMPANY_NAME)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5002)