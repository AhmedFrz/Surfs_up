
#9.4.3 Set Up Flask and Create a Route 

from flask import Flask
app = Flask(__name__)
@app.route('/')

@app.route('/')
def hello_world():
    return 'Hello world ahmed faraz'

if __name__ == '__main__':
   app.run()


# 9.5.1 Set Up the Database and Flask

# Set Up the Flask Weather App
# Add these dependencies to the top of your app.py file.

import datetime as dt
import numpy as np
import pandas as pd


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")


Base = automap_base()
Base.prepare(engine, reflect=True)


Measurement = Base.classes.measurement
Station = Base.classes.station


session = Session(engine)


# Set Up Flask
app = Flask(__name__)


import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")




### 9.5.2 Create the Welcome Route

@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')



### 9.5.3 Precipitation Route
# To create the route, add the following code
@app.route("/api/v1.0/precipitation")
def precipitation():
    return

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   return


def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


### 9.5.4 Stations Route

@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)



### 9.5.5 Monthly Temperature Route
# problem

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    return



def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)



### 9.5.6 Statistics Route

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)



def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


# command line type 
    # flask run

#copy and paste the web address provided by Flask into a web browser. 
    # Open /api/v1.0/temp/start/end route 

# You would add the following path to the address in your web browser:
    # /api/v1.0/temp/2017-06-01/2017-06-30

# When you run the code, it should return the following result:
# ["temps":[71.0,77.21989528795811,83.0]]