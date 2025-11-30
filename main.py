from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

from state import State


# hide_debug_information()
# set_website_title("Your Drafter Website")
# set_website_framed(False)


@route
def index(state: State) -> Page:
    return Page(state, ["Hello ___!"])


start_server(State())
