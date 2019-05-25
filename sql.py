"""import psycopg2

conn = psycopg2.connect(database="postgres", user = "postgres", password = "x", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

#/anaconda3/lib/python3.7/site-packages (2.8.2)

import asyncio
import asyncpg
import datetime

async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect('postgresql://postgres@localhost/test')
    # Execute a statement to create a new table.
    await conn.execute('''
        CREATE TABLE users(
            id serial PRIMARY KEY,
            name text,
            dob date
        )
    ''')

    # Insert a record into the created table.
    await conn.execute('''
        INSERT INTO users(name, dob) VALUES($1, $2)
    ''', 'Bob', datetime.date(1984, 3, 1))

    # Select a row from the table.
    row = await conn.fetchrow(
        'SELECT * FROM users WHERE name = $1', 'Bob')
    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))

    # Close the connection.
    await conn.close()

asyncio.get_event_loop().run_until_complete(main())
"""

import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(user='postgres', password='x',
                                 database='postgres', host='127.0.0.1')

    await conn.execute('''
        CREATE TABLE users(
            id serial PRIMARY KEY,
            name text,
            dob date
        )
    ''')
    row = await conn.fetchrow(
        'select * from player where player_host <> "'"N/A'")

    
    await conn.close()

#loop = asyncio.get_event_loop()
#loop.run_until_complete(run())
print(row)