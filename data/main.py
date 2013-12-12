"""
The main function is defined here. It simply creates an instance of
tools.Control and adds the game states to its dictionary using
tools.setup_states.  There should be no need (theoretically) to edit
the tools.Control class.  All modifications should occur in this module
and in the setup module.
"""

from . import setup,tools
from .states import title,splash,menu,level1

def main():
    """Add states to control here."""
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {"SPLASH" : splash.Splash(),
                  "TITLE"  : title.Title(),
                  "MENU"   : menu.Menu(),
                  'LEVEL1'  : level1.Level_1(),
                  }
    run_it.setup_states(state_dict,"SPLASH")
    run_it.main()
