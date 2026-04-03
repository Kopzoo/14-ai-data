from flask import Flask, render_template, request
from saramin import search_saramin  
from file import save_to_file
from flask import send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = search_saramin(keyword)

    return render_template(
        "search.html",
        keyword=keyword,
        jobs=enumerate(jobs)
    )

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    jobs = search_saramin(keyword)
    save_to_file(jobs)

    return send_file("./jobs.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)