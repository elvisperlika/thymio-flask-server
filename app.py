from flask import Flask, request, jsonify, render_template, redirect
import json
from urllib.parse import unquote
import asyncio
from tdmclient import ClientAsync, aw, notebook

app = Flask(__name__)

client = ClientAsync()

# make variable robot global
robots = []

async def setupThymios():
    await notebook.start()
    global robots
    robots = await notebook.get_nodes()
    print(robots)

@app.route("/control")
def control():
    return 'These are thymios on the network: ' + str(robots)

@app.route("/setup")
def setuo():
    asyncio.run(setupThymios())
    return redirect("/control")

@app.route("/")
def index():
    # Run setupThymios in an event loop
    return render_template('index.html')


@app.get('/thymio')
def getThymioParams():
    assert request.method == 'GET'

    # check that is only an params named json
    if len(request.args) != 1 or 'json' not in request.args:
        return "Error: only one parameter named json is allowed", 400
    
    encoded_json = request.args.get('json', default=None)
    if encoded_json:
        # decode the URL
        decoded_json = unquote(encoded_json)
        try:
            command_data = json.loads(decoded_json)
            
            id_thymio = command_data.get("id")
            left_motor = command_data.get("l")
            right_motor = command_data.get("r")
            
            print(f"ID: {id_thymio},  L: {left_motor}, R: {right_motor}")

            moveThymio(id_thymio, left_motor, right_motor)
            
            return jsonify({"status": "ok", "message": "Data received", "ID": id_thymio, "L": left_motor, "R": right_motor})
        
        except json.JSONDecodeError:
            return jsonify({"status": "error", "message": "Invalid JSON format"}), 400

def moveThymio(id, left, right):
    global robots
    robot = robots[id]
    print(robot)
    aw(robot.lock())
    v = {
        "motor.left.target": [left],
        "motor.right.target": [right],
    }
    aw(robot.set_variables(v))
    aw(robot.unlock())


if __name__ == '__main__':
    app.run(port=52000)

    
