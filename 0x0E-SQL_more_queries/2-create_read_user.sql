-- creates database hbtn_0d_2 and user user_0d_2
-- create Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user without failing
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant only SELECT priviledge
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';