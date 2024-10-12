import sqlalchemy
import pandas as pd

connection_string = "postgresql+psycopg2://<user>:<password>@<host>:<port>/<database>"
db_engine = sqlalchemy.create_engine(connection_string)

# Update the query to select the review field
query = """
	SELECT 
    	review
    FROM nested_reviews;
"""

# Execute the query
data = pd.read_sql(query, db_engine)

# Print the first element of the DataFrame
print(data.iloc[0, 0])



# Build the query to select the statement and location fields
query = """
	SELECT 
    	review -> 'statement' AS statement, 
        review -> 'location' AS location 
    FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)
