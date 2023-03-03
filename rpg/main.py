


class Question:
    def __init__(self):
        self.text = ""
        self.answers = list()
        self.id = 0

    def init(self):
        pass

    def __str__(self):
        _output = ""
        _output += self.text + ":\n"
        for _i, _a in enumerate(self.answers):
            _output += str(_i) + ":" + _a[0] + "\n"
        return _output

    def get_answer(self):
        _ans = input("> ")
        return self.answers[int(_ans)][1]
        #return chose_question(self.answers[int(_ans)][1])


class Question1(Question):
    def init(self):
        super().init()
        self.id = 1
        self.text = "Jesteś studenciakiem. Dowiedziałeś się jak zrobić forka: "
        self.answers = [["Robisz go na serwerach politechniki", Question2()],
                        ["Wykorzystujesz go do zrobienia zadań do adiego", Question3()],
                        ["Rzucasz studia", 0]]


class Question2(Question):
    def init(self):
        super().init()
        self.id = 1
        self.text = "Szlag!!! Serwery uczelni nie wytrzymały przeciążenia wywołanego atakiem i zostałeś wezwany do dziekana"
        self.answers = [["Dziekan? Co ten debil chce? Nie idę tam", Question5()],
                        ["Opuszczasz egzamin z podstaw elektrotechniki i elektroniki i idziesz do dziekana", Question6()],
                        ["Srasz w gacie i rzucasz studia", Question1()]]


class Question3(Question):
    def init(self):

        super().init()
        self.id = 1
        self.text = "Brawo. Adi zaliczony na 4 jednak koledzy śmieją się żeś pizda bo nie zrobiłeś ataku"
        self.answers = [["Decydujesz się zrobić atak", Question2()],
                        ["Nie słuchasz ich i bijesz Przemka w mordę", Question4()],
                        ["Zmieniasz uczelnię. Tutaj za dużo osób wie żeś pizda", 9]]


class Question4(Question):
    def init(self):
        super().init()
        self.id = 1
        self.text = "Przemek oddał ci najmocniej jak umiał ale to nadal dość lekko"
        self.answers = [["Napierdalasz się z nim dalej w imię zasad", None],
                        ["Dajesz mu wygrać bo nie chcesz żeby stary cię wyjebał", None],
                        ["Zmieniasz uczelnię. Tutaj za dużo osób wie żeś pizda", 0]]


class Question5(Question):
    def init(self):
        super().init()
        self.id = 1
        self.text = "Olałeś dziekana. Zostałeś wyrzucony z uczelni"
        self.answers = [["Chuj z tym", None],
                        ["Nie obchodzi mnie to", None]]


class Question6(Question):
    def init(self):
        super().init()
        self.id = 1
        self.text = "A więc postanowiłeś przyjść do dziekana. Słusznie, stary ci wybaczył. Wracasz do domu"
        self.answers = [["Srasz", None],
                        ["uczysz się do egzaminu z PEIE", None]]



def main():
    question = Question1()
    #question.init()
    playing = True
    while playing:
        question.init()
        print(question)
        new = question.get_answer()
        if new == None:
            break

        question = new




if __name__ == "__main__":
    main()
