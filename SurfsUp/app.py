# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def route():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Precipitation Route: /api/v1.0/precipitation<br/>" 
        f"Stations Route: /api/v1.0/stations<br/>" 
        f"Tobs Route: /api/v1.0/tobs<br/>" 
        f"Start Route: /api/v1.0/<start><br/>" 
        f"Start/End Route: /api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Return json with the date as the key and the value as the precipitation
    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    year_old_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    data_precipitation = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= (year_old_date)).order_by(measurement.date.desc())
    
    # close the session
    session.close()
    
    p_data = {}  
    
    for date, p in data_precipitation:  
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = p
        p_data[date] = p  
    
    # Only returns the jsonified precipitation data for the last year in the database
    return jsonify(list(np.ravel(p_data)))

    
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(station.station).all()  
    stations = list(np.ravel(results))
    
    # close the session
    session.close()
    
    # A stations route that returns jsonified data of all of the stations in the database 
    return jsonify(list(np.ravel(stations)))


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    year_old_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temp_year_data = session.query(measurement.date, measurement.tobs).\
        filter(measurement.station == 'USC00519281', measurement.date >= year_old_date).all()
    temperature_data = list(temp_year_data)
    
    # close the session
    session.close()
    
    # Returns jsonified data for the most active station (USC00519281) 
    # Only returns the jsonified data for the last year of data 
    return jsonify(list(np.ravel(temperature_data))) 
    
    
@app.route("/api/v1.0/<start>")
def start():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    start = session.query(func.min(Measurement.tobs), 
                          func.max(Measurement.tobs), 
                          func.avg(Measurement.tobs)).filter(Measurement.date >= start)
    # close the session
    session.close()
    
    # Accepts the start date as a parameter from the URL 
    # Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset 
    start_list = []

    for min, max, avg in start:
        temp_dict = {}
        temp_dict["min"] = min
        temp_dict["max"] = max
        temp_dict["avg"] = avg
        start_list.append(temp_dict)

    return(jsonify(list(np.ravel(start_list))))
    
    
@app.route("/api/v1.0/<start>/<end>")
def startend():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    startend = session.query(func.min(Measurement.tobs), 
                             func.max(Measurement.tobs), 
                             func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end)
    # close the session
    session.close()
    
    # Accepts the start and end dates as parameters from the URL
    # Returns the min, max, and average temperatures calculated from the given start date to the given end date
    startend_list = []

    for min, max, avg in startend:
        startend_temp = {}
        startend_temp["min"] = min
        startend_temp["max"] = max
        startend_temp["avg"] = avg
        startend_list.append(startend_temp)

    return jsonify(list(np.ravel(startend_list)))



#start the app
if __name__ == "__main__":
    app.run(debug=True)