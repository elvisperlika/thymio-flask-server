# Read Me

Flask server that receive event from the Orchestrator (you can call it "leader") and control [Thymio Robots](https://www.thymio.org/). 

You can use this server with real Thymio II Robots and with the Simulator that you can launch by Thymio Suite. 
No need to setup the network, ```tdmclient``` and Thymio Suite do it for you.

## Start the server

To start the server launch the command
```
ipython app.py
```
I choose the port 52000 for my server but you can change it in the code. By default it runs on port 5000.

It's relvent to use ```ipython``` because the ```tdmclient.notebook``` work only with that interpreter.

## Control Thymios

1. Open ThymioSuite and plug in the dongles for all thymios you want to use.
2. Open your browser in ```localhost:port```.
3. Yuo will redirect to the control from and you can send manualy commands to a Thymio.
4. Send a command to the Thymio setting physical id, left power motor and right motor power

## API

Control a thymio from your project using this GET method in your application:

```
/thymio?json={"id":"44cdb758-cffc-42f3-ad5e-02262a80fcfc","l":-50,"r":+50}
```
- id: physical id
- l: left power motor
- r: right power motor


