import os
import configparser
import sys

from nodes import Install_nodes, get_repo_section
from common import log
from models import huggingface
from settings import config



def modelInstaller(modelList: list, settings: configparser.ConfigParser, dryRun=False):
    setting = config()

    for m in modelList:
        try:
            try:      
                log(f"Installing {m}")
                nodes = get_repo_section(m)
                Install_nodes(settings=setting, nodes=nodes)
            except KeyError as e: 
                log(f"Could not find {m} in node database! This is fine.")

            try:
                log("Downloading MiniMaxH3 models")
                huggingface.hugginface_downloadModel(model=m, settings=setting, dryRun=dryRun)
                pass
            except KeyError as e: 
                log(f"Could not find {m} in model database!", "ERROR")
                sys.exit()
        except Exception as e:
            log(f"ERROR INSTALLING MODEL ${m}", "ERROR")
            log(e)
            sys.exit()

if __name__ == "__main__":
    modelInstaller(modelList=["MiniMaxH3", "Krea2"], settings=config(isDebug=True), dryRun=True)
    pass