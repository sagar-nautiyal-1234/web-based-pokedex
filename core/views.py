from django.shortcuts import render
from .services import (
    fetch_pokemon_list,
    fetch_pokemon_detail,
    fetch_pokedex_region
)

# -----------------------------------------------------
# HOMEPAGE: Paginated Pokémon List
# -----------------------------------------------------
def pokemon_list(request):
    page = int(request.GET.get("page", 1))
    limit = 20
    offset = (page - 1) * limit

    data = fetch_pokemon_list(limit=limit, offset=offset)

    results = data["results"]
    pokemon_list = []

    for index, p in enumerate(results, start=offset + 1):
        pokemon_list.append({
            "id": index,
            "name": p["name"].capitalize(),
            "sprite": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{index}.png"
        })

    context = {
        "pokemon_list": pokemon_list,
        "page": page,
        "has_prev": page > 1,
        "has_next": offset + limit < data["count"],
    }

    return render(request, "core/list.html", context)


# -----------------------------------------------------
# POKÉMON DETAIL PAGE
# -----------------------------------------------------
def pokemon_detail(request, name_or_id):
    data = fetch_pokemon_detail(name_or_id)

    if data is None:
        return render(request, "core/detail.html", {"not_found": True})

    types = [t["type"]["name"].capitalize() for t in data["types"]]
    stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
    abilities = [a["ability"]["name"].replace("-", " ").title() for a in data["abilities"]]

    context = {
        "id": data["id"],
        "name": data["name"].capitalize(),
        "sprite": data["sprites"]["front_default"],
        "types": types,
        "height": data["height"],
        "weight": data["weight"],
        "stats": stats,
        "abilities": abilities,
    }

    return render(request, "core/detail.html", context)


# -----------------------------------------------------
# REGION POKÉDEX VIEW (Kanto, Johto, Hoenn, etc.)
# -----------------------------------------------------
def region_pokedex(request, region_name):
    data = fetch_pokedex_region(region_name)

    if data is None:
        return render(request, "core/list.html", {"not_found": True})

    entries = data["pokemon_entries"]
    pokemon_list = []

    # Extract Pokémon name + ID
    for entry in entries:
        name = entry["pokemon_species"]["name"]

        # ID comes from Pokémon species URL
        species_url = entry["pokemon_species"]["url"]
        pokemon_id = species_url.rstrip('/').split('/')[-1]

        pokemon_list.append({
            "id": pokemon_id,
            "name": name.capitalize(),
            "sprite": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
        })

    return render(request, "core/list.html", {
        "pokemon_list": pokemon_list,
        "region_name": region_name.capitalize(),
        "has_next": False,
        "has_prev": False,
    })
