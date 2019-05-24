<h1>Algoritmes</h1>
<h4>Greedy:</h4>
Bij greedy wordt aan ieder aminozuur een richting verwezen om het aminozuur te vouwen. Iedere keer als er een richting wordt toegevoegd wordt er berekend welke vouwing(en) het hoogste aantal punten geven. Deze routes worden onthouden om er een volgende richting aan toe te voegen voor het volgende aminozuur. De rest van de vouwingen worden gepruned.

<h4>Multiple step breadth first:</h4>
Het multiple step breadth first algoritme genereert een random oplossing voor het gekozen eiwit en genereert alle vouwingsopties van een opgegeven lengte (default 2D = 8, default 3D = 6). Het algoritme probeert al deze opties een opgegeven aantal keer (default = 3) op elke positie in het eiwit toe te passen en onthoudt verbeteringen.

<h4>Greedy with look ahead:</h4>
Greedy with look ahead genereert alle vouwingopties van een opgegeven lengte (default 2D = 8, default 3D = 6) en bouwt aan de hand van deze opties het eiwit op.
Daarna loopt het algoritme nog een opgegeven aantal keer (default = 2) over het eiwit volgens het multiple step breadth first algoritme.

<h4>Beam Search:</h4>
Beam Search voegt net als bij greedy iedere keer een richting toe aan de vouwing. Er zijn een boven- en een ondergrens toegevoegd om de uitkomsten van breath first in een ronde in 3 groepen te verdelen. De bovengrens is de hoogste score die behaald is tijdens het toevoegen van het vorige aminozuur. De ondergrens is het gemiddelde van alle vouwingen van het vorige aminozuur. Als de score van een vouwingen in de nieuwe groep boven de bovengrens zit, wordt deze zeker meegenomen voor de volgende iteraties. Boven de ondergrens, maar onder de bovengrens krijgt een hoge kans (default = 75%) om door te gaan, de scores onder de ondergrens krijgen een lage kans (default = 20%) om door te gaan.

<h4>Beam search with look ahead:</h4>
Bij beam search with look ahead wordt er eerst voor een opgegeven aantal stappen (default 2D = 6, default 3D = 4) alle vouwingen gemaakt. Daarna wordt er dezelfde methode gebruikt voor prunen m.b.v. de ondergrens als bij beam search. Voor de bovengrens wordt alleen de beste vouwing(en) onthouden aan de hand van hun scores.
