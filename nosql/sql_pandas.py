import pandas as pd
import sqlalchemy

# Create a connection to the reviews database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/disneyland")

query = """SELECT * FROM nested_reviews;"""

# Execute the query, check out the results
results = pd.read_sql(query, db_engine)

# Print the review column from the results DataFrame
print(results["review"])
