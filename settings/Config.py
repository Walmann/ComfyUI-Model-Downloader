import configparser
import os
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Button, DirectoryTree, Label
from textual.containers import Horizontal


from common.log import log


class __FolderPickerApp(App):
    def compose(self) -> ComposeResult:
        yield Label("Velg en mappe:")
        yield DirectoryTree(Path("/"))  # startsti her
        with Horizontal():
            yield Label("", id="chosen")
            yield Button("Bekreft", variant="primary", id="ok")

    def on_directory_tree_directory_selected(
        self, event: DirectoryTree.DirectorySelected
    ) -> None:
        # Kalles hver gang brukeren trykker Enter/dobbeltklikker på en mappe
        self.chosen_path = event.path
        self.query_one("#chosen", Label).update(str(event.path))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if hasattr(self, "chosen_path"):
            self.exit(self.chosen_path)  # returnerer valgt mappe fra app.run()

def config(isDebug = False):
    config = configparser.ConfigParser()
    # Add sections and key-value pairs
    # config.add_section('Default') 
    # config.set("Default",'REPO_URL', os.getenv("GIT_REPO_URL", "https://github.com/YOUR-REPO/setup.git"))
    # config.set("Default",'REPO_BRANCH', os.getenv("GIT_REPO_BRANCH", "main"))


    config.add_section('API_Key') 
    config.set("API_Key","HF_TOKEN", os.getenv("HF_TOKEN", ""))
    config.set("API_Key","CIVITAI_API_KEY", os.getenv("CIVITAI_API_KEY", "") )

    config.add_section('ComfyUI') 
    config.set("ComfyUI","Extra_Args", str(os.getenv("EXTRA_ARGS")))

    config.add_section("ModelDownload")
    config.set("ModelDownload", "MiniMaxH3", os.getenv("DlMiniMaxH3", "True"))
    
    config.add_section('Ports') 
    config.set("Ports","COMFY_PORT", os.getenv("COMFY_PORT", "8188"))
    config.set("Ports","OLLAMA_PORT", os.getenv("OLLAMA_PORT", "11434"))
    config.set("Ports","JUPYTER_PORT", os.getenv("JUPYTER_PORT", "8888"))


    config.add_section('Paths') 

    # Set workspace dir. 
    temp = os.getenv("WORKSPACE")
    if os.getenv("WORKSPACE") == None:# and isDebug is False:
        log("Trying to find ComfyUI folder using know locations")
        knownComfyLocations= [
            "/workspace/runpod-slim",
            "/workspace",
        ] # TODO Are there more locations? 

        for d in knownComfyLocations:
            if Path.is_dir(Path(d)):
                os.environ["WORKSPACE"] = str(d)
                break
        else:
            log("Workspace not found! Please select workspace folder! (The folder containing ComfyUI folder)")
            if isDebug:
                selectedFolder = "/workspaceDEBUG"
            else:
                selectedFolder = __FolderPickerApp().run()
            os.environ["WORKSPACE"] =  str(selectedFolder)

        log(os.getenv("WORKSPACE"))
        pass
        

    
    config.set("Paths","WORKSPACE",             str(os.getenv("WORKSPACE")))
    config.set("Paths","COMFYUI_DIR",           str(Path(config.get("Paths", "WORKSPACE") +"/ComfyUI")))
    config.set("Paths","COMFYUI_MODELS_DIR",    str(Path(config.get("Paths", "COMFYUI_DIR") +"/models")))
    config.set("Paths","COMFYUI_NODES_DIR",     str(Path(config.get("Paths", "COMFYUI_DIR") + "/custom_nodes",)))
    config.set("Paths","REPO_DIR",              str(Path(config.get("Paths", "WORKSPACE") + "/RunpodComfy")))
    
    # # Write the configuration to a file
    # log("Writing configuration to file", "DEBUG")
    # with open('config.ini', 'w') as configfile:
    #     config.write(configfile)

    if isDebug:
        config.set("Paths","WORKSPACE",str(Path("/workspaceDEBUG")))

    return config


    
if __name__ == "__main__":
    c = config(isDebug=True)
    d = config(isDebug=True)
    pass


# # ============================================================
# # CONFIGURATION — All values can be overridden via RunPod ENV
# # ============================================================

# REPO_URL = os.getenv("GIT_REPO_URL", "https://github.com/YOUR-REPO/setup.git")
# REPO_BRANCH = os.getenv("GIT_REPO_BRANCH", "main")

# # API Keys
# HF_TOKEN = os.getenv("HF_TOKEN", "")
# CIVITAI_API_KEY = os.getenv("CIVITAI_API_KEY", "") 

# # Ports — Also configured in RunPod web console
# COMFY_PORT = os.getenv("COMFY_PORT", "8188")
# OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")
# JUPYTER_PORT = os.getenv("JUPYTER_PORT", "8888")

# # Paths
# WORKSPACE = Path("/workspace")
# COMFYUI_DIR = WORKSPACE / "ComfyUI"
# COMFYUI_MODELS_DIR = WORKSPACE / "ComfyUI/models"
# COMFYUI_NODES_DIR = WORKSPACE / "ComfyUI/custom_nodes"
# REPO_DIR = ""