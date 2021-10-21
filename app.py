from flask import Flask, render_template, request
from schedule import *

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/bus")
def bus_name():
    return render_template("busname.html", bus=sorted(busList))


@app.route("/stage")
def stage_name():
    return render_template("stagename.html", stage=sorted(list(stageList)))


@app.route("/stages")
def stages():
    return render_template("stages.html", stage=sorted(list(stageList)))


@app.route("/stage-result", methods=["POST"])
def result():
    stage = request.form["stageName"]
    stage_result = []
    for x in sorted(busList):
        if stage in schedule[x].values():
            stage_result.append(x)
    return render_template("list.html", stage1=stage, buses=stage_result)


@app.route("/stages-result", methods=["POST"])
def results():
    stage1 = request.form["first_stage"]
    stage2 = request.form["second_stage"]
    stages_result = []
    stage = stage1 +" - "+ stage2
    for x in sorted(busList):
        if (stage1 in schedule[x].values()) and (stage2 in schedule[x].values()):
            stages_result.append(x)
    return render_template("list.html", stage1=stage, buses=stages_result)


@app.route("/details", methods=["POST"])
def bus_detail():
    bus = request.form["busName"]
    return render_template("details.html", busName=bus, details=schedule[bus].items())


if __name__ == "__main__":
    app.run()
