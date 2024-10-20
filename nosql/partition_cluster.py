# Leverage the existing micro-partitions and data clustering
query = """
SELECT
	team,
    year,
    sport,
    event,
    medal
FROM olympic_medals
WHERE year >= 2000;
"""

# Execute the query, print the results
results = conn.cursor().execute(query).fetch_pandas_all()
print(results)
