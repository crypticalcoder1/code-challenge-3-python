# main.py

from database import (
    initialize_db, get_band_for_concert, get_venue_for_concert, concert_introduction,
    band_play_in_venue, band_most_performances, get_concerts_for_band, get_venues_for_band,
    get_concerts_for_venue, get_bands_for_venue, concert_on, most_frequent_band, is_hometown_show,
    cursor, connection, close_connection  # Import cursor, connection, and close_connection
)

# Initialize the database schema
initialize_db()

# Insert sample data for testing
cursor.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", ('The Beatles', 'Liverpool'))
cursor.execute("INSERT INTO venues (title, city) VALUES (?, ?)", ('Madison Square Garden', 'New York'))
connection.commit()

# Fetch the band and venue details
band = cursor.execute("SELECT * FROM bands WHERE name = ?", ('The Beatles',)).fetchone()
venue = cursor.execute("SELECT * FROM venues WHERE title = ?", ('Madison Square Garden',)).fetchone()

# Create a new concert
band_play_in_venue(band['id'], venue['id'], '2024-12-31')

# Fetch concert details
concert = cursor.execute("SELECT * FROM concerts").fetchone()
print(concert_introduction(concert['id']))

# Check hometown show
print(is_hometown_show(concert['id']))

# Get most frequent band
print(most_frequent_band(venue['id']))

# Close the database connection
close_connection()
