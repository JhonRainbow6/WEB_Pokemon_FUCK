from db import *
from model import PokemonBase


def create_pokemon(pokemon: PokemonBase,session: SessionDep):
    session.add(pokemon)
    session.commit()
    session.refresh(pokemon)

    return pokemon
