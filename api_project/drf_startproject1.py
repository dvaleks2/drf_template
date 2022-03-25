import subprocess
import os


def replace_str_in_file(filepath, search, replace):
    with open(filepath, "rt") as file:
        x = file.read()
    with open(filepath, "wt") as file:
        x = x.replace(search, replace)
        file.write(x)


def main():
    print('This script will create DRF project')
    project_name = input('enter project name (will do django-admin startpoject <project_name>):\n')
    db_name = input('enter db name (will create postgres local database):\n')
    db_user = input('enter db user:\n')
    db_password = input('enter db password:\n')

    cmd = ['django-admin', 'startproject', project_name]
    subprocess.run(cmd)
    # res = subprocess.run(cmd, stdout=subprocess.PIPE)
    # res = res.stdout.decode('utf-8')

    # copy configs folder to project
    configs_path = f'{project_name}/{project_name}/configs'
    cmd = ['cp', '-r', 'configs_template', configs_path]
    subprocess.run(cmd)

    # set <secret_key> from settings to local_config
    settings_path = f'{project_name}/{project_name}/settings.py'
    local_config_path = os.path.join(configs_path, 'local_config.py')
    with open(settings_path, 'r') as file:
        for line in file:
            if line.startswith('SECRET_KEY'):
                sk = line.split(' ')[2].strip().replace("'", "")
                replace_str_in_file(local_config_path, '<secret_key>', sk)
                break

    replace_str_in_file(local_config_path, '<db_name>', db_name)
    replace_str_in_file(local_config_path, '<db_user>', db_user)
    replace_str_in_file(local_config_path, '<db_password>', db_password)

    # set <project_name> in settings.py
    project_path = os.path.join(os.getcwd(),
                                project_name, project_name)
    filepath = os.path.join(project_path, 'configs', 'settings.py')
    replace_str_in_file(filepath, '<project_name>', project_name)

    # move settings.py from configs_template to project folder
    cmd = ['mv', filepath, settings_path]
    subprocess.run(cmd)

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
    print(f'done! Initialized {project_name} with configs')

    print('do:\n sudo -su postgres')
    print('psql -U postgres -f init_database.sql')

    print('')
    print('python manage.py makemigrations')
    print('python manage.py migrate')
    print('python manage.py runserver')


if __name__ == "__main__":
    main()
