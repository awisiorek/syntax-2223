from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice, OpenTextfield
from questions import single, multiple, offen, selection, luecke

blatt5_1 = [
    [Lueckentext("Bei nicht allen Satzgliedern, die vom Verb abhängen handelt es sich um Ergänzungen. Die PP <i> mit der S-Bahn </i> stellt eine Angabe dar. ", {"nicht":[], "PP":["NP", "VP"], "Angabe":["Ergänzung"]})],
    [MultipleChoice("Mit welchen Tests kann die Funktion des obrigen Satzgliedes <i> mit der S-Bahn </i> festgestellt werden?", correct=["Weglassbarkeitstest", "geschehen-Test"], wrong=["Adverbialsatz-Test"])],
    [MultipleChoice("Bei welchen Sätzen wurden die Tests richtig angewendet?", correct=["Die neue Kollegin fährt zu ihrem neuen Arbeitsplatz.", "Die neue Kollegin fährt zu ihrem neuen Arbeitsplatz, und das geschieht mit der S-Bahn."], wrong=[])] 
]


blatt5_2 = [
    [SingleChoice("Um welchen Attributtyp handelt es sich bei dem Attribut <i>lang ersehnte</i>?", "Adjektivattribut", "Genitivattribut", "präpositionales Attribut", "attributiver Relativsatz")],
    [SingleChoice("Um welchen Attributtyp handelt es sich bei dem Attribut <i>der Klasse 5b</i>?", "Genitivattribut", "Adjektivattribut", "präpositionales Attribut", "attributiver Relativsatz")],
    [SingleChoice("Um welchen Attributtyp handelt es sich bei dem Attribut <i>nach Paris</i>?", "präpositionales Attribut", "Genitivattribut", "Adjektivattribut", "attributiver Relativsatz")],
    [SingleChoice("Um welchen Attributtyp handelt es sich bei dem Attribut <i>die sich aus irgendeinem Grunde immer wieder verzögert hatte</i>?", "attributiver Relativsatz", "präpositionales Attribut", "Genitivattribut", "Adjektivattribut")]
]

blatt5_3 = [
    [Lueckentext("Die Wortgruppe <i> sehr_gut </i> stellt im Satz ein Modaladverbial dar. Dieses Adverbial wird als Adjektivphrase realisiert. Innerhalb der Adjektivphrase tritt ein Adverb auf, das Wort <i> sehr </i>. Das Wort teilt mit anderen Wörtern derselben Klasse formale Eigenschaften. Die Bezeichnung \" Adverbial \" gibt die Satzgliedfunktion an. Diese lässt sich immer nur im konkreten Satz bestimmen.", {"Adverb":["Adverbial"], "Adverbial":["Adverb"], "Modaladverbial":["Lokaladverbial", "Modaladverb", "Lokaladverb"], "sehr":["gut"], "Adjektivphrase":["Nominalphrase", "Präpositionalphrase"]})]
]

blatt5_4 = [
    [MultipleChoice("Was sind Identifikationskriterien für das Subjekt?", correct=["Agenseigenschaften", "drückt häufig das Topik aus", "Kongruenz mit Verb", "steht im Nominativ"], wrong=["Patienseigenschaften", "steht im Akkusativ", "Kongruenz mit Artikel"])],
    [MultipleChoice("Was gilt <b>nicht</b> für die NP <i> ein Fehler </i> ?", correct=["Agenseigenschaften", "drückt das Topik aus"], wrong=["Patienseigenschaften", "Verb kongruiert mit NP", "steht im Nominativ"])],
    [MultipleChoice("Was spricht dafür, dass es sich bei <i> ein Fehler </i> eher um ein Objekt handelt?", correct=["Patienseigenschaften", "drückt nicht das Topik aus"], wrong=["Verb kongruiert mit NP", "steht im Nominativ", "Agenseigenschaften"])]
]

blatt5_5a = [
    [MultipleChoice("Welche Gründe sprechen für eine Klassifizierung als direktes Objekt?", correct=["unmittelbare Nachbarschaft zum Verb", "Distanzstellung nur bedingt möglich (<i>..dass man ihn des Diebstahls endlich überführt hat</i>)"], wrong=["Genitivmarkierung"])],
    [MultipleChoice("Welche im Deutschen für das Objekt typische Kriterien werden dagegen nicht erfüllt?", correct=["Passivierbarkeit", "Akkusativmarkierung"], wrong=["Relativierbarkeit (<i>..der Diebstahl, dessen man ihn endlich überführt hat</i>)"])],
]

blatt5_5b = [
    [SingleChoice("Im Englischen wird das indirekte Objekt __________. ", "präpositional angeschlossen", "kasusmarkiert")],
    [SingleChoice("Im Deutschen wird das indirekte Objekt __________. ", "kasusmarkiert", "präpositional angeschlossen")]
]

blatt5_6a = [
    [Lueckentext("Laut Weglassbarkeitstest ist die Entscheidung \"weglassbar\" gleichbedeutend damit, dass es sich um eine Angabe handelt.", {"Angabe":["Ergänzung"]})],
    [SingleChoice("Schlägt der Adverbialsatz-Test fehl, so handelt es sich um eine:", "Ergänzung", "Angabe")],
    [SingleChoice("Schlägt der geschehen-Test fehl, so handelt es sich um eine:", "Ergänzung", "Angabe")],

    [MultipleChoice("Welche Tests ergeben, dass es sich bei <i> auf das Pferd </i> im 1. Satz um eine Angabe handelt?", correct=[], wrong=["Adverbialsatz-Test", "Weglassbarkeitstest", "geschehen-Test"])],
    [MultipleChoice("Welche Tests ergeben, dass es sich bei <i> das Pferd </i> im 2. Satz um eine Angabe handelt?", correct=[], wrong=["Weglassbarkeitstest", "geschehen-Test", "Adverbialsatz-Test"])],
    [MultipleChoice("Welche Tests ergeben, dass es sich bei <i> das Pferd </i> im 3. Satz um eine Angabe handelt?", correct=["Weglassbarkeitstest"], wrong=["Adverbialsatz-Test", "geschehen-Test"])],
]

blatt5_6b = [
    [MultipleChoice("Unter der Annahmen, dass alle präpositional angeschlossenen Glieder Angaben sind: in welchen der Sätze ist das in Frage stehende Satzglied eine Angabe?", correct=["1. Satz (auf das Pferd)"], wrong=["2. Satz (das Pferd)", "3. Satz (das Pferd)"])],
    [MultipleChoice("Unter der Annahmen, dass alle Adverbiale Angaben sind: in welchen der Sätze ist das in Frage stehende Satzglied eine Angabe?", correct=["1. Satz (auf das Pferd)"], wrong=["2. Satz (das Pferd)", "3. Satz (das Pferd)"])],

    [SingleChoice("Wie könnte man abschließend das in Frage stehende Satzglied in Satz 1 charakterisieren?", "adverbiale Ergänzung", "Angabe", "fakultative Ergänzung")],
    [SingleChoice("Wie könnte man abschließend das in Frage stehende Satzglied in Satz 2 charakterisieren?", "Ergänzung", "Angabe")],
    [SingleChoice("Wie könnte man abschließend das in Frage stehende Satzglied in Satz 3 charakterisieren?", "fakultative Ergänzung", "Angabe", "adverbiale Ergänzung")],

]


blatt5_7 = [
    [SingleChoice("Handelt es sich im Satz bei der Präpositionalphrase um ein präpositionales Objekt?", "Ja", "Nein")],
    [MultipleChoice("Wieso?", correct=["fehlende Austauschbarkeit", "keine Eigensemantik", "vom Verb gefordert"], wrong=["austauschbar","trägt Eigensemantik"])]
]

blatt5_8 = [
    [Lueckentext("Im Satz hängen sowohl das Subjekt <i> Peter </i> als auch das Modaladverbial <i> gerne </i> und das Lokaladverbial <i> im Zelt </i> vom Verb <i> schlafen </i> ab, sind also Dependentien des Verbs .",{"Dependentien":["Valenzen"], "Subjekt":["Objekt"], "Modaladverbial":["Lokaladverbial"], "Lokaladverbial":["Modaladverbial"]})],
    [Lueckentext("Doch nur das Subjekt gehört zur Valenz von <i> schlafen </i>. Die Valenz bezieht sich auf die Verbindungsfähigkeit von relationalen Wörtern (Verben, Adjektiven, Substantiven), während die Dependenz Abhängigkeitsbeziehungen verschiedener Art zusammenfasst.", {"Valenz":["Dependenz"], "Dependenz":["Valenz"], "Subjekt":["Modaladverbial", "Lokaladverbial"]})]
]

blatt5_9a =[
    [MultipleChoice("Welche Kriterien stimmen?", correct=["H bestimmt die Distributionsklassen von C", "H ist obligatorisch, D kann optional sein", "H wählt D aus", "H bestimmt die morphologische Form von D", "H bestimmt den semantischen Typ von C"], wrong=["H und D sind optional"])]
]

blatt5_9b = [
    [MultipleChoice("Wie läßt sich die Einführung von einem Nicht-Terminal TV für transitive Verben (usw.) interpretieren?", correct=["Modellierung von Subkategorisierung der syntaktischen Kategorie V durch Kategorienerweiterung"], wrong=["Modellierung eines Subkategorisierungsrahmens über Merkmale im Lexikoneintrag"])]
]