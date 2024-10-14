from flask import Flask, request, jsonify, render_template, redirect
import json
from urllib.parse import unquote
import asyncio
from tdmclient import ClientAsync, aw, notebook

app = Flask(__name__)

client = ClientAsync()

# make variable robot global
robots_json = ''
robots = []
robotsMap = {}

# create a map of the robots physical id and the id of the robot

async def setupThymios():
    await notebook.start()
    global robots
    robots = await notebook.get_nodes()

    # global robots_json
    # robots_json = [{"physical_id": i, "id": str(robot).replace("Node ", "")} for i, robot in enumerate(robots)]
    # with open('robots_info.json', 'w') as f:
    #     json.dump(robots_json, f)
    
    global robotsMap
    for i, robot in enumerate(robots):
        physical_id = str(robot).replace("Node ", "")
        print(f"Robot {i}: {physical_id}")
        robotsMap[physical_id] = i
    print(robotsMap.keys())
    print(robotsMap.values())



@app.route("/control")
def control():
    global robots_json
    return render_template('control.html', thymios=str(robots_json))

@app.route("/setup")
def setuo():
    asyncio.run(setupThymios())
    return redirect("/control")

@app.route("/")
def index():
    # Run setupThymios in an event loop
    return render_template('index.html')

@app.route("/thymio-form")
def thymioForm():
    physical_id_thymio = request.args.get('id')
    left_motor = request.args.get('l')
    right_motor = request.args.get('r')
    print(f"ID: {robotsMap.get(physical_id_thymio)},  L: {left_motor}, R: {right_motor}")
    moveThymio(robotsMap.get(physical_id_thymio), int(left_motor), int(right_motor))
    
    return redirect("/control")

@app.get('/thymio')
def getThymioParams():
    assert request.method == 'GET'

    # check that is only an params named json
    if len(request.args) != 1 or 'json' not in request.args:
        return "Error: only one parameter named json is allowed", 400
    
    encoded_json = request.args.get('json', default=None)
    if encoded_json:
        print(f"Encoded JSON: {encoded_json}")
        # decode the URL
        decoded_json = unquote(encoded_json)
        try:
            command_data = json.loads(decoded_json)
            
            physical_id_thymio = command_data.get("id")
            left_motor = command_data.get("l")
            right_motor = command_data.get("r")
            
            print(f"ID: {physical_id_thymio},  L: {left_motor}, R: {right_motor}")

            print(robotsMap.get(physical_id_thymio))
            moveThymio(robotsMap.get(physical_id_thymio) , left_motor, right_motor)
            
            return jsonify({"status": "ok", "message": "Data received", "ID": physical_id_thymio, "L": left_motor, "R": right_motor})
        
        except json.JSONDecodeError:
            return jsonify({"status": "error", "message": "Invalid JSON format"}), 400

def moveThymio(id, left, right):
    global robots
    robot = robots[id]
    print(robot)
    aw(robot.lock())
    v = {
        "motor.left.target": [int(left)],
        "motor.right.target": [int(right)],
    }
    aw(robot.set_variables(v))
    aw(robot.unlock())


if __name__ == '__main__':
    app.run(port=52000)

    
