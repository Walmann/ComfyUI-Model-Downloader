import huggingface_hub
from configparser import ConfigParser
from pathlib import Path

from models import model_registry
from common import log


def hugginface_downloadModel(model: str, settings:ConfigParser, dryRun=False):
    # TODO Create multi-Thread downloading.

    modelList = model_registry()
    for item in modelList[model]:
        i = modelList[model][item]
        name = item
        repo = i["repo"]
        path = i["path"]
        subdir = i["subdir"]

        # If subdir is included in path, remove subdir from path. 
        if path[:len(subdir)] == subdir:
            path = path[len(subdir)+1:]
            # subdir = ""

        # Add the modelname to the path, for easier organisation
        subdir = Path(subdir, model)

        temp = settings["Paths"]["COMFYUI_MODELS_DIR"]
        model_dir = str(Path(settings["Paths"]["COMFYUI_MODELS_DIR"],  subdir))

        log(f"Model is being downloaded to: {model_dir}", "DEBUG")
        dryRun_results = huggingface_hub.hf_hub_download(repo_id=repo, filename=path, local_dir=model_dir, dry_run=dryRun)
        if dryRun:
            log("DryRun results: ", "DEBUG")
            log(str(dryRun_results), "DEBUG")
        pass

    pass




if __name__ == "__main__":
    from model_registry import model_registry
    from settings import config
    hugginface_downloadModel(model="MiniMaxH3", settings=config(isDebug=True), dryRun=True)
