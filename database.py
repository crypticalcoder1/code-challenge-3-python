# database.py

import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('concerts.db')
connection.row_factory = sqlite3.Row  # This will allow us to get dict-like row objects
cursor = connection.cursor()

# Function to initialize the database schema
def initialize_db():
    with open('schema.sql', 'r') as schema_file:
        schema = schema_file.read()
    cursor.executescript(schema)
    connection.commit()

# Concert Methods
def get_band_for_concert(concert_id):
    query = """
    SELECT bands.* FROM bands
    JOIN concerts ON concerts.band_id = bands.id
    WHERE concerts.id = ?
    """
    cursor.execute(query, (concert_id,))
    return cursor.fetchone()

def get_venue_for_concert(concert_id):
    query = """
    SELECT venues.* FROM venues
    JOIN concerts ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """
    cursor.execute(query, (concert_id,))
    return cursor.fetchone()

def is_hometown_show(concert_id):
    query = """
    SELECT bands.hometown, venues.city FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """
    cursor.execute(query, (concert_id,))
    result = cursor.fetchone()
    return result['hometown'] == result['city']

def concert_introduction(concert_id):
    query = """
    SELECT bands.name, bands.hometown, venues.city FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE concerts.id = ?
    """
    cursor.execute(query, (concert_id,))
    result = cursor.fetchone()
    return f"Hello {result['city']}!!!!! We are {result['name']} and we're from {result['hometown']}"

# Band Methods
def get_concerts_for_band(band_id):
    query = "SELECT * FROM concerts WHERE band_id = ?"
    cursor.execute(query, (band_id,))
    return cursor.fetchall()

def get_venues_for_band(band_id):
    query = """
    SELECT DISTINCT venues.* FROM venues
    JOIN concerts ON concerts.venue_id = venues.id
    WHERE concerts.band_id = ?
    """
    cursor.execute(query, (band_id,))
    return cursor.fetchall()

def band_play_in_venue(band_id, venue_id, date):
    query = """
    INSERT INTO concerts (band_id, venue_id, date)
    VALUES (?, ?, ?)
    """
    cursor.execute(query, (band_id, venue_id, date))
    connection.commit()

def band_most_performances():
    query = """
    SELECT bands.name, COUNT(concerts.id) AS performance_count FROM bands
    JOIN concerts ON concerts.band_id = bands.id
    GROUP BY bands.id
    ORDER BY performance_count DESC
    LIMIT 1
    """
    cursor.execute(query)
    return cursor.fetchone()

# Venue Methods
def get_concerts_for_venue(venue_id):
    query = "SELECT * FROM concerts WHERE venue_id = ?"
    cursor.execute(query, (venue_id,))
    return cursor.fetchall()

def get_bands_for_venue(venue_id):
    query = """
    SELECT DISTINCT bands.* FROM bands
    JOIN concerts ON concerts.band_id = bands.id
    WHERE concerts.venue_id = ?
    """
    cursor.execute(query, (venue_id,))
    return cursor.fetchall()

def concert_on(venue_id, date):
    query = """
    SELECT * FROM concerts
    WHERE venue_id = ? AND date = ?
    LIMIT 1
    """
    cursor.execute(query, (venue_id, date))
    return cursor.fetchone()

def most_frequent_band(venue_id):
    query = """
    SELECT bands.name, COUNT(concerts.id) AS performance_count FROM bands
    JOIN concerts ON concerts.band_id = bands.id
    WHERE concerts.venue_id = ?
    GROUP BY bands.id
    ORDER BY performance_count DESC
    LIMIT 1
    """
    cursor.execute(query, (venue_id,))
    return cursor.fetchone()

# Close the database connection
def close_connection():
    connection.close()
