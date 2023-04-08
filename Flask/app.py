from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt
import numpy as np


# Set up the database
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
base = automap_base()
base.prepare(engine, reflect=True)

t_measurement = base.classes.measurement
t_station = base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_data = session.query(t_measurement.date, t_measurement.prcp).filter(t_measurement.date >= one_year_ago).all()
    session.close()

    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(t_station.station).all()
    session.close()

    stations_list = list(np.ravel(stations))
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    most_active_station_id = 'USC00519281'
    tobs_data = session.query(t_measurement.tobs).filter(t_measurement.station == most_active_station_id).filter(t_measurement.date >= one_year_ago).all()
    session.close()

    tobs_list = list(np.ravel(tobs_data))
    return jsonify(tobs_list)

def calc_temps(start_date, end_date=None):
    session = Session(engine)
    if end_date:
        temps = session.query(func.min(t_measurement.tobs), func.avg(t_measurement.tobs), func.max(t_measurement.tobs)).filter(t_measurement.date >= start_date).filter(t_measurement.date <= end_date).all()
    else:
        temps = session.query(func.min(t_measurement.tobs), func.avg(t_measurement.tobs), func.max(t_measurement.tobs)).filter(t_measurement.date >= start_date).all()
    session.close()

    temps_list = list(np.ravel(temps))
    return temps_list

@app.route("/api/v1.0/<start>")
def start(start):
    temps = calc_temps(start)
    temps_dict = {"TMIN": temps[0], "TAVG": temps[1], "TMAX": temps[2]}
    return jsonify(temps_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    temps = calc_temps(start, end)
    temps_dict = {"TMIN": temps[0], "TAVG": temps[1], "TMAX": temps[2]}
    return jsonify(temps_dict)

if __name__ == '__main__':
    app.run(debug=True)