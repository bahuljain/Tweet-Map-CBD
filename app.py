from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
from pymongo import Connection
from flask import Flask, render_template#, session
from flask.ext.socketio import SocketIO, emit
import logging

logging.basicConfig()

app = Flask('CloudProject1')
socketio = SocketIO(app)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
thread = None

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
       
    while True:
        time.sleep(5)
        count += 1
        socketio.emit('background thread',
                      {'data': 'backgroundThread', 'count': count},
                      namespace='/test')
                          
def sendCoordinatesFromDB():
    con = Connection()   
    db = con.twitterDatabase_test
    tweetsCollection = db.tweetsCollection_test
    tweets = tweetsCollection.find()
    coordinates = []
    for tweet in tweets:
        coordinates.append({'lat':tweet['coordinates'][1],'lon':tweet['coordinates'][0]})
    
    return coordinates    

def filterCoordinatesFromDB(keyword):
    con = Connection()   
    db = con.twitterDatabase_test
    tweetsCollection = db.tweetsCollection_test
    tweets = tweetsCollection.find()
    coordinates = []
    for tweet in tweets:
        if keyword.lower() in tweet['category']:
            coordinates.append({'lat':tweet['coordinates'][1],'lon':tweet['coordinates'][0]})
    return coordinates    


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('map.html')


@socketio.on('client connected', namespace='/test')
def load_coordinates(message):
    coordinates = sendCoordinatesFromDB()        
    emit('load all coordinates',
         {'coordinates':coordinates})

@socketio.on('filter event', namespace='/test')
def filter_coordinates(message):
    coordinates = filterCoordinatesFromDB(message['data'])        
    emit('filtered coordinates',
         {'coordinates':coordinates})


if __name__ == '__main__':
    socketio.run(app)
