to init project do:

create and activate venv
pip install -r requirements.txt
python rename_project.py
python init_local_db.py
sudo -su postgres
psql -U postgres -f init_database.sql

also:
cd configs/
python create_example_cfg_from_local.py
python create_kuber_cfg_from_local.py
