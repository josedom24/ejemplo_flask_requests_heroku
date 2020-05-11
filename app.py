import requests
import os
from flask import Flask, render_template,abort
app = Flask(__name__)	
URL_BASE="https://dit.gonzalonazareno.org/redmine/"

@app.route('/',methods=["GET","POST"])
def inicio():
    key=os.environ["key"]
    payload = {'key':key}
    r=requests.get(URL_BASE+'projects.json',params=payload)
    if r.status_code == 200:
	    doc=r.json()
	    return render_template("inicio.html", lista=doc["projects"])
    else:
        abort(404)
port=os.environ["PORT"]
app.run('0.0.0.0',  int(port), debug=False)






