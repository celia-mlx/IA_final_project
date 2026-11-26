"""Partición del texto en chunks de N palabras con solape."""
from __future__ import annotations

""" text : txt brut à découper, size : nbr max de mot par morceaux, overlap: nbr mot repeté d'un morceau a un autre"""
def chunk_text(text: str, size: int = 250, overlap: int = 50) -> list[str]:
  
    """ conditions pour emp^che des erreurs de logique ie 
    - un morceau peut pas contenir 0 mot
    - le chevauchment doit être positif mais < taille morceau
    """
    if size <= 0:
        raise ValueError("size doit être > 0")
    if not 0 <= overlap < size:
        raise ValueError("overlap doit être dans [0, size)")

    """ prépa des mots
        - decoupe txt à chaque espace ou saut ligne pour grande liste de mots
        - si text vide-> renvoie liste vide
    """
    words = text.split()
    if not words:
        return []

    """ 
    - step calcule de combien de mots on avance à chaque tour. Avec size = 250 et overlap = 50, on avance de 200 mots à chaque fois.
    """

    step = size - overlap
    chunks: list[str] = []
    for start in range(0, len(words), step):

        """ - prélève une tranche de size mots à partir de start.
            -  recolle ces mots avec des espaces pour reformer une chaîne de caractères propre, puis l'ajoute à la liste chunks.
            -  dès que la fenêtre atteint ou dépasse la fin du texte, la boucle s'arrête."""

        window = words[start : start + size]
        chunks.append(" ".join(window))
        if start + size >= len(words):
            break
    return chunks
