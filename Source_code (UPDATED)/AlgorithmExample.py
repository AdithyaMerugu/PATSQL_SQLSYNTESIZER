#   This Application will not take the runtime parameters. It only  process with the predefined inputs.
import mysql.connector

# Define the database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Replace with your MySQL root password
    database="syntests"
)
db_cursor = db_connection.cursor()

# Placeholder classes to represent the grammar constructs
class Table:
    def __init__(self, name):
        self.name = name

class Order:
    def __init__(self, table, key):
        self.table = table
        self.key = key

# Placeholder functions to represent the synthesized program
def generate_sql_query(input_table, output_table, synthesis_results):
    option, results = synthesis_results

    if option == 'SELECT':
        # Constructing the SELECT clause
        select_clause = ', '.join(results)
        
        # Constructing the FROM clause
        from_clause = f'FROM {input_table.name}'
        
        # Constructing the final SQL query
        sql_query = f'SELECT\n{select_clause}\n{from_clause}\n'
        return sql_query

    # Handle other synthesis options if needed

# User input (replace with user's choices)
input_table = Table("employees")
output_table = None
synthesis_results = ('SELECT', ["Name", "Age"])

# Generate the SQL query
sql_query = generate_sql_query(input_table, output_table, synthesis_results)
print(sql_query)

# Execute the SQL query
db_cursor.execute(sql_query)

# Fetch and print the results (only for SELECT queries)
results = db_cursor.fetchall()
for row in results:
    print(row)

# Close the database connection
db_connection.close()
