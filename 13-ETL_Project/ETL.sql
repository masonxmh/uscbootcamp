-- Create Beer ID Table--------------------------
DROP TABLE IF EXISTS beer_id_table;
CREATE TABLE beer_id_table (
	id INT NOT NULL PRIMARY Key,
	name VARCHAR NOT NULL);
SELECT * FROM beer_id_table;

-- Create Brewery ID Table--------------------------
DROP TABLE IF EXISTS brewery_id_table;
CREATE TABLE brewery_id_table (
	brewery_id INT NOT NULL PRIMARY Key,
	brewery_name VARCHAR NOT NULL);
SELECT * FROM brewery_id_table;

-- Create Profile Table--------------------------
DROP TABLE IF EXISTS beer_profile_table;
CREATE TABLE beer_profile_table (
	id INT NOT NULL,
	name VARCHAR NOT NULL,
	beer_style VARCHAR,
	alchol_by_volume FLOAT,
	availability VARCHAR,
	state VARCHAR,
	brewery_name VARCHAR,
	FOREIGN KEY (id) REFERENCES beer_id_table(id));
SELECT * FROM beer_profile_table;

-- Create Brewery Location Info Table----------------------
DROP TABLE IF EXISTS brewery_location_table;
CREATE TABLE brewery_location_table (
	brewery_id INT NOT NULL,
	brewery_name VARCHAR NOT NULL,
	city VARCHAR,
	state VARCHAR,
	country VARCHAR,
	FOREIGN KEY (brewery_id) REFERENCES brewery_id_table(brewery_id));
SELECT * FROM brewery_location_table;

--Create Beer Reviews Table----------------------------------
DROP TABLE IF EXISTS review_table;
CREATE TABLE review_table (
	id INT NOT NULL,
	name VARCHAR NOT NULL,
	beer_style VARCHAR,
	alchol_by_volume FLOAT,
	review_overall FLOAT,
	review_aroma FLOAT,
	review_appearance FLOAT,
	review_taste FLOAT,
	review_time TIMESTAMP,
	FOREIGN KEY (id) REFERENCES beer_id_table(id));
	SELECT * FROM review_table;

-- Create Adjusted Beer Review Table------------------------
DROP TABLE IF EXISTS adjusted_table;
CREATE TABLE adjusted_table (
	id INT NOT NULL,
	review_overall_adjusted	FLOAT,
	review_aroma_adjusted FLOAT,	
	review_appearance_adjusted FLOAT,
	review_palate_adjusted	FLOAT,
	review_taste_adjusted FLOAT,
	FOREIGN KEY (id) REFERENCES beer_id_table(id));
	SELECT * FROM adjusted_table;