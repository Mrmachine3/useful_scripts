# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///chinook.db')

#Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT EmployeeId, FirstName, LastName, Title, Email FROM employees WHERE Title != 'Sales Support Agent'")
#    rs = con.execute("SELECT * FROM sqlite_master WHERE type != 'index';") 
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the length of the DataFrame df
#print(len(df))

# Print the head of the DataFrame df
#print(df.head())
print(df)

