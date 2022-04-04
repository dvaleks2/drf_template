
CREATE DATABASE drf_project_db;
CREATE USER drf_project_user with password 'drf_project_password';
ALTER ROLE drf_project_user SET CLIENT_ENCODING TO 'utf8';
ALTER ROLE drf_project_user SET DEFAULT_TRANSACTION_ISOLATION TO 'read committed';
ALTER ROLE drf_project_user SET TIMEZONE TO 'UTC'; 
GRANT ALL PRIVILEGES ON DATABASE drf_project_db to drf_project_user;