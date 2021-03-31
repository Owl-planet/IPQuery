from flask import Flask,render_template,request
import requests
from netaddr import IPNetwork

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/veri",methods = ["GET","POST"])
def veri():
    if request.method == "POST":
        ipi = request.form.get("ip")
        imask = request.form.get("mask")
        site = "https://ipinfo.io/" + ipi
        res = requests.get(site)
        data=res.json()
        imaskpp = '/'  +imask
        naislem = IPNetwork(ipi + imaskpp)
        return render_template(
            "info.html",
            ip = data['ip'],
            city = data['city'],
            region = data['region'],
            country = data['country'],
            org = data['org'],
            postal = data['postal'],
            timezone = data['timezone'],
            mask = naislem.netmask,
            ipbits = naislem.ip.bits(),
            networkbits = naislem.network.bits(),
            netmaskbits = naislem.netmask.bits(),
            broadcastbits = naislem.broadcast.bits(),
            cidr = naislem.cidr,
        )
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug = True)
