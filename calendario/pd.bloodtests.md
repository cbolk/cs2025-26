### Datasets

1. `regions`: Basic info about geographic areas included in the study

| Column        | Type   | Description                      |
| ------------- | ------ | -------------------------------- |
| `region_id`   | int    | Unique identifier for the region |
| `region_name` | string | Name of the geographic area      |
| `population`  | int    | Estimated population size        |

2. `campaigns`: Blood-test campaigns run in different regions at different times

| Column           | Type             | Description                                          |
| ---------------- | ---------------- | ---------------------------------------------------- |
| `campaign_id`    | int              | Unique identifier for each blood test campaign       |
| `region_id`      | int              | Region where the campaign was performed              |
| `campaign_month` | string (YYYY-MM) | Month the campaign took place                        |
| `test_type`      | string           | Type of blood test (e.g., *Glucose*, *Cholesterol*)  |

3. `results`: Aggregated results from each campaign

| Column        | Type   | Description                                           |
| ------------- | ------ | ----------------------------------------------------- |
| `campaign_id` | int    | Campaign identifier (FK → `campaigns.campaign_id`)    |
| `age_group`   | string | Age bracket (e.g., *18–30*, *31–50*, *51+*)           |
| `avg_value`   | float  | Average measured value for the test in that age group |
| `num_tests`   | int    | Number of tests performed in that age group           |


**List of questions for getting knowledge from data**

+ Which regions participated in blood-test campaigns, and how many campaigns did each region run?
+ For each test type, what is the total number of tests performed across all campaigns?
+ List all campaigns that took place in a given month (e.g., "2024-03") and identify the regions involved.
+ Merge region information with campaign results to compute: the average test value per region and per test type.
+ Find the top 3 regions with the highest number of total tests performed across all campaigns.
+ For each campaign, create a table showing age groups as rows and avg_value as columns for different test types.
+ Identify campaigns where at least one age group recorded an avg_value above a chosen threshold (e.g., glucose > 110).
+ Compute the percentage of each region’s population that participated in tests during the entire dataset period.
+ Determine month-to-month changes in average values for a specific test type within each region.
+ For each region, find which age group had the highest average measurement across all campaigns.
+ Produce a report of all cholesterol campaigns run in regions with population > 200,000, including total tests performed and date of the campaign.


