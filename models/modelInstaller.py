import os
import configparser


from nodes import Install_nodes, get_repo_section
from common import log
from models import huggingface
from settings import config



def modelInstaller(modelList: list, settings: configparser.ConfigParser, dryRun=False):
    setting = config()

    
    if "minimaxh3" in modelList:
        log("Installing MiniMaxH3")
        log("SKIPPING: NODES NOT IMPLEMENTED YET!", "WARNING")
        # nodes = get_repo_section("MiniMaxH3")
        # Install_nodes(settings=setting, nodes=nodes)

        log("Downloading MiniMaxH3 models")
        huggingface.hugginface_downloadModel(model="MiniMaxH3", settings=setting, dryRun=dryRun)
        pass


if __name__ == "__main__":
    modelInstaller(modelList=["minimaxh3"], settings=config(isDebug=True), dryRun=True)
    pass