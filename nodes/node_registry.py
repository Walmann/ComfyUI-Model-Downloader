


import configparser
import os
from pathlib import Path

# from common.log import log


def node_registry(category:str):
    models: dict = {
        "Default": {
            "ComfyUI-KJNodes": {
                "name": "ComfyUI-KJNodes",
                "repo": "https://github.com/kijai/ComfyUI-KJNodes.git",
                "subdir": "ComfyUI-KJNodes"
            },
            "ComfyUI-VideoHelperSuite": {
                "name": "ComfyUI-VideoHelperSuite",
                "repo": "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git",
                "subdir": "ComfyUI-VideoHelperSuite"
            },
            "rgthree-comfy": {
                "name": "rgthree-comfy",
                "repo": "https://github.com/rgthree/rgthree-comfy.git",
                "subdir": "rgthree-comfy"
            },
        },
        "MiniMaxH3": {
            "ComfyUI-Spectrum-MiniMax-H3": {
                "name": "ComfyUI-Spectrum-MiniMax-H3",
                "repo": "https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3.git"
            },
            # "krea2_turbo_fp8_scaled.safetensors": {
            #     "repo": "https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3.git"
            # },
        },
    }
   
    return models[category]


if __name__ == "__main__":
    conf = node_registry("Default")
    for key in conf:
        print(str(key, conf[key]))

pass

