from souhaiel import Calculs;


def main():
    ma_liste = ["a", "b", "c"]
    calculs_instance = Calculs(ma_liste)
    calculs_instance.afficher_liste()
    calculs_instance.modifier_liste(0, "3")
    calculs_instance.afficher_liste()

if __name__ == "__main__":
    main()