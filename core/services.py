import requests

BASE_URL = "https://pokeapi.co/api/v2"

class PokeAPIError(Exception):
    pass


# --------------------------------------------------------
# FETCH POKÉMON LIST (Used for homepage)
# --------------------------------------------------------
def fetch_pokemon_list(limit=20, offset=0):
    url = f"{BASE_URL}/pokemon"
    params = {"limit": limit, "offset": offset}
    resp = requests.get(url, params=params, timeout=5)

    if resp.status_code != 200:
        raise PokeAPIError("Failed to fetch Pokémon list")

    return resp.json()


# --------------------------------------------------------
# FETCH SINGLE POKÉMON DETAIL (Used for /pokemon/<id>/)
# --------------------------------------------------------
def fetch_pokemon_detail(name_or_id):
    url = f"{BASE_URL}/pokemon/{name_or_id.lower()}"
    resp = requests.get(url, timeout=5)

    if resp.status_code == 404:
        return None
    if resp.status_code != 200:
        raise PokeAPIError("Error fetching Pokémon data")

    return resp.json()


# --------------------------------------------------------
# FETCH REGION VIA POKÉDEX ENDPOINT (Used for /region/<name>/)
# Example: https://pokeapi.co/api/v2/pokedex/kanto/
# --------------------------------------------------------
def fetch_pokedex_region(region_name):
    url = f"{BASE_URL}/pokedex/{region_name.lower()}"
    resp = requests.get(url, timeout=5)

    if resp.status_code == 404:
        return None
    if resp.status_code != 200:
        raise PokeAPIError("Failed to fetch region Pokédex")

    return resp.json()
