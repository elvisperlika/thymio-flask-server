# Read Me

Flask server that receive event from the Orchestrator (you can call it "leader") and control [Thymio Robots](https://www.thymio.org/). 

You can use this server with real Thymio II Robots and with the Simulator that you can launch by Thymio Suite. 
No need to setup the network, ```tdmclient``` do it fo you.

## Start the server

To start the server launch the command
```
ipython app.py
```
I choose the port 52000 for my server but you can change it in the code. By default it runs on port 5000.

It's relvent to use ```ipython``` because the ```tdmclient.notebook``` work only with that interpreter.

## Connect with Thymios

1. Connect all Thymios you need in you network.
2. Open your browser in ```localhost:52000```(in my case).
3. Press the button **CONNECT**
4. Send a command to the server using the form (WIP)

## Send command manually

Paste a string like this after the root:
```
/thymio?json={"id":1,"l":-50,"r":+50}
```

