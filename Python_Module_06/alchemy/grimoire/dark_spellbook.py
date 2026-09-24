from .dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients():
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str):
    validation_result = validate_dark_ingredients(ingredients)
    if "VALID" in validation_result:
        return f"Dark spell '{spell_name}' recorded"
    return f"Dark spell '{spell_name}' rejected"
