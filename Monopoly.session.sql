-- ALTER TABLE players
-- ADD COLUMN position INTEGER DEFAULT 0;

-- ALTER TABLE players
-- ADD COLUMN in_jail BOOLEAN DEFAULT FALSE;


-- ALTER TABLE players ADD COLUMN board_id INTEGER;
-- ALTER TABLE players ADD CONSTRAINT fk FOREIGN KEY (board_id) REFERENCES board(id);
-- ALTER TABLE players ADD COLUMN game_id INTEGER;
-- ALTER TABLE players ADD CONSTRAINT fk_game FOREIGN KEY (game_id) REFERENCES games(id);
-- ALTER TABLE games ADD COLUMN current_turn INTEGER;
-- ALTER TABLE games ADD CONSTRAINT fk_turn FOREIGN KEY (current_turn) REFERENCES players(id);
-- ALTER TABLE dice_rolls
-- ADD CONSTRAINT fk_player
-- FOREIGN KEY (player_id) REFERENCES players(id);


-- ALTER TABLE players
-- ADD CONSTRAINT fk_players_game
-- FOREIGN KEY (game_id) REFERENCES games(id);

-- ALTER TABLE jail
-- ADD COLUMN game_id INTEGER REFERENCES games(id);

-- ALTER TABLE players ADD COLUMN laps INTEGER DEFAULT 0;

-- ALTER TABLE properties ADD COLUMN position INTEGER;
-- ALTER TABLE properties ADD COLUMN rent INTEGER DEFAULT 0;

ALTER TABLE properties ADD CONSTRAINT unique_property_position UNIQUE (position);




-- INSERT INTO properties (name, price, owner_id) VALUES
--   ('Mediterranean Avenue', 60, NULL),
--   ('Baltic Avenue', 60, NULL),
--   ('Oriental Avenue', 100, NULL),
--   ('Vermont Avenue', 100, NULL),
--   ('Connecticut Avenue', 120, NULL),
--   ('St. Charles Place', 140, NULL),
--   ('Electric Company', 150, NULL),
--   ('States Avenue', 140, NULL),
--   ('Virginia Avenue', 160, NULL),
--   ('Pennsylvania Railroad', 200, NULL),
--   ('St. James Place', 180, NULL),
--   ('Tennessee Avenue', 180, NULL),
--   ('New York Avenue', 200, NULL),
--   ('Kentucky Avenue', 220, NULL),
--   ('Indiana Avenue', 220, NULL),
--   ('Illinois Avenue', 240, NULL),
--   ('B&O Railroad', 200, NULL),
--   ('Atlantic Avenue', 260, NULL),
--   ('Ventnor Avenue', 260, NULL),
--   ('Water Works', 150, NULL),
--   ('Marvin Gardens', 280, NULL),
--   ('Pacific Avenue', 300, NULL),
--   ('North Carolina Avenue', 300, NULL),
--   ('Pennsylvania Avenue', 320, NULL),
--   ('Short Line Railroad', 200, NULL),
--   ('Park Place', 350, NULL),
--   ('Boardwalk', 400, NULL);

UPDATE properties SET position = 1, rent = 2 WHERE name = 'Mediterranean Avenue';
UPDATE properties SET position = 3, rent = 4 WHERE name = 'Baltic Avenue';
UPDATE properties SET position = 6, rent = 6 WHERE name = 'Oriental Avenue';
UPDATE properties SET position = 8, rent = 6 WHERE name = 'Vermont Avenue';
UPDATE properties SET position = 9, rent = 8 WHERE name = 'Connecticut Avenue';
UPDATE properties SET position = 11, rent = 10 WHERE name = 'St. Charles Place';
UPDATE properties SET position = 12, rent = 75 WHERE name = 'Electric Company'; 
UPDATE properties SET position = 13, rent = 10 WHERE name = 'States Avenue';
UPDATE properties SET position = 14, rent = 12 WHERE name = 'Virginia Avenue';
UPDATE properties SET position = 15, rent = 25 WHERE name = 'Pennsylvania Railroad';
UPDATE properties SET position = 16, rent = 14 WHERE name = 'St. James Place';
UPDATE properties SET position = 18, rent = 14 WHERE name = 'Tennessee Avenue';
UPDATE properties SET position = 19, rent = 16 WHERE name = 'New York Avenue';
UPDATE properties SET position = 21, rent = 18 WHERE name = 'Kentucky Avenue';
UPDATE properties SET position = 23, rent = 18 WHERE name = 'Indiana Avenue';
UPDATE properties SET position = 24, rent = 20 WHERE name = 'Illinois Avenue';
UPDATE properties SET position = 25, rent = 25 WHERE name = 'B&O Railroad'; 
UPDATE properties SET position = 26, rent = 22 WHERE name = 'Atlantic Avenue';
UPDATE properties SET position = 27, rent = 22 WHERE name = 'Ventnor Avenue';
UPDATE properties SET position = 28, rent = 75 WHERE name = 'Water Works'; 
UPDATE properties SET position = 29, rent = 24 WHERE name = 'Marvin Gardens';
UPDATE properties SET position = 31, rent = 26 WHERE name = 'Pacific Avenue';
UPDATE properties SET position = 32, rent = 26 WHERE name = 'North Carolina Avenue';
UPDATE properties SET position = 34, rent = 28 WHERE name = 'Pennsylvania Avenue';
UPDATE properties SET position = 35, rent = 25 WHERE name = 'Short Line Railroad';
UPDATE properties SET position = 37, rent = 35 WHERE name = 'Park Place';
UPDATE properties SET position = 39, rent = 50 WHERE name = 'Boardwalk';




-- INSERT INTO chance_cards (description) VALUES
--   ('Advance to Go (Collect $200)'),
--   ('Advance to Illinois Avenue'),
--   ('Advance to St. Charles Place'),
--   ('Advance token to nearest Utility. If unowned, you may buy it.'),
--   ('Advance token to the nearest Railroad and pay owner twice the rental to which they are otherwise entitled.'),
--   ('Bank pays you dividend of $50'),
--   ('Get Out of Jail Free. This card may be kept until needed or sold.'),
--   ('Go Back 3 Spaces'),
--   ('Go to Jail. Go directly to Jail, do not pass Go, do not collect $200'),
--   ('Make general repairs on all your property: For each house pay $25, For each hotel pay $100'),
--   ('Pay poor tax of $15'),
--   ('Take a trip to Reading Railroad. If you pass Go, collect $200'),
--   ('Take a walk on the Boardwalk. Advance token to Boardwalk.'),
--   ('You have been elected Chairman of the Board. Pay each player $50'),
--   ('Your building loan matures. Collect $150'),
--   ('You have won a crossword competition. Collect $100');


-- INSERT INTO community_chest_cards (description) VALUES
--   ('Advance to Go (Collect $200)'),
--   ('Bank error in your favor. Collect $200'),
--   ('Doctors fees. Pay $50'),
--   ('From sale of stock you get $50'),
--   ('Get Out of Jail Free. This card may be kept until needed or sold'),
--   ('Go to Jail. Go directly to Jail, do not pass Go, do not collect $200'),
--   ('Grand Opera Night. Collect $50 from every player for opening night seats'),
--   ('Holiday Fund matures. Receive $100'),
--   ('Income tax refund. Collect $20'),
--   ('It is your birthday. Collect $10 from every player'),
--   ('Life insurance matures. Collect $100'),
--   ('Hospital Fees. Pay $100'),
--   ('School fees. Pay $50'),
--   ('Receive $25 consultancy fee'),
--   ('You are assessed for street repairs: Pay $40 per house and $115 per hotel'),
--   ('You have won second prize in a beauty contest. Collect $10'),
--   ('You inherit $100');

-- DROP TABLE cards;

-- INSERT INTO board (position, name, type) VALUES
--   (0, 'Go', 'go'),
--   (1, 'Mediterranean Avenue', 'property'),
--   (2, 'Community Chest', 'community_chest'),
--   (3, 'Baltic Avenue', 'property'),
--   (4, 'Income Tax', 'tax'),
--   (5, 'Reading Railroad', 'railroad'),
--   (6, 'Oriental Avenue', 'property'),
--   (7, 'Chance', 'chance'),
--   (8, 'Vermont Avenue', 'property'),
--   (9, 'Connecticut Avenue', 'property'),
--   (10, 'Jail / Just Visiting', 'jail'),
--   (11, 'St. Charles Place', 'property'),
--   (12, 'Electric Company', 'utility'),
--   (13, 'States Avenue', 'property'),
--   (14, 'Virginia Avenue', 'property'),
--   (15, 'Pennsylvania Railroad', 'railroad'),
--   (16, 'St. James Place', 'property'),
--   (17, 'Community Chest', 'community_chest'),
--   (18, 'Tennessee Avenue', 'property'),
--   (19, 'New York Avenue', 'property'),
--   (20, 'Free Parking', 'free_parking'),
--   (21, 'Kentucky Avenue', 'property'),
--   (22, 'Chance', 'chance'),
--   (23, 'Indiana Avenue', 'property'),
--   (24, 'Illinois Avenue', 'property'),
--   (25, 'B&O Railroad', 'railroad'),
--   (26, 'Atlantic Avenue', 'property'),
--   (27, 'Ventnor Avenue', 'property'),
--   (28, 'Water Works', 'utility'),
--   (29, 'Marvin Gardens', 'property'),
--   (30, 'Go To Jail', 'go_to_jail'),
--   (31, 'Pacific Avenue', 'property'),
--   (32, 'North Carolina Avenue', 'property'),
--   (33, 'Community Chest', 'community_chest'),
--   (34, 'Pennsylvania Avenue', 'property'),
--   (35, 'Short Line', 'railroad'),
--   (36, 'Chance', 'chance'),
--   (37, 'Park Place', 'property'),
--   (38, 'Luxury Tax', 'tax'),
--   (39, 'Boardwalk', 'property');


