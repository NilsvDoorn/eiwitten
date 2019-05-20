# Eiwit vouwen
Eiwitten zijn essentieel voor het leven. Ze bestaan uit een aaneenschakeling van aminozuren die, afhankelijk van het type, een bepaalde interactie met elkaar aan gaan waardoor een bepaalde vouwing ontstaat.
<p>De algoritmes binnen deze map proberen de vouwing van een eiwit te voorspellen aan de hand van de aminozuurvolgorde. Hiervoor worden de aminzuren in groepen verdeeld (P, H of C) en op een grid geplaatst waarbij twee opeenvolgende aminozuren 1 stap van elkaar verwijderd liggen. De score van de vouwing wordt vervolgens bepaald door de hoeveelheid H's en C's die naast elkaar liggen. Hierbij leveren H-H en C-H 1 punt op en C-C 5 punten.

<h2>Aan de slag (Getting Started)<h2>
<h3>Vereisten (Prerequisites)</h3>
Deze codebase is volledig geschreven in Python3.6.3. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

<p>pip install -r requirements.txt

<h3>Structuur (Structure)</h3>
Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

<h3>Test (Testing)</h3>
Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:</br>

python main.py

<h2>Auteurs (Authors)</h2>
Nils van Doorn</br>
Jesse Pannekeet</br>
Thomas Verouden

<h2>Dankwoord (Acknowledgments)</h2>
StackOverflow</br>
minor programmeren van de UvA
