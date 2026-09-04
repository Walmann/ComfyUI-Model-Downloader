import sys
from textual.app import App, ComposeResult
from textual.widgets import SelectionList, Button
from textual.widgets.selection_list import Selection

from common import log
from settings import config
from models import modelInstaller

class MultiSelectApp(App):
    def compose(self) -> ComposeResult:
        yield SelectionList(
            Selection("MiniMax H3", "MiniMaxH3"),
            Selection("Krea 2", "Krea2"),
        )
        yield Button("Kjør videre", variant="primary", id="run")
    def on_selection_list_selected_changed(self, event: SelectionList.SelectedChanged) -> None:
        self.sub_title = str(event.selection_list.selected)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Hent alle valgte verdier
        selected: list[str] = self.query_one(SelectionList).selected
        print(f"Valgte elementer: {selected}")  # f.eks. ['apple', 'cherry']
        self.exit(selected )
    




def main(dryRun=False):

    settings = config()


    log("Checking if we are in a python venv.", "DEBUG")
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        log("We are already inside a Venv. Yhay!")
    else:
        log("We are not in a Venv. #TODO Handle this. We should be in a Venv, if some models require custom nodes.", "WARNING")




    log("Starting UI for downloading models.")
    app = MultiSelectApp()
    modelList: list = app.run()

    log("Installing models")
    modelInstaller(modelList= modelList, settings=settings, dryRun=dryRun)

    pass



if __name__ == "__main__":
    main(dryRun=False)

    pass
