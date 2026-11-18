def calculate_score(
    has_site,
    phone,
    category,
    instagram,
    email,
):
    score = 0

    if not has_site:
        score += 40

    if phone:
        score += 10

    if instagram and not has_site:
        score += 25

    priority_categories = [
        "advogado",
        "dentista",
        "estética",
        "estetica",
        "arquiteto",
        "arquitetura",
    ]

    if category:
        category = category.lower()

        if any(
            item in category
            for item in priority_categories
        ):
            score += 25

    if email:
        score -= 15

    return max(0, min(score, 100))