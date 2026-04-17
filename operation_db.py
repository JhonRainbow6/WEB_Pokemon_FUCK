from sqlmodel import Session
from model import PokemonBase, PokemonID


def create_pokemon_db(pokemon:PokemonBase, session: Session):
    new=PokemonID.model_validate(pokemon)
    session.add(new)
    session.commit()
    session.refresh(new)

    return new
