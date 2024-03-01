
from souhaiel import Calculs;
from wissem import GestionChaine;

def main():
    ma_liste = ["a", "b", "c"]
    calculs_instance = Calculs(ma_liste)
    calculs_instance.afficher_liste()
    calculs_instance.modifier_liste(0, "3")
    calculs_instance.afficher_liste()

    chaine = "Bonjour, monde!"

    chaine_majuscule = GestionChaine.convertir_en_majuscule(chaine)
    print("Chaîne en majuscule :", chaine_majuscule)

    longueur_chaine = GestionChaine.calculer_longueur_chaine(chaine)
    print("Longueur de la chaîne :", longueur_chaine)

if __name__ == "__main__":
    main()

