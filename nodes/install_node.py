import sys
from configparser import ConfigParser
from pathlib import Path
from git import Repo

# # Legg til scripts/ i sys.path (2 nivåer opp fra install_node.py)
# scripts_dir = Path(__file__).parent.parent
# sys.path.insert(0, str(scripts_dir))


from settings import config
from common import git_installer, pipInstall_file, log
from nodes import node_registry


### Install nodes
def Install_node(settings: ConfigParser, node_info:dict):

    log(f"Installing node {node_info["name"]}")
    repo: Repo = git_installer.install(repo=node_info["repo"], dir=Path(settings["Paths"]["COMFYUI_NODES_DIR"], node_info["name"])) # type: ignore # , node_folder=node_info["name"])

    log(f"Installing requirements for node: {node_info[0]}")
    requirements = Path(repo.working_dir, "\\requirements.txt")
    pipInstall_file(req_file=requirements)
    pass

def Install_nodes(settings:ConfigParser, nodes: dict):
    for node in nodes:
        n = nodes[node]
        Install_node(settings=settings, node_info=nodes[node])
    pass

def get_repo_section(section: str):
    r: dict = node_registry(section)
    return r


# For testing this script:
if __name__ == "__main__":
    # Install_node(settings=config(), repo_url="https://github.com/ssitu/ComfyUI_UltimateSDUpscale")
    
    # Get list of repo URLs
    # t = get_repo_section("Default")

    # Install multiple nodes:
    node_list = get_repo_section("Default")
    setting = config(isDebug=True)
    Install_nodes(settings=setting, nodes=node_list)

    pass