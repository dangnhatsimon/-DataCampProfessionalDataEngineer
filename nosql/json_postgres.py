import pandas as pd


# Build a query to create a JSON-object
query = """
SELECT
	row_to_json(row(review_id, rating, year_month))
FROM reviews;
"""

# Execute the query, and output the results
results = pd.read_sql(query, db_engine)
print(results.head(10))



# Build a query to find the unique keys in the review column
query = """
SELECT
	DISTINCT json_object_keys(review)
FROM nested_reviews;
"""

# Execute the query, show the results
unique_keys = pd.read_sql(query, db_engine)
print(unique_keys)



# Build the query to select the review_id and rating fields
query = """
	SELECT 
    	review -> 'location' AS location, 
        review -> 'statement' AS statement 
    FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)



# Find the data type of the location field
query = """
SELECT
    json_typeof(review -> 'location') AS location_type
FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)



# Update the query to select the nested reviewer field
query = """
SELECT 
	review -> 'location' ->> 'branch' AS branch,
    review -> 'location' ->> 'reviewer' AS reviewer
FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)



# Build the query to select the rid and rating fields
query = """
SELECT
	review -> 'statement' AS customer_review 
FROM nested_reviews 
WHERE review -> 'location' ->> 'branch' = 'Disneyland_California';
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)


# Attempt to query the statement, nested branch, and nested
# zipcode fields from the review column
query = """
	SELECT 
    	json_typeof(review #> '{statement}'),
        review #>> '{location, branch}' AS branch,
        review #>> '{location, zipcode}' AS zipcode
    FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)




# Return the statement and reviewer fields, filter by the 
# nested branch field
query = """
    SELECT 
        json_extract_path(review, 'statement'),
        json_extract_path_text(review, 'location', 'reviewer')
    FROM nested_reviews
    WHERE json_extract_path_text(review, 'location', 'branch') = 'Disneyland_California';
"""

data = pd.read_sql(query, db_engine)
print(data)




# Extract fields from JSON, and filter by reviewer location
query = """
    SELECT
    	review_id,
        review #> '{location, branch}' AS branch,
        review ->> 'statement' AS statement,
        rating
    FROM nested_reviews
    WHERE json_extract_path_text(review, 'location', 'reviewer') = 'Australia'
    ORDER BY rating DESC;
"""

data = pd.read_sql(query, db_engine)
print(data)
