import os
import shutil
import defaults

def stream_out_to_file(file_name: str, msg: str = ""):
    with open(file_name, "a") as f2w:
        f2w.write(msg)

def create_dir(dir_path: str):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

def create_file(file_path: str):
    if os.path.exists(file_path):
        backup_and_create(file_path)
    else:
        stream_out_to_file(file_path)

def backup_and_create(file_path: str):
    dir_name = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    backup_path = os.path.join(dir_name, 'backup', file_name)

    create_dir(os.path.join(dir_name, 'backup'))
    shutil.copyfile(file_path, backup_path)
    
    os.remove(file_path)
    stream_out_to_file(file_path)

def fetch_template(template_path: str) -> str:
    if os.path.exists(template_path):
        with open(template_path, 'r') as f2r:
            return f2r.read()
    else:
        print(f"Invalid path @{template_path}")
        return ""

def write_template_to_file(template_name: str, target_file: str):
    template_path = os.path.join(defaults.PROJECT_TEMPLATE_DIR, f"{template_name}_template.txt")
    content = fetch_template(template_path)
    create_file(target_file)
    stream_out_to_file(target_file, content)

out_root_dir = os.path.join(defaults.OUTPUT_DIR, defaults.PROJECT_NAME)
create_dir(out_root_dir)

def initiate_root_dir():
    files_to_create = [
        ('.gitattributes', 'gitattributes'),
        ('.gitmodules', 'gitmodules'),
        ('.gitignore', 'gitignore'),
        ('CMakeLists.txt', 'CMakeLists'),
        ('Makefile.variables', 'MakeVariables'),
        ('Makefile', 'Makefile'),
        ('Dockerfile', 'Dockerfile'),
        (f'{defaults.PROJECT_NAME}.code-workspace', 'Workspace'),
        ('build.sh', 'build')
    ]
    
    for file_name, template_name in files_to_create:
        write_template_to_file(template_name, os.path.join(out_root_dir, file_name))

def create_github_dir():
    github_dir = os.path.join(out_root_dir, '.github')
    sub_dirs = ['ISSUE_TEMPLATE', 'actions', 'workflows']
    
    create_dir(github_dir)
    for sub_dir in sub_dirs:
        create_dir(os.path.join(github_dir, sub_dir))
    
    create_file(os.path.join(github_dir, 'dependabot.yml'))
    dependabot_fill = """
# To get started with Dependabot version updates, you'll need to specify which
# package ecosystems to update and where the package manifests are located.
# Please see the documentation for more information:
# https://docs.github.com/github/administering-a-repository/configuration-options-for-dependency-updates
# https://containers.dev/guide/dependabot

version: 2
updates:
 - package-ecosystem: "devcontainers"
   directory: "/"
   schedule:
     interval: weekly
"""
    stream_out_to_file(os.path.join(github_dir, 'dependabot.yml'), dependabot_fill)
    write_template_to_file('pullrequest', os.path.join(github_dir, 'pull_request_template.md'))
    write_template_to_file('bug', os.path.join(github_dir, 'ISSUE_TEMPLATE', 'bug.yml'))
    write_template_to_file('feature', os.path.join(github_dir, 'ISSUE_TEMPLATE', 'feature.yml'))
    write_template_to_file('config', os.path.join(github_dir, 'ISSUE_TEMPLATE', 'config.yml'))

def create_devcontainer_dir():
    devcontainer_dir = os.path.join(out_root_dir, '.devcontainer')
    create_dir(devcontainer_dir)
    write_template_to_file('devcontainer', os.path.join(devcontainer_dir, '.devcontainer.json'))

def create_software_dir():
    software_dir = os.path.join(out_root_dir, 'software')
    create_dir(software_dir)
    
    software_subdirs = [
        'application', 'bsw', 'bsw/mcal', 'bsw/com',
        'common', 'common/includes', 'common/platform', 'common/stubs', 'gendata'
    ]
    for subdir in software_subdirs:
        create_dir(os.path.join(software_dir, subdir))
    
    software_files = {
        'CMakeLists.txt': """
cmake_minimum_required(VERSION 3.10)

# building software
message(STATUS "Building software")

# building bsw
add_subdirectory("${bsw}")

# building application
add_subdirectory("${app_dir}")
""",
        'application/CMakeLists.txt': """
cmake_minimum_required(VERSION 3.10)

# building application
message(STATUS "Building application")

# building application software component
add_subdirectory("${app_swc}")
""",
        'bsw/CMakeLists.txt': """
cmake_minimum_required(VERSION 3.10)

# building bsw
message(STATUS "Building BSW")

# building mcal
add_subdirectory("${mcal_dir}")
""",
        'bsw/mcal/CMakeLists.txt': """
cmake_minimum_required(VERSION 3.10)

# building bsw
message(STATUS "Building MCAL")

# building mcal swc's
# add_subdirectory("${xyz}")
"""
    }
    
    for file_path, content in software_files.items():
        target_file = os.path.join(software_dir, file_path)
        create_file(target_file)
        stream_out_to_file(target_file, content)

def create_tools_dir():
    tools_dir = os.path.join(out_root_dir, 'tools')
    create_dir(tools_dir)
    
    sub_dirs = ['build', 'build/CMake', 'build/IDE', 'frameworks']
    for sub_dir in sub_dirs:
        create_dir(os.path.join(tools_dir, sub_dir))
    
    create_file(os.path.join(tools_dir, 'build/IDE/.gitkeep'))
    cmake_files = [
        ('build/CMake/build_toolchain.cmake', 'cmake_build_toolchain'),
        ('build/CMake/test_toolchain.cmake', 'cmake_test_toolchain'),
        ('build/CMake/user.cmake', 'cmake_users'),
        ('build/CMake/cmockConfig.yml', 'cmock_config')
    ]
    
    for file_name, template_name in cmake_files:
        write_template_to_file(template_name, os.path.join(tools_dir, file_name))

def create_wiki_dir():
    wiki_dir = os.path.join(out_root_dir, 'wiki')
    create_dir(wiki_dir)
    create_file(os.path.join(wiki_dir, '.gitkeep'))

def create_doc_dir():
    doc_dir = os.path.join(out_root_dir, 'doc')
    create_dir(doc_dir)
    create_file(os.path.join(doc_dir, '.gitkeep'))

if __name__ == '__main__':
    initiate_root_dir()
    create_github_dir()
    create_devcontainer_dir()
    create_software_dir()
    create_tools_dir()
    create_wiki_dir()
    create_doc_dir()
    
    print("Done creating the project file structure")
