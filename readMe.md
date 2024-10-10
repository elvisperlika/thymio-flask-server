# Read Me

Flask server that receive event from the Orchestrator (you can call it "leader") and control [Thymio Robots](https://www.thymio.org/). 

![Thymio II](https://www.thymio.org/wp-content/uploads/2021/12/intro_2_11zon.jpg)

You can use thi server with real Thymio and with the Simulator.

## Start the server

To start the server launch the command
```
ipython app.py
```
I choose the port 52000 for my server but you can change it in the code. By default it run on port 5000.

It's relvent to use ```ipython``` because the ```tdmclient.notebook``` work only with that interpreter.

## Connect with Thymios

1. Connect all Thymios you need in you network.
2. Open your browser in ```localhost:52000```(in my case).
3. Press the button **CONNECT**
4. Send a command to the server using the form (WIP)

## Send command

You need to send a GET request to the route **/robot*** with params:
```
/robots?json={"ID":1,"L":-50,"R":+50}
```

