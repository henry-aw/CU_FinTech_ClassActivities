# A Cartographer's Expedition

You and your friends have decided to tackle NYC old school! No cell phones or GPS devices allowed. Although everyone is a bit nervous,  you realize that using an actual map might be pretty cool.

Instead of spending money on a map of NYC, become a true, modern cartographer and create interactive map plots that can be used by you and your friends to get the lay of the city.

Using the CSV file provided, your goal is to generate a map that plots between five and six locations in the city.  Plotly Express and Mapbox should be used to plot the route (point A to point B to point C) for the expedition.

## Instructions

1. Create a .env file to hold your **Mapbox API access token**.

2. Read in the Mapbox API access token using the `os.getenv` function. Use the function provided to confirm that the token is available for use in the program. Finally, set your Mapbox API access token as the parameter in the `px.set_mapbox_access_token` function.

3. Read in the `nyc_excursion_plans.csv` file in to a Pandas DataFrame. Drop any rows that contain missing data or NaN values.

4. Slice data for your **arriving airport** and the **first** location the group will visit.

  > Hint: You can use either or both of the Pandas [`str.contains`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.contains.html) or [`isin`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html) functions to access the names of the locations you intend to visit.

5. Now create a plot that includes your second and third location. Be sure to include your first stop so that you know how to get to the second.

6. Now create a plot that includes your fourth and fifth location. Be sure to include your third stop so that you know how to get where you are going.

7. Plot all locations on one map. What is the order in which you should visit them to get you back to the airport most efficiently?

### Challenge

If there are places in NYC that you'd like to visit and you know their geospatial details (latitude and longitude), feel free to add them to the data file. Be careful not to corrupt the data file.

If you do corrupt the file, re-download the data and start again.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
