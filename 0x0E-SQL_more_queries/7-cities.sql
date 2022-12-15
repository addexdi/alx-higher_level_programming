-- creates a database and table on MySQL server
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use database
USE hbtn_0d_usa;
-- create a table in the database
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL UNIQUE AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCE states(id));

