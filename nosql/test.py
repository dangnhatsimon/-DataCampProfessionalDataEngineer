# Update the query to pull the team, year, event, and medal
# fields from the olympic_medals table
query = """
SELECT
	team,
    year,
    event,
    medal
FROM olympic_medals;
"""

results = conn.cursor().execute(query).fetch_pandas_all()
print(results)


# Select the review column from the nested_reviews table
query = """
SELECT 
	review
FROM nested_reviews;
"""

data = pd.read_sql(query, db_engine)
print(data)


# Set the name key-value pair
redis_conn.set("name", "Sarah")

# Retrieve and print the value stored in the "name" key
name = redis_conn.get("name")
print(name)
