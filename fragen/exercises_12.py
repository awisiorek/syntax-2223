from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice
from questions import single, multiple, offen, selection, luecke

blatt12_1 = [
    [
        MultipleChoice(
            "Welche der folgenden Bedingungen wird an eine PCFG gestellt?",
            ["Die Summe aller Regelwahrscheinlichkeiten für jede LHS ist jeweils 1."],
            ["Die Summe aller Regelwahrscheinlichkeiten für jede RHS ist jeweils 1.",
             "Die Summe aller Regelwahrscheinlichkeiten innerhalb einer Grammatik ist 1."],
            inst=single
        )
    ],
    [
        MultipleChoice(
            "Was ist die Aufgabe des Viterbi-Algorithmus?",
            ["Bestimmung des wahrscheinlichsten Syntaxbaums"],
            ["Finden aller Konstituenten",
             "Bestimmung der Köpfe und Dependenzrelationen"],
            inst=single
        )
    ],
]

blatt12_2a = [
    [MultipleChoice("Welche zwei Faktoren führen bei der syntaktischen Analyse natürlicher Sprache mittels formaler Grammatiken zu mehr Ambiguität (Anzahl an Ableitungen)?", correct=[
                    "Zunahme der Anzahl von Regeln", "längere Sätze"], wrong=["kürzere Sätze", "Abnahme der Anzahl von Regeln"], inst="Wählen Sie die zwei korrekten Antworten aus.")]
]

blatt12_2b = [
    [MultipleChoice("Welche zwei Arten von Ambiguität unterscheidet man hier?", correct=["strukturelle Ambiguität", "lexikalische Ambiguität"], wrong=[
                    "Attachment-Ambiguität", "Koordinierungsambigutiät"], inst="Wählen Sie die zwei korrekten Antworten aus.")]
]
