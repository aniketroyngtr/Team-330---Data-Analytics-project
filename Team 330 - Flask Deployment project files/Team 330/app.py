from flask import Flask, render_template 

app = Flask(__name__) 

@app.route("/") 
def home(): 
    return render_template('index.html') 

@app.route("/index.html") 
def index(): 
    return render_template('index.html') 


@app.route("/Dashboard.html") 
def Dashboard(): 
    return render_template('Dashboard.html') 

@app.route("/services.html") 
def services(): 
    return render_template('services.html') 

@app.route("/team.html") 
def team(): 
    return render_template('team.html') 


 
app.run(debug=True) 