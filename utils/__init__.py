import os


def get_project_root_path():
    """获取项目根路径"""
    project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return project_root_path
