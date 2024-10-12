import snowflake.connector

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
)


# Write a query to return all columns, limiting to 10 rows
query = "SELECT * FROM olympic_medals LIMIT 10;"

# Execute the query
results = conn.cursor().execute(query).fetch_pandas_all()

# Print the results of the query
print(results)


# Return team, name, and year for all years greater than 2000
query = """
SELECT
	team,
    name,
    year
FROM olympic_medals 
WHERE year > 2000
;
"""

# Execute the query, print the results
results = conn.cursor().execute(query).fetch_pandas_all()
print(results)

