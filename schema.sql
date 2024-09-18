-- schema.sql

DROP TABLE IF EXISTS concerts;
DROP TABLE IF EXISTS bands;
DROP TABLE IF EXISTS venues;

-- Create bands table
CREATE TABLE bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
);

-- Create venues table
CREATE TABLE venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    city TEXT NOT NULL
);

-- Create concerts table
CREATE TABLE concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER,
    venue_id INTEGER,
    date TEXT,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);
