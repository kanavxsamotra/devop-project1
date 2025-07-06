from flask importFlask 
app =Flask (__name__)
@app.route("/info")
def lwinfo():
return "im lw "
@app.route("/phone")
def lwphone():
return"(host=" 0.0.0.0")