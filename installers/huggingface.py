from huggingface_hub import hf_hub_download, login, auth_list, whoami
import os

from common import log


def huggingface_setup():
    log("Authenticating with Huggingface")

    if os.getenv("HF_TOKEN") == None:
        os.environ["HF_TOKEN"] = input("Huggingface API key not found in Enviorment variable. Please paste key: ")


    login(os.getenv("HF_TOKEN"))
    log(str(whoami(token=os.getenv("HF_TOKEN"))), "DEBUG")
    log(str(auth_list()),"DEBUG")
    pass



if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    huggingface_setup()
