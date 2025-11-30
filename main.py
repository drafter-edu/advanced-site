from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

from meta import *
from state import State


@route
def index(state: State) -> Page:
    return Page(state, ["Hello ___!"])


start_server(State())
