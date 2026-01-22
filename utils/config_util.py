import os

import yaml

from utils import get_project_root_path

project_root_path = get_project_root_path()
# 配置文件夹路径
config_parent_path = os.path.join(project_root_path, "config")


def load_yaml_config(config_path: str):
    with open(config_path, "r", encoding="UTF-8") as f:
        return yaml.safe_load(f)


prompt_config = load_yaml_config(os.path.join(config_parent_path, "prompt_config.yaml"))
