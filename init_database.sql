
CREATE DATABASE project_db;
CREATE USER project_user with password 'project_password';
ALTER ROLE project_user SET CLIENT_ENCODING TO 'utf8';
ALTER ROLE project_user SET DEFAULT_TRANSACTION_ISOLATION TO 'read committed';
ALTER ROLE project_user SET TIMEZONE TO 'UTC'; 
GRANT ALL PRIVILEGES ON DATABASE project_db to project_user;
        