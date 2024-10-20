# Build a query to pull city and country names
query = """
SELECT
	city_meta:city,
    city_meta:country
FROM host_cities;
"""

# Execute query and output results
results = conn.cursor().execute(query).fetch_pandas_all()
print(results)



# Build a query to extract nested location coordinates
query = """
SELECT
	city_meta:coordinates.lat,
    city_meta:coordinates.long
FROM host_cities;
"""

# Execute the query and output the results
results = conn.cursor().execute(query).fetch_pandas_all()
print(results)


