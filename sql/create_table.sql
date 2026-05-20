-- Run this script once to create the bookings table in PostgreSQL
-- Connect to your database first:  psql -U postgres -d hotel_db

CREATE TABLE IF NOT EXISTS bookings (
    id            SERIAL PRIMARY KEY,
    full_name     VARCHAR(150)  NOT NULL,
    email         VARCHAR(150)  NOT NULL,
    phone         VARCHAR(30)   NOT NULL,
    check_in      DATE          NOT NULL,
    check_out     DATE          NOT NULL,
    room_type     VARCHAR(50)   NOT NULL,
    num_guests    INTEGER       NOT NULL CHECK (num_guests >= 1),
    special_requests TEXT       DEFAULT '',
    created_at    TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);
