# sqlalchemy-challenge
Module 10 Challenge

## Overview
I have decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decide to do a climate analysis about the area. 

## Analyzing and Explore the Climate Data

In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, I used SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, I use the SQLAlchemy create_engine() function to connect to your SQLite database. I then used the SQLAlchemy automap_base() function to reflect my tables into classes, and then saved references to the classes named station and measurement.  I also linked Python to the database by creating a SQLAlchemy session.

### Precipitation Analysis
I found the most recent date in the dataset and used that date to get the previous 12 months of precipitation data by querying the previous 12 months of data. I loaded the query results into a Pandas DataFrame and set the column names, sorting the values by "date."

Below you can see the plot of my results:

![](https://github.com/Houdini24/sqlalchemy-challenge/blob/main/Resources/Precipitation%20Image.png)

### Station Analysis
I then designed a query to calculate the total number of stations in the dataset, and to find the most-active stations (that is, the stations that have the most rows). To do so, I listed the stations and observation counts in descending order. I also designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

Below you can see the histogram of my results:


Part 2: Design Your Climate App

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
/
Start at the homepage.
List all the available routes.
/api/v1.0/precipitation
Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.
/api/v1.0/stations
Return a JSON list of stations from the dataset.
/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.
/api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
Hints

Join the station and measurement tables for some of the queries.
Use the Flask jsonify function to convert your API data to a valid JSON response object.



