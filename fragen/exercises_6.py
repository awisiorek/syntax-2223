from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice, OpenTextfield
from questions import single, multiple, offen, selection, luecke

blatt6_1 = [
    [SingleChoice("Wie wird die Deklination der Nominalphrase <i>altes Bier</i> auch bezeichnet?", "starke Deklination", "schwache Deklination", sonst=True)],
    [SingleChoice("Wie wird die Deklination der Nominalphrase <i>das alte Bier</i> auch bezeichnet?", "schwache Deklination", "starke Deklination", sonst=True)],
    [SingleChoice("Für die Deklination ist hier relevant, ob das Adjektiv mit einem ____________ Artikel auftritt oder nicht.", "bestimmten", "unbestimmten")],
    [MultipleChoice("Welche Aussagen über Adjektive stimmen?", correct=["Die Form des Adjektivs richtet sich nach dem Genus des Substantivs."], wrong=["Die Form vom Adjektiven hängt niemals von irgendeinem Genus ab.", "Das Genus des Adjektivs ist lexikalisch fix definiert."])],
    [MultipleChoice("Welche Aussagen gelten für Nominalphrasen mit bestimmtem Artikel?", correct= ["Der Artikel übernimmt die Genusmarkierung.", "Der Artikel übernimmt z. T. die Kasusmarkierung.", "Das Adjektiv tritt nur in zwei verschiedenen Formen auf."], wrong=["Die Endungen von Adjektiv und Artikel stimmen überein.", "Die Form des Adjektivs ist in jedem Kasus unterschiedlich."])],
    [MultipleChoice("Welche Aussagen gelten für den Fall, dass das Adjektiv in einer NP ohne Artikel auftritt? (vgl. <i>altes Bier</i>)", correct=["Das Adjektiv übernimmt die Endungen des Artikels.", "Das Adjektiv übernimmt die Genus- und z.T. die Kasusmarkierung."], wrong=["Das Fehlen des Artikels hat keine Auswirkungen auf das Adjektiv."])]
]

blatt6_2 = [
    [SingleChoice("Schildern beide Sätze denselben Sachverhalt?", "Ja", "Nein")],
    [MultipleChoice("Welche syntaktischen Unterschiede bestehen?", correct=["Passivierung (Objekt-Promotion)", "Subjekt-Demotion zu Adverbial"], wrong=["Perspektivierung", "Ausrichtung der Empathie"])],
    [MultipleChoice("Welche kommunikativ-funktionalen Unterschiede bestehen?", correct=["Perspektivierung", "Ausrichtung der Empathie"], wrong=["Passivierung (Objekt-Promotion)", "Subjekt-Demotion zu Adverbial"])]
]

blatt6_3 = [
    [Lueckentext("In Verbindung mit einem Personalpronomen wird das Adjektiv hier stark dekliniert. Dies mag daran liegen, dass die Personalpronomina keine Genusmerkmale realisieren. Das Adjektiv muss also, wie auch beim Fehlen des bestimmten Artikels, die Genusmarkierung übernehmen.", {"Personalpronomen":["Nomen", "Adverbial"], "stark":["schwach", "nicht"], "Personalpronomina":["Nomen","Adverbiale"], "Genusmerkmale":["Kasusmerkmale"], "Genusmarkierung":["Kasusmarkierung"]})]
]

blatt6_4a = [
    [MultipleChoice("Wie werden Features beim POS-Tagging verwendet?", correct=["Sie werden aus der Eingabe extrahiert (feature extraction)"], wrong=["Sie werden im Vorhinein deklariert (feature lexicon)"], sonst=True, inst=single)],
    [MultipleChoice("Wie werden Features in formalen Grammatiken verwendet?", correct=["Sie werden im Vorhinein deklariert (feature lexicon)"], wrong=["Sie werden aus der Eingabe extrahiert (feature extraction)"], sonst=True, inst=single)]
]

blatt6_4b = [
    [SingleChoice("Welche native python-Datenstruktur bietet sich für die Deklaration von Merkmalstrukturen als Menge von Attribut-Wert-Paaren an?", "dictionary", "list", "stack", "tuple")]
]

blatt6_4c = [
    [SelectionList("Um welchen Faktor erhöht sich die Regelanzahl, wenn man Kongruenz (Agreement) in Numerus und Person durch Integration von Merkmalen in die Kategoriensymbole einer CFG modelliert (S → NP_1_SG VP_1_SG usw.)?", "6", "1", "2", "4", "8", "10", inst=single)]
]
