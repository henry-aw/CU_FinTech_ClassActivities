# Data Cleaning

You have been hired as a consultant by a trading firm to help train a machine learning model for an algorithmic stock trader. Unfortunately, the data that is coming in to the firm has quality issues, and they need you to help clean it up. Your supervisor has sent you a CSV file containing a sample of their data. You need to figure out how to create a quality control preprocessing system.

## Instructions

1. Using the Pandas `read_csv` function, import `stock_data.csv` into a Pandas DataFrame. 

2. Identify the structure—the number of rows and columns—of the DataFrame. 

3. Generate a sample of the data to confirm the data has been imported correctly.

4. Identify the number of records in the DataFrame. Compare it with the number of rows in the original file.

5. Identify null records by calculating the average percent of nulls for each Series. **Hint:** This step requires the `mean` function.

6. Drop null records.

7. Confirm that all nulls have been dropped by calculating the `sum` of values that are null.

8. Default null `ebitda` values to 0.

9. Check that there are no null `ebitda` values using the `sum` function.

10. Remove duplicate rows.

### Bonus

Now that nulls and duplicates have been wrangled, clean up the data a little more by removing the `$` currency symbols from the `price` field. Then, use the `astype` function to cast `price` to a `float`.

## Hint

Pandas offers a `replace` function that can be executed against a Series. To learn more about this function, refer to the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html).

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
