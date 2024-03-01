class Cal:
    @staticmethod
    def calculerSomme(tableau):
        somme = sum(tableau)
        return somme

    @staticmethod
    def calculerMoyenne(tableau):
        if tableau:
            moyenne = sum(tableau) / len(tableau)
            return moyenne
        else:
            return 0.0
