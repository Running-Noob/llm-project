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

prompt_config_dict = {
    "system_prompt": prompt_config["system_prompt"],
    "travel_agent_prompt": prompt_config["travel_agent_prompt"],
    "delimiter": prompt_config["delimiter"],
    "react_prompt_template": prompt_config["react_prompt_template"],
    "planner_prompt_template": prompt_config["planner_prompt_template"],
    "executor_prompt_template": prompt_config["executor_prompt_template"]
}

if __name__ == "__main__":
    print(prompt_config_dict)
