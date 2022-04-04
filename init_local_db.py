import os
from django.core.management.utils import get_random_secret_key


def replace_str_in_file(filepath, *search_replace_pairs):
    with open(filepath, "r") as file:
        x = file.read()
    with open(filepath, "w") as file:
        for pair in search_replace_pairs:
            search = pair[0]
            replace = pair[1]
            x = x.replace(search, replace)
        file.write(x)


def main():
    print('This script generates SQL to init local postgres database,\n'
          'and changes local_config.py:\n'
          '- database name\n'
          '- database user\n'
          '- database password\n')

    project_name = input('enter actual project name:\n')
    db_name = input('enter db name:\n')
    db_user = input('enter db user:\n')
    db_password = input('enter db password:\n')

    project_folder = os.path.join(os.getcwd(), project_name, project_name)
    local_config_path = os.path.join(project_folder, 'configs', 'local_config.py')

    replace_str_in_file(local_config_path,
                        ['<secret_key>', f'django-insecure-{get_random_secret_key()}'])

    replace_str_in_file(local_config_path,
                        ['<db_name>', db_name],
                        ['<db_user>', db_user],
                        ['<db_password>', db_password])

    # create sql script
    with open('init_database.sql', 'w') as file:
        cmd = f"""
CREATE DATABASE {db_name};
CREATE USER {db_user} with password '{db_password}';
ALTER ROLE {db_user} SET CLIENT_ENCODING TO 'utf8';
ALTER ROLE {db_user} SET DEFAULT_TRANSACTION_ISOLATION TO 'read committed';
ALTER ROLE {db_user} SET TIMEZONE TO 'UTC'; 
GRANT ALL PRIVILEGES ON DATABASE {db_name} to {db_user};
        """
        file.write(cmd)

    print('-'*10)
    print(f'done! Generated SQL script, '
          f'replaced database values in local_config.py')

    print('Next do:\n sudo -su postgres')
    print('psql -U postgres -f init_database.sql')

    print('')
    print('switch back to venv')
    print('python manage.py makemigrations')
    print('python manage.py migrate')
    print('python manage.py runserver')


if __name__ == "__main__":
    main()
