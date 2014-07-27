import os, sys
mcstatus_path = os.path.abspath("mcstatus")
sys.path.append(mcstatus_path)
from flask import Flask
from flask import request
from flask import jsonify
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route("/query", methods=["GET"])
def serverQuery():
    host = request.args.get("host")
    port = request.args.get("port")
    query_type = request.args.get("type")

    query_type = str(query_type)
    host = str(host)
    port = int(port)

    query = MinecraftQuery(host, port)


    if query_type == "simple":
        basic_info = query.get_status()
        return jsonify(basic_info)
    else:
        info = query.get_rules()
        return jsonify(info)


@app.route("/", methods=["GET"])
def help():
    helpText = '<a href="https://github.com/nrauh/mcserverquery">Take a look at the docs on Github for information</a>'
    return helpText


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)