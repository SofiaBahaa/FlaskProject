from flask import Flask , render_template

my_app = Flask(__name__)  

@my_app.route("/")
def homepage():
    return render_template("home.html")    

@my_app.route("/about")
def about():
    return render_template("about.html",title = "aboutPage")

if __name__ == "__main__":
    my_app.run(debug=True)
    