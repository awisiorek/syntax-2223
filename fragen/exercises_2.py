from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice
from questions import single, multiple, offen, selection, luecke




blatt2_1a = [
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 1 zugrunde?","Regelsystem","Regelbuch", "formale Grammatik","Theorie der Sprachstruktur", "Wissen um Sprachstruktur", sonst=False, inst=single)],
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 2 zugrunde?","Regelbuch", "Regelsystem", "formale Grammatik","Theorie der Sprachstruktur", "Wissen um Sprachstruktur", sonst=False, inst=single)],
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 3 zugrunde?","Theorie der Sprachstruktur", "Regelbuch", "Regelsystem", "formale Grammatik", "Wissen um Sprachstruktur", sonst=False, inst=single)]
    ]

blatt2_1b = [
    [MultipleChoice("Welche Gesetzmäßigkeiten umfasst die Grammatik als Regelsystem?", correct=["phonologische", "morphologische", "syntaktische"],wrong=["semantische", "pragmatische"],sonst=False, inst=multiple)],
    [Lueckentext("Die Syntax ist ein Teilbereich der Grammatik, der sich auf die syntaktischen Regularitäten bezieht.", {"Teilbereich":["Oberbegriff","Synonym"], "syntaktischen":["morphologischen","phonologischen","semantischen"]},inst=luecke)]
    ]




blatt2_2 = [
    [Lueckentext("Für die Blätter gilt: natürlichsprachliche Wörter sind eine Teilmenge aus dem Alphabet der Grundsymbole der formalen Sprache; ein analysierter natürlichsprachlicher Satz ist ein in der formalen Grammatik ableitbares Wort der formalen Sprache.", {"Wort":["Morphem","Symbol"], "Grundsymbole":["Nicht-Terminale"]},inst=luecke)]
    ]    




blatt2_3a = [
    [MultipleChoice("Welche Typen von Syntaxbäumen (auch: Parsebäume, Ableitungsbäume) wurden gezeigt?", correct=["Konstituentenbaum mit Phrasenlabels als Knoten","Dependenzgraph mit gelabelten Kanten"],wrong=["Konstituentenbaum mit gelabelten Kanten", "Dependenzgraph mit Phrasenlabels als Knoten"],sonst=False, inst=multiple)]
    ]

blatt2_3b = [
    [SingleChoice("In welcher Form wird die syntaktische Struktur eines Satzes beim Aufruf von NLTK print(tree) erstellt?","Klammernotation","Baumdiagramm", sonst=True, inst=single)],
    [SingleChoice("In welcher Form wird die syntaktische Struktur eines Satzes beim Aufruf von NLTK tree.pretty_print() erstellt?","Baumdiagramm", "Klammernotation", sonst=True, inst=single)]
    ]




    
blatt2_4a = [
    [MultipleChoice("Hinsichtlich welcher syntaktischen Grundprinzipien werden natürliche Sprachen mit formalen Methoden analysiert?", correct=["Konstituenz", "Dependenz"],wrong=["Synonymie", "Korrektheit"],sonst=False, inst=multiple)],
    [SingleChoice("Konstituenz ist synonym zu:","Phrasenstruktur","Dependenz", "Abhängigkeitsstruktur", "Wortstruktur", sonst=True, inst=single)],
    [SingleChoice("Dependenz ist synonym zu:","Abhängigkeitsstruktur", "Phrasenstruktur", "Konstituenz",  "Wortstruktur", sonst=True, inst=single)],
    ]

blatt2_4b = [
    [SingleChoice("Welche Mittel kommen in einer formalen Syntaxanalyse zum Einsatz?", "formale Grammatik + Parser", "Parsebäume", "formale Grammatik", "Parser", sonst=False, inst=single)],
    ]

blatt2_4c = [
    [MultipleChoice("Die ________ eines Satzes bzgl. der formalen Grammatik wird erkannt.", correct=["Wohlgeformtheit", "Grammatikalität"],wrong=["Sinnhaftigkeit"],sonst=False, inst=multiple)],
#     [SingleChoice("Bei einer solchen Analyse wird welche ja/nein-Entscheidung unweigerlich getroffen?","Wohlgeformtheit", "Sinnhaftigkeit", "Korrektheit", sonst=True, inst=single)],
    ]

blatt2_4d = [
    [MultipleChoice("Welche Vorteile hat die Modellierung der Satzstruktur mit Hilfe einer formalen Grammatik?", correct=["Eine unendliche Menge an Sätzen kann mit endlichen Mitteln beschrieben werden.", "Eine automatische Strukturanalyse wird möglich."], wrong=["Eine endliche Menge an Sätzen kann mit unendlichen Mitteln beschrieben werden."], inst=multiple)]
    ]

