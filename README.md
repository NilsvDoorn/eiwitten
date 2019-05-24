# Eiwit vouwen
Eiwitten zijn essentieel voor het leven. Ze bestaan uit een aaneenschakeling van aminozuren die, afhankelijk van het type, een bepaalde interactie met elkaar aan gaan waardoor een bepaalde vouwing ontstaat.
<p>De algoritmes binnen deze folder proberen de vouwing van een eiwit te voorspellen aan de hand van de aminozuurvolgorde. Hiervoor worden de aminzuren in groepen verdeeld (P, H of C) en op een grid geplaatst waarbij twee opeenvolgende aminozuren 1 stap van elkaar verwijderd liggen. De score van de vouwing wordt vervolgens bepaald door de hoeveelheid H's en C's die naast elkaar liggen. Hierbij leveren H-H en C-H 1 punt op en C-C 5 punten.

<h3>Aan de slag (Getting Started)<h3>
<h4>Vereisten (Prerequisites)</h4>
Deze codebase is volledig geschreven in Python3.6.3. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip d.m.v. de volgende instructie:</br>

<p>pip install -r requirements.txt

<h4>Structuur (Structure)</h4>
Alle Python scripts staan in de folder 'code'. In de folder 'data' staan alle opgegeven aminozuurvolgorden en in de folder 'resultaten' worden alle resultaten opgeslagen door de code.

<h4>Test (Testing)</h4>
Om het programma te runnen kan de volgende command gebruikt worden in de Root van de repository. De command line interface geeft verdere instructies</br>

<p>python main.py

<h3>Auteurs (Authors)</h3>
Nils van Doorn</br>
Jesse Pannekeet</br>
Thomas Verouden

<h3>Dankwoord (Acknowledgments)</h3>

Een dankwoord aan Reitze L.H. Jansen en Wouter L.J. Vrielink voor hun technische en theoretische ondersteuning iedere week, en Daan v.d. Berg voor het organiseren van het vak Heuristieken op de Universiteit van Amsterdam.
