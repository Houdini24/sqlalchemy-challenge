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

![](https://github.com/Houdini24/sqlalchemy-challenge/blob/main/Resources/Temperature%20for%20Station%20USC00519281.png)




