import sqlite3 # database library

table_name = f""  # Declare table_name as a global variable
dbConnection = sqlite3.connect('blackboard.db') # Connect to blackboard as a global variable
cursor = dbConnection.cursor() # Connect cursor as a global variable

def newTable(time_elapsed, h, v, m_fuel, m_lander, displacement, acceleration, impactTime):
    # Declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    # Execute a query to get the number of tables
    cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';")

    # Fetch the result
    num_tables = cursor.fetchone()[0]

    # Print the number of tables
    print("Number of tables in the database:", num_tables)
    table_name = f"blackboard_display_data{num_tables}"
    print(table_name)

    # create a new table
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
    (
    time_elapsed_sec float PRIMARY KEY,
    altitude float,
    velocity float,
    fuel_mass float,
    lander_mass float,
    displacement float,
    acceleration float,
    time_till_impact float
    );''')

    # Add Initial values
    Time = time_elapsed
    Altitude = h
    Velocity = v
    Fuel = m_fuel
    LanderMass = m_lander
    Displacement = displacement
    Acceleration = acceleration
    TTI = impactTime

    # Construct the SQL command for insertion
    sqlCommand = f"INSERT INTO {table_name} (time_elapsed_sec, altitude, velocity, fuel_mass, lander_mass, displacement, acceleration, time_till_impact) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    # Execute the insertion with parameterized values
    cursor.execute(sqlCommand, (Time, Altitude, Velocity, Fuel, LanderMass, Displacement, Acceleration, TTI))

    # Commit the changes
    dbConnection.commit()    

def getAltitude():
    # Declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    # Value from last row, altitude column
    sqlCommand = f"SELECT altitude FROM {table_name} ORDER BY time_elapsed_sec DESC LIMIT 1"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    row = cursor.fetchone()
    if row:
        result = row[0]

    return result  

def getVelocity():
    # Declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    # Value from last row, velocity column
    sqlCommand = f"select velocity from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    for row in cursor:
        result =  row[0]

    return result

def getFuelMass():
    # Declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    # Value from last row, fuel mass column
    sqlCommand = f"select fuel_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    for row in cursor:
        result =  row[0]

    return result

def getLanderMass():
    # Declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    # Value from last row, lander mass column
    sqlCommand = f"select lander_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    for row in cursor:
        result =  row[0]

    return result   

def getTotalMass():
    # Declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    # Value from last row, total mass column
    sqlCommand = f"select total_mass from {table_name}"
    cursor = dbConnection.execute(sqlCommand)
    
    result = 0
    for row in cursor:
        result =  row[0]

    return result

def addRow(time_elapsed, h, v, m_fuel, m_lander, displacement, acceleration, impactTime):
    # Declare that you are modifying the global variables within this function
    global table_name
    global dbConnection
    global cursor

    # Add new row to DB with this data
    Time = time_elapsed
    Altitude = h
    Velocity = v
    Fuel = m_fuel
    LanderMass = m_lander
    Displacement = displacement
    Acceleration = acceleration
    TTI = impactTime

    # Construct the SQL command for insertion
    sqlCommand = f"INSERT INTO {table_name} (time_elapsed_sec, altitude, velocity, fuel_mass, lander_mass, displacement, acceleration, time_till_impact) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    # Execute the insertion with parameterized values
    cursor.execute(sqlCommand, (Time, Altitude, Velocity, Fuel, LanderMass, Displacement, Acceleration, TTI))
    dbConnection.commit()

def close():
    # Declare global variables and close them
    global dbConnection
    global cursor
    cursor.close()
    dbConnection.close()