from flask import Flask
from time import sleep

app = Flask(__name__)


@app.route("/time/<id>", methods=["GET"])
def hello(id):
    id = int(id)

    def escolhe_time(id):
        if id == 1:
            return "gremio"
        elif id == 2:
            return "internacional"
        elif id == 3:
            return "palmeiras"
        elif id == 4:
            return "corinthians"
        elif id == 5:
            return "sao_paulo"
        elif id == 6:
            return "santos"
        elif id == 7:
            return "cruzeiro"
        elif id == 8:
            return "flamengo"
        elif id == 9:
            return "fluminense"
        elif id == 10:
            return "vasco"
        else:
            return "N/A"

    time = escolhe_time(id)
    resp = {"id:": id, "time:": time}

    return resp


if __name__ == "__main__":
    app.run(debug=True)
