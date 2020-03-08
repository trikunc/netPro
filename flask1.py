from flask import  Flask, request, jsonify
import json
from napalm import get_network_driver

app = Flask(__name__)

@app.route('/show_info', methods=["GET"])
def show_info():
    ip = request.args.get("ip_router")
    username = request.args.get("user")
    password = request.args.get("passw")

    #get info from router
    # ip = "192.168.122.46"

    driver = get_network_driver("ios")
    ios_r1 = driver(ip,username,password)
    ios_r1.open()

    r1_facts = ios_r1.get_facts()

    r1_interfaces = ios_r1.get_interfaces()

    # print(json.dumps(r1_facts, indent=3))
    return jsonify(r1_facts)


app.run(host='0.0.0.0', port=80, debug=True)
