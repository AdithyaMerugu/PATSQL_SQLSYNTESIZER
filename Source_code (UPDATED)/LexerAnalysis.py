import mysql.connector
import ply.lex as lex
import ply.yacc as yacc

# Define the database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Replace with your MySQL root password
    database="syntests"
)
db_cursor = db_connection.cursor()

# Tokens
tokens = (
    'TABLE', 'ORDER', 'DISTINCT', 'PROJECT', 'SELECT', 'GROUP', 'WINDOW',
    'JOIN', 'LEFTJOIN', 'LPAREN', 'RPAREN', 'COMMA', 'ID', 'ASC', 'DESC',
    'MAX', 'MIN', 'COUNT', 'SUM', 'AVG', 'CONCATCOMMA', 'CONCATSPACE',
    'CONCATSLASH', 'RANK', 'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE', 'ISNULL',
    'ISNOTNULL', 'AND', 'OR', 'CONST'
)

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ASC = r'Asc'
t_DESC = r'Desc'
t_EQ = r'='
t_NEQ = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_AND = r'and'
t_OR = r'or'
t_ISNULL = r'isNull'
t_ISNOTNULL = r'isNotNull'
t_CONST = r'\d+'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Token for identifiers

t_ignore = ' \t\n'

# Placeholder class for the parsed tables
class Table:
    def __init__(self, name):
        self.name = name

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

# Parsing rules
def p_expression(p):
    '''expression : TABLE
                  | ORDER
                  | DISTINCT
                  | PROJECT
                  | SELECT
                  | GROUP
                  | WINDOW
                  | JOIN
                  | LEFTJOIN'''
    p[0] = p[1]

def p_select_expression(p):
    '''expression : SELECT LPAREN table RPAREN LPAREN column_list RPAREN'''
    input_table = p[3]
    output_table = None
    synthesis_results = ('SELECT', p[6])
    sql_query = generate_sql_query(input_table, output_table, synthesis_results)
    p[0] = sql_query

def p_table(p):
    'table : ID'
    p[0] = Table(p[1])

def p_column_list(p):
    '''column_list : ID COMMA ID
                   | ID'''
    p[0] = [p[1]]
    if len(p) == 4:
        p[0].append(p[3])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# User input for table and columns
table_name = input("Enter the table name: ")
column_input = input("Enter the column(s) separated by commas: ")
columns = [col.strip() for col in column_input.split(',')]

# Placeholder for user input
user_input = f'Select(({table_name}), ({", ".join(columns)}))'

# Example usage
result = parser.parse(user_input.lower())
print(result)

# Check the parsed result
if result:
    input_table, output_table, select_list = result
    # Generate the SQL query
    select_clause = ', '.join(select_list)
    from_clause = f'FROM {input_table.name}'
    sql_query = f'SELECT {select_clause} {from_clause};'
    print(sql_query)

    # Execute the SQL query
    db_cursor.execute(sql_query)

    # Fetch and print the results (only for SELECT queries)
    results = db_cursor.fetchall()
    for row in results:
        print(row)
else:
    print("Parsing error")

# Close the database connection
db_connection.close()
