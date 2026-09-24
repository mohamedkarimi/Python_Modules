def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str):
    from .light_validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    if "VALID" in validation_result:
        return f"Light spell '{spell_name}' recorded"
    return f"Light spell '{spell_name} rejected'"
