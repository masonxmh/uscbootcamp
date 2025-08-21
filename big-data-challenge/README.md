# big-data-challenge

## Background

Many of Amazon's shoppers depend on product reviews to make a purchase. Amazon makes these datasets publicly available. However, they are quite large and can exceed the capacity of local machines to handle. One dataset alone contains over 1.5 million rows; with over 40 datasets, this can be quite taxing on the average local computer. Your first goal for this assignment will be to perform the ETL process completely in the cloud and upload a DataFrame to an RDS instance. The second goal will be to use PySpark or SQL to perform a statistical analysis of selected data.

## Analysis

The customers review data has been selected by vote number larger than 10, and then choose the helpful reviews more than 50% of the total reviews. Then split the vine and non-vine data.

* The average rating of vine review ratings are higher than non-vine review ratings.

* The star rating of five stars of non-vine percentage is higher than vine review.

## Conclusion

The vine system performance is not as good as expected.