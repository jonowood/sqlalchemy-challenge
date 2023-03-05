<p align="center">
<img src="/Images/surfs-up.jpg" alt="" title="">
</p>

# Climate Analysis and Exploration in Honolulu

In this project, we analyze and explore climate data in Honolulu, Hawaii using Python, SQLAlchemy, and Flask API. We use the provided files climate_starter.ipynb and hawaii.sqlite to complete the analysis and exploration.

## Part 1: Climate Analysis and Exploration

In this section, we use Python and SQLAlchemy to analyze and explore the climate data from the database. We perform precipitation analysis and station analysis to understand the data better.

### Step 1: Connect to the database

We use the SQLAlchemy create_engine() function to connect to our SQLite database. We then use the SQLAlchemy automap_base() function to reflect our tables into classes and save references to the classes named station and measurement. Finally, we link Python to the database by creating a SQLAlchemy session.

### Step 2: Precipitation Analysis

We perform a precipitation analysis by finding the most recent date in the dataset and using that date to get the previous 12 months of precipitation data. We select only the "date" and "prcp" values and load the query results into a Pandas DataFrame. We then set the index to the "date" column and sort the DataFrame values by "date". Finally, we plot the results using the DataFrame plot method and print the summary statistics for the precipitation data.

### Step 3: Station Analysis

We perform a station analysis by designing a query to calculate the total number of stations in the dataset. We then design a query to find the most-active stations and answer the question: which station id has the greatest number of observations? Using the most-active station id, we calculate the lowest, highest, and average temperatures. Finally, we design a query to get the previous 12 months of temperature observation (TOBS) data, filter by the station that has the greatest number of observations, and plot the results as a histogram with bins=12.

## Part 2: Design Your Climate App

In this part, we design a Flask API based on the queries that we developed in Part 1.

### Routes
```/```: Start at the homepage and listing of all the available routes.

```/api/v1.0/precipitation```: Converts the query results to a dictionary by using date as the key and prcp as the value. Return the JSON representation of the dictionary.

```/api/v1.0/stations```: Returns a JSON list of stations from the dataset.

```/api/v1.0/tobs```: Queries the dates and temperature observations of the most-active station for the previous year of data. Return a JSON list of temperature observations for the previous year.

```/api/v1.0/<start>``` and ```/api/v1.0/<start>/<end>```: Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range. 
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date. For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

## Requirements

To run the code for this project, you will need the following libraries and tools:

- Python 3.6 or later
- Pandas
- Matplotlib
- SQLAlchemy
- Flask

Note: you will also need the hawaii.sqlite file and the climate_starter.ipynb notebook, which are provided in this repository.

## Project Structure
- `resources/` directory contains the dataset in CSV format and sqlite database
- `notebooks/` directory contains Jupyter notebooks used for data analysis & preprocessing
- `images/` directory contains images for readme
- `app.py` is the main Python file for the web application
- `requirements.txt` is the list of required dependencies to run the web application

## Running the Web Application

To run the web application, follow these steps:

1. Clone the repository
2. Install the required Python libraries using ```pip install -r requirements.txt```
3. Run ```python app.py``` in the terminal
4. Open the web application in the browser at ```http://localhost:5000```

## Acknowledgments
I would like to thank our bootcamp instructors for their guidance and support throughout this assignment.

## References
- Python: https://www.python.org/
- Pandas: https://pandas.pydata.org/
- Matplotlib: https://matplotlib.org/
- SQLAlchemy: https://www.sqlalchemy.org/
- Flask: https://flask.palletsprojects.com/

