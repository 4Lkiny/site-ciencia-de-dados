from flask import Flask, render_template

app = Flask(_name_,
            template_folder= "siteciencia/templates", 
            static_folder = "siteciencia/static")
@app.route("/")
def index():
    #return "<h1> Bom dia, professor.<h1/>"
    return render_template("Index.html")
