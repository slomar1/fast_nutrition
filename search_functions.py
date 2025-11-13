from data import sample_data




def find_food_by_max_calories(max_cals):

    result = []

    for i in sample_data:
        if i["calories"] <= max_cals:
            result.append(f"{i["restaurant"]} {i["name"]}")

    return result


def find_food_by_min_calories(min_cals):

    result = []

    for i in sample_data:
        if i["calories"] >= min_cals:
            result.append(f"{i["restaurant"]} {i["name"]}")

    return result


def find_food_by_min_protein(min_protein):

    result = []

    for i in sample_data:
        if i["protein_g"] >= min_protein:
            result.append(f"{i["restaurant"]} {i["name"]}")

    return result


def find_food_by_max_fat(max_fat):

    result = []

    for i in sample_data:
        if i["fat_g"] <= max_fat:
            result.append(f"{i["restaurant"]} {i["name"]}")

    return result


def find_food_by_min_fat(min_fat):

    result = []

    for i in sample_data:
        if i["fat_g"] >= min_fat:
            result.append(f"{i["restaurant"]} {i["name"]}")

    return result


def find_food_by_max_carbs(max_carbs):

    result = []

    for i in sample_data:
        if i["carbs_g"] <= max_carbs:
            result.append(f"{i["restaurant"]} {i["name"]}")

    return result