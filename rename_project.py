import subprocess
import os


def replace_str_in_file(filepath, *search_replace_pairs):
    with open(filepath, "rt") as file:
        x = file.read()
    with open(filepath, "wt") as file:
        for pair in search_replace_pairs:
            search = pair[0]
            replace = pair[1]
            x = x.replace(search, replace)
        file.write(x)


def main():
    print('This script will rename existing DRF project')
    old_name = input('enter current (old) django project name:\n')
    new_name = input('enter new django project name:\n')

    project_path = os.path.join(os.getcwd(), old_name)
    new_project_path = os.path.join(os.getcwd(), new_name)
    django_project_folder = os.path.join(project_path, old_name)
    new_django_project_folder = os.path.join(project_path, new_name)
    settings_path = os.path.join(django_project_folder, 'settings.py')

    manage_path = os.path.join(project_path, 'manage.py')
    wsgi_path = os.path.join(project_path, old_name, 'wsgi.py')
    asgi_path = os.path.join(project_path, old_name, 'asgi.py')
    urls_path = os.path.join(project_path, old_name, 'urls.py')

    replace_str_in_file(settings_path,
                        [f'from {old_name}.configs.',
                         f'from {new_name}.configs.'],
                        [f"ROOT_URLCONF = '{old_name}.urls'",
                         f"ROOT_URLCONF = '{new_name}.urls'"],
                        [f"WSGI_APPLICATION = '{old_name}.wsgi.application'",
                         f"WSGI_APPLICATION = '{new_name}.wsgi.application'"])

    for file_path in (manage_path, wsgi_path, asgi_path):
        replace_str_in_file(file_path,
                            [f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{old_name}.settings')",
                             f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{new_name}.settings')"])

    replace_str_in_file(urls_path,
                        [f"from {old_name} import settings",
                         f"from {new_name} import settings"])
    print(f'replaced {old_name} with {new_name} in settings.py, manage.py, urls.py, wsgi.py, asgi.py')

    # rename folders
    cmd = ['mv', django_project_folder, new_django_project_folder]
    subprocess.run(cmd)
    cmd = ['mv', project_path, new_project_path]
    subprocess.run(cmd)
    print(f'renamed fodlers from {old_name} to {new_name}')

    print('done!')


if __name__ == "__main__":
    main()
