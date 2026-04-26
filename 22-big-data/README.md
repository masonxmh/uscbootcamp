# Big Data Homework: Amazon Reviews ETL

This folder contains the Big Data homework for Amazon customer reviews. The assignment uses PySpark to extract large public review datasets from S3, transform them into production-style tables, load them into an AWS RDS database, and analyze whether Amazon Vine reviews show rating bias.

## Background

Amazon publishes large customer review datasets that are too large for easy local analysis. This homework focuses on using cloud-style ETL tools to process those datasets and prepare them for relational database storage and analysis.

Datasets used:

- Amazon Camera Reviews
- Amazon Watches Reviews

Source:

- `https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt`

## Folder Structure

- `level-1/`: Required ETL workflow.
- `level-2/`: Optional Vine review bias analysis.

## Level 1: ETL To RDS

Files:

- `level-1/camera.ipynb`
- `level-1/watch.ipynb`
- `level-1/schema.sql`

The Level 1 notebooks extract the Camera and Watches review datasets from S3 with PySpark, count the records, transform each dataset into table-specific DataFrames, and load the outputs into PostgreSQL/RDS tables.

Record counts:

| Dataset | Records |
| --- | ---: |
| Camera reviews | 1,801,974 |
| Watches reviews | 960,872 |

Tables created by `schema.sql`:

- `review_id_table`
- `products`
- `customers`
- `vine_table`

Transformed DataFrames:

- `review_id_df`: Review ID, customer ID, product ID, product parent, and review date.
- `products_df`: Unique product IDs and product titles.
- `customers_df`: Customer IDs with review counts.
- `vine_df`: Review ID, star rating, helpful votes, total votes, and Vine flag.

## Level 2: Vine Review Analysis

Files:

- `level-2/camera_lvl2.ipynb`
- `level-2/watch_lvl2.ipynb`
- `level-2/vine_schema.sql`

The Level 2 notebooks analyze whether Vine reviews appear biased compared with non-Vine reviews. Reviews are filtered to reduce noisy data:

- Keep reviews with `total_votes >= 10`.
- Keep reviews where `helpful_votes / total_votes >= 0.5`.
- Split the filtered data into Vine reviews (`vine == "Y"`) and non-Vine reviews (`vine == "N"`).

### Camera Review Results

| Group | Review Count | Five-Star Reviews | Average Star Rating | Five-Star Percentage |
| --- | ---: | ---: | ---: | ---: |
| Vine | 1,171 | 518 | 4.14 | 44.24% |
| Non-Vine | 107,112 | 52,960 | 3.83 | 49.44% |

### Watches Review Results

| Group | Review Count | Five-Star Reviews | Average Star Rating | Five-Star Percentage |
| --- | ---: | ---: | ---: | ---: |
| Vine | 121 | 43 | 4.01 | 35.54% |
| Non-Vine | 23,615 | 12,083 | 3.79 | 51.17% |

## Findings

Across both selected datasets, Vine reviews had a higher average star rating than non-Vine reviews. However, non-Vine reviews had a higher percentage of five-star ratings in both categories.

Based on these results, the Vine program does not show a simple pattern of producing more five-star reviews. The average rating is higher for Vine reviews, but the five-star share is higher for non-Vine reviews, so the results are mixed.

## How To Review

Open the notebooks in Jupyter Notebook, JupyterLab, or a PySpark-compatible notebook environment:

1. `level-1/camera.ipynb`
2. `level-1/watch.ipynb`
3. `level-2/camera_lvl2.ipynb`
4. `level-2/watch_lvl2.ipynb`

Review the SQL schema files:

1. `level-1/schema.sql`
2. `level-2/vine_schema.sql`

## Notes

- The homework guideline recommends running the ETL workflow in a cloud notebook environment such as ZEPL with PySpark.
- RDS endpoint, username, and password values should be stored locally and removed before publishing notebooks.
- The `HW guideline/` folder is ignored by `.gitignore`.
