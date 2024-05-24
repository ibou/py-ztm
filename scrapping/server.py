from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("./index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("data.txt", mode="a") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f"{email}, {subject}, {message}\n")

def write_to_csv(data):
    # créer une entete du fichier csv s'il n'existe pas
 
    with open("data.csv", newline='', mode="a") as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_csv)
        csv_writer.writerow([email, subject, message])
         

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("./thankyou.html")
        except:
            return 'did not save to database'
    else:
        return "Form Submitted but something wrong"
