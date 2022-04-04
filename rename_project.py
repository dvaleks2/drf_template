import subprocess
import os


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
    print('This script will rename existing DRF project')
    old_name = input('enter current (old) django project name:\n')
    print('')
    new_name = input('enter new django project name:\n')
    print('')

    cwd = os.getcwd()
    project_path = os.path.join(cwd, old_name)
    new_project_path = os.path.join(cwd, new_name)
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

    for filepath in (manage_path, wsgi_path, asgi_path):
        replace_str_in_file(filepath,
                            [f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{old_name}.settings')",
                             f"os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{new_name}.settings')"])

    replace_str_in_file(urls_path,
                        [f"from {old_name} import settings",
                         f"from {new_name} import settings"])
    print(f'replaced {old_name} with {new_name} in\n'
          f'- settings.py\n'
          f'- manage.py\n'
          f'- urls.py\n'
          f'- wsgi.py\n- asgi.py\n')

    # for filepath in (os.path.join(cwd, '.gitlab-ci.yml'),
    #                  os.path.join(cwd, 'Dockerfile'),
    #                  os.path.join(cwd, 'Dockerfile.nginx'),
    #                  os.path.join(cwd, f'{old_name}.conf'),
    #                  os.path.join(cwd, 'dp-celery.yml'),
    #                  os.path.join(cwd, 'dp-beat.yml')):
    #     replace_str_in_file(filepath, old_name, new_name)
    #
    # # rename project.conf
    # cmd = ['mv', os.path.join(cwd, f'{old_name}.conf'),
    #        os.path.join(cwd, f'{new_name}.conf')]
    # subprocess.run(cmd)
    #
    # print(f'replaced {old_name} with {new_name} in:\n'
    #       f'- Dockerfile\n- Dockerfile.nginx\n'
    #       f'- .gitlab-ci.yml\n'
    #       f'- dp-celery.yml\n'
    #       f'- dp-beat.yml\n'
    #       f'- <project>.conf (renamed to {new_name}.conf)\n')

    # rename folders
    cmd = ['mv', django_project_folder, new_django_project_folder]
    subprocess.run(cmd)
    cmd = ['mv', project_path, new_project_path]
    subprocess.run(cmd)
    print(f'renamed folders from {old_name} to {new_name}\n')

    # should_do = input('(?) Replace <project-name> in dp.yml and dp-nginx.yml? y/n\n'
    #                   'Will replace hyphened project name *\n'
    #                   '- project name where " _ " is replaced with " - "\n')
    # if should_do.lower() == 'y':
    #     old_hyphened_name = old_name.replace('_', '-')
    #     new_hyphened_name = new_name.replace('_', '-')
    #     for filepath in (os.path.join(cwd, 'dp.yml'),
    #                      os.path.join(cwd, 'dp-nginx.yml')):
    #         replace_str_in_file(filepath,
    #                             [old_hyphened_name, new_hyphened_name])

    print('done!')


if __name__ == "__main__":
    main()
