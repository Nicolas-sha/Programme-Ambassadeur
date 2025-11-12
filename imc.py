def calculer_imc(poids_kg: float, taille_m: float) -> float:
    """
    Calcule l'indice de masse corporelle (IMC) à partir du poids et de la taille.

    Args:
        poids_kg: Le poids en kilogrammes.
        taille_m: La taille en mètres.

    Returns:
        L'IMC calculé.

    Raises:
        ValueError: Si la taille est inférieure ou égale à zéro.
    """

    if poids_kg <= 0:
        raise ValueError("Le poids doit être un nombre positif.")
    if taille_m <= 0:
        raise ValueError("La taille doit être un nombre positif.")
    return poids_kg / (taille_m ** 2)

