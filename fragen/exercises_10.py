from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice, OpenTextfield
from questions import single, multiple, offen, selection, luecke

blatt10_1a = [
    [MultipleChoice("Beantworten Sie die beiden obigen Fragen.", correct=["74; (\'address\', \'number\')"], wrong=["74; ( \'number\', \'address\')", "\'rue Pascal\'; (\'spouse\', \'address\', \'street\')"] , inst=single)]
]

blatt10_1b = [
    [MultipleChoice("Welche Beispiele erfüllen die obige Subsumptionsbeziehung?", correct=["FS0 = [CAT = N], FS1 = [CAT = N, GEN = MASK]", "FS0 = [CAT = N, GEN = FEM], FS1 = [CAT = N, GEN = FEM]"], wrong=["FS0 = [CAT = N, GEN = MASK], FS1 = [CAT = N]", "FS0 = [CAT = N, GEN = FEM], FS1 = [CAT = DET, GEN = FEM]"])],
    [MultipleChoice("Was gilt immer für das Ergebnis der Unifikation solcher Merkmalstrukturen?", correct=["Es ist die spezifischere Merkmalsstruktur."], wrong=["Es ist die allgemeinere Merkmalsstruktur.", "Es ist undefiniert."], inst=single)]
]

blatt10_1c = [
    [MultipleChoice("Welche der Beispiele erfüllen die Subsumptionsbeziehung aus 1b nicht?", wrong=["FS0 = [CAT = N], FS1 = [CAT = N, GEN = MASK]", "FS0 = [CAT = N, GEN = FEM], FS1 = [CAT = N, GEN = FEM]"], correct=["FS0 = [CAT = N, GEN = MASK], FS1 = [CAT = N]", "FS0 = [CAT = N, GEN = FEM], FS1 = [CAT = DET, GEN = FEM]", "FS0 = [CAT = DET], FS1 = [CAT = N, GEN = MASK]"])]
]

blatt10_1d = [
    [MultipleChoice("Im Falle, dass im Zuge einer Unifikation Informationen zum Wert eines Pfades x hinzugefügt werden, wie verändern sich die Werte aller zu x äquivalenten Pfade?", correct=["Sie werden aktualisiert."], wrong=["Sie werden gelöscht.", "Sie werden neu eingefügt."], inst=single)]
]

blatt10_1e = [
    [MultipleChoice("Wie läßt sich im NLTK ein äquivalenter Pfad definieren?", correct=["Variable: -> (1)", "?x"], wrong=["Variable: <- (1)", "x?", "!x", "x!"])]
]