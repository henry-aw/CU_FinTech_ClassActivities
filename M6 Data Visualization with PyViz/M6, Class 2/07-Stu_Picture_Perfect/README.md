# Picture Perfect

Still in your role as a data analyst for a video streaming service, you have now been asked by your manager to compare and contrast the revenue numbers by quarter for the various international regions.

The results of your analysis will be presented at the board meeting so you need to make sure your visualizations are picture perfect.  Using the customization attributes and options demonstrated by the instructor, curate your visualizations. Make sure to assess each plot for opportunities of aesthetic improvement.

Be sure to consult the [HvPlot Customization](https://hvplot.holoviz.org/user_guide/Customization.html) page for additional opportunities of aesthetic improvement.

## Instructions

1. Open the [starter file](Unsolved/picture_perfect.ipynb), and create a Pandas DataFrame from the regional_revenue.csv file that is located in the Resources folder.

2. Create a line plot that visualizes the growth in revenue for the United States and Canada region.

3. Add x- and y-axis labels to your plot. Rotate the x-axis plot ticks 45 degrees.

4. Add a title to the US and Canada revenue plot.

5. Use the yformatter option to format y-axis values.

6. Add a line_color of blue and hover_line_color of yellow to the plot.

7. Save the plot you just created to a variable so that it can eventually be utilized in an overlay plot.

8. Create a line plot that visualizes the growth in revenue for the Europe, Middle East and Africa region. Style it with the same options utilized in the first plot. However, make the line_color equal to orange. Be sure to save this plot to a variable as well.

9. Create an overlay plot for the "United States and Canada" and the "Europe, Middle East and Africa" regions.

10. Add a title to the overlay plot. Additionally, adjust height, width and background color.

    > Hint: The `opts` function can be used customize composite plot (i.e `(plot_state_avgs * plot_2015_2016 * plot_2010_2014).opts(bgcolor="lightgrey")`)

11. If time permits, add stylized line plots for the Asia-Pacific and Latin America regions and include them in the overlay plot.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
