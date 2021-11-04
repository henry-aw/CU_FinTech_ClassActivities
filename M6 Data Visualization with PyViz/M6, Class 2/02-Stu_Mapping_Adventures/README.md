# Mapping Adventures

It's time to take a break from your day job and to plan an adventure!

Your friends have decided to plan a trip to New York City, and you're all looking forward to the time away from the office. In order to plan for the event, you started doing some research regarding points of interest. You've found one dataset that lists a bunch of cool places to see.

Use **Plotly Express** and the **Mapbox API** to create a geographical plots that will visualize each area of interest within the city.

### Instructions

1. Create a .env file to hold your **Mapbox API access token**. Use the function provided to confirm that the token is available for use in the pro

2. Read in the Mapbox API access token using the `os.getenv` function, and use the function provided to confirm that the token is available for use in the program. Finally, set your Mapbox API access token as the parameter in the `px.set_mapbox_access_token` function.

3. Read in the `nyc_places_interest.csv` file from the Resources folder into a Pandas DataFrame. Drop any rows that contain missing data or NaN values.

4. Use the Plotly Express `scatter_mapbox` function to plot all of the places of interest, setting the color to **Name**.

5. Use `scatter_mapbox` to plot places of interest by **PlaceType**.

6. Plot places of interest by **Borough**.

7. Plot **parks** that are of interest.

8. Plot **gardens** that are of interest.

9. Plot **squares** that are of interest.

10. **Challenge** Select just two locations from the `places_of_interest` DataFrame and plot them on a scatter plot map.

  > Hint: Use the Pandas [`isin` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html) to reference a list containing the names of the two locations, as specified in the "Name" column, that you would like to visit.


### Hint

Creating too many map plots in one notebook might create a memory issue. Consider creating a separate notebook for the challenge section. This will require you to read the CSV data in both notebooks.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
