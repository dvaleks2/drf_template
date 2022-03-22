to init project do:

create and activate venv
cd api_project (rename folder if want)
pip install -r requirements.txt
python drf_startproject.py
(enter project_name, db_name, db_user, db_password)
sudo -su postgres
psql -U postgres -f init_database.sql

rm -r configs_template
rm drf_startproject.py init_database.sql

also:
cd configs/
python write_example_from_local.py
python write_kuber_from_local.py
- to create configs from local_config.py

for kuber:
replace <project_name>, <api_project> in gitlab yml files
