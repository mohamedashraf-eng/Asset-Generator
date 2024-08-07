import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PROJECT_ROOT_DIR = ROOT_DIR
PROJECT_TEST_DIR = f"{PROJECT_ROOT_DIR}/test"
PROJECT_SRC_DIR = f"{PROJECT_ROOT_DIR}/src"
PROJECT_LOGGING_DIR = f"{PROJECT_ROOT_DIR}/.cache"

PROJECT_TEMPLATE_DIR = f"{PROJECT_ROOT_DIR}/data/templates/"

JSON_CFG_DIR = PROJECT_ROOT_DIR
JSON_CFG_NAME = "config.json"

YAML_CFG_DIR = PROJECT_ROOT_DIR
YAML_CFG_NAME = "config.yml"

OUTPUT_DIR = f"{PROJECT_ROOT_DIR}/out"

PROJECT_NAME = f"wxk"

RUN_FORMATTER = False
FORMATTER_SCRIPT_PATH = f"{PROJECT_ROOT_DIR}/data/formatters/clang/.clang-format"

# Module configuration
WHOLE_MODULE_DIR = True
MODULE_ALL_SMALL_CASE = True

MODULE_DIR_EXTRA_EXT = ""
MODULE_SOURCES_DIR_NAME = "core"
MODULE_TESTS_DIR_NAME = "tests"
MODULE_TOOLS_DIR_NAME = "tools"

MODULE_CMAKE_INCLUDED = True
MODULE_CMAKE_DIR_NAME = "CMake"
