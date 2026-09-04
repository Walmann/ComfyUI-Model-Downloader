
import subprocess
import sys
from pathlib import Path

from .log import log


def pipInstall(modules:list):
    for e in modules:
        subprocess.check_call([sys.executable, "-m", "pip", "install", e])

def pipInstall_file(req_file:Path):
    reqs = []

    try:
        with open(req_file, "r") as file:
            for line in file.readlines():
                reqs.append(line)
        pipInstall(reqs)
    except FileNotFoundError:
        log("No requirements.txt file found. Skipping.")