import sys
from textual.app import App, ComposeResult
from textual.widgets import SelectionList, Button, DirectoryTree, Label
from textual.widgets.selection_list import Selection
from textual.containers import Horizontal
from pathlib import Path

from common import log
from settings import config
from models import modelInstaller

class MultiSelectApp(App):
    def compose(self) -> ComposeResult:
        yield SelectionList(
            Selection("MiniMax H3", "minimaxh3"),
        )
        yield Button("Kjør videre", variant="primary", id="run")
    def on_selection_list_selected_changed(self, event: SelectionList.SelectedChanged) -> None:
        self.sub_title = str(event.selection_list.selected)

    def on_button_pressed(self, event: Button.Pressed) -> None:

        # Hent alle valgte verdier
        selected = self.query_one(SelectionList).selected
        print(f"Valgte elementer: {selected}")  # f.eks. ['apple', 'cherry']
        self.exit(selected )

class FolderPickerApp(App):
    def compose(self) -> ComposeResult:
        yield Label("Velg en mappe:")
        yield DirectoryTree(Path.home())  # startsti her
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


def main(dryRun=False):

    settings = config()


    log("Checking if we are in a python venv.", "DEBUG")
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        log("We are already inside a Venv. Yhay!")
    else:
        log("We are not in a Venv. #TODO Handle this. We should be in a Venv, if some models require custom nodes.", "WARNING")


    log("Trying to find ComfyUI folder using know locations")
    knownComfyLocations= [
        "/workspace",
        "/workspace/runpod-slim"
    ] # TODO Are there more locations? 

    for d in knownComfyLocations:
        if Path.is_dir(d):
            settings.set("Paths","WORKSPACE", str(d))
            break
    else:
        log("Workspace not found! Please select workspace folder! (The folder containing ComfyUI folder)")
        selectedFolder = FolderPickerApp().run()
        settings.set("Paths","WORKSPACE", str(selectedFolder))
        pass

    log("Starting UI for downloading models.")
    app = MultiSelectApp()
    modelList = app.run()

    log("Installing models")
    modelInstaller(modelList= modelList, settings=settings, dryRun=dryRun)

    pass



if __name__ == "__main__":
    main(dryRun=True)

    pass
