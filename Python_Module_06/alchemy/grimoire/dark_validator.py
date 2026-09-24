from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    for ingredient in allowed:
        if ingredient.lower() in ingredients_lower:
            return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
