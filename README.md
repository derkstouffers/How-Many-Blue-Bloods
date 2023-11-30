# STAT371 Final Project - Blue Bloods in NBA Championship Teams

## Data Source
The data used for this analysis is sourced from the 'STAT371 CSV - Sheet1.csv' file, compiled using information from [Basketball-Reference](https://www.basketball-reference.com/). Basketball-Reference is a comprehensive online repository that provides detailed basketball statistics, including NBA championship data.

## Data Processing
1. Empties in the 'College' column, representing international or high school players, are handled by replacing them with 'international/high-school'.
2. Blue Blood schools, including Kentucky, Kansas, UNC, and Duke, are identified for analysis.
3. A hash map is created to track the number of Blue Blood players for each year.

## Results and Visualizations
1. Outliers and exceptional years are identified.
2. A bar graph illustrates the count of Blue Blood players per year from 1995 to 2023.
3. The Cumulative Distribution Function (CDF) is plotted to showcase the cumulative probability of Blue Blood players over the years.

## Expected Value
The analysis calculates the expected value, determining that, on average, it takes approximately [insert calculated value] Blue Blood players for an NBA team to achieve championship status.

## Usage
- Ensure you have the required CSV file ('STAT371 CSV - Sheet1.csv') in the same directory.
- Run the provided Python script to perform the analysis and generate visualizations.

## Author
- Deric Shaffer

- **Data Attribution:** The data used in this project is sourced from [Basketball-Reference](https://www.basketball-reference.com/), a valuable resource for basketball statistics.
