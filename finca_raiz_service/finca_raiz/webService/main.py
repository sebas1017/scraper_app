

import requests
from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route("/menu", methods=["GET","POST"])
def menu():
    if request.method == "POST":
        print(request.form)
        data = { 
            "inmueble": request.form["inmueble"],
            "transaccion" : request.form["transaccion"],
            "ubicacion" : request.form["ubicacion"],
            "pagina" : "1"
            }
        
        params = {
        "crawl_args":json.dumps(data),
        "spider_name":"inmueblesFincaRaiz",
        "start_requests": "True"
        }
        print(params)
        data_finca_raiz = requests.post("http://finca-raiz-service:3000/crawl.json",data=json.dumps(params))
        data_finca_raiz = data_finca_raiz.json()["items"][0]["DATA"]["resultados"]        
        return json.dumps(data_finca_raiz)
    return render_template("input_form.html")


app.run(port=5000,host="0.0.0.0",debug=True)