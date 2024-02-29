def speelveldInlezen():
    
    """
    Speelveld inlezen uit invoer en teruggeven als een matrix van karakters,
    waarbij '*' een positie aangeeft waar een mijn ligt en '.' een positie waar
    geen mijn ligt.
    """
    
    # aantal rijen en kolommen inlezen
    rijen, _ = [int(x) for x in input().split()]
    
    # speelveld inlezen en omzetten naar matrix van karakters
    speelveld = []
    for _ in range(rijen):
        regel = input()
        speelveld.append(list(regel))
        
    # speelveld teruggeven
    return speelveld

def aantalMijnen(rij, kolom, speelveld):
    
    """
    Aan deze functie moet een speelveld doorgegeven worden als een matrix (lijst
    van lijsten) waarin posities waar een mijn ligt worden voorgesteld door '*'
    en posities waar geen mijn ligt worden voorgesteld door '.'. De functie 
    geeft een waarde terug die aangeeft voor een cel op een gegeven rij en 
    kolom, op hoeveel naburige cellen er een mijn ligt.
    """

    # aantal rijen en kolommen bepalen
    rijen, kolommen = len(speelveld), len(speelveld[0])
    
    # richtingen bepalen van alle buurpunten van de huidge cel in het rooster
    buren = (
        (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)
    )
    
    # ga na hoeveel buurpunten van de gegeven cel een mijn bevatten
    aantal = 0
    for dr, dk in buren:
        # belangrijk: controleren of de naburige positie niet buiten het 
        #             speelveld valt
        if 0 <= rij + dr < rijen and 0 <= kolom + dk < kolommen:
            if speelveld[rij + dr][kolom + dk] == '*':
                aantal += 1
                
    # geef terug hoeveel buurpunten van de gegeven cel een mijn bevatten
    return aantal
  
def speelveldAanvullen(speelveld):
    
    """
    Aan deze functie moet een speelveld doorgegeven worden als een matrix (lijst
    van lijsten) waarin posities waar een mijn ligt worden voorgesteld door '*'
    en posities waar geen mijn ligt worden voorgesteld door '.'. De functie 
    vervangt de posities waar geen mijn ligt door een string met een cijfer
    dat aangeeft op hoeveel naburige posities (inclusief diagonale buren) er een
    mijn ligt.
    """

    # overloop alle cellen van boven naar onder en van links naar rechts, en vul 
    # in alle cellen die geen mijn bevatten in hoeveel buurpunten van die cel
    # wel een mijjn bevatten
    rijen, kolommen = len(speelveld), len(speelveld[0])
    for rij in range(rijen):
        for kolom in range(kolommen):
            # cellen waar geen mijn ligt worden aangegeven door een punt
            if speelveld[rij][kolom] == '.':
                # getal moet voorgesteld worden als een string om achteraf
                # makkelijk het rooster als een string te kunnen uitschrijven
                speelveld[rij][kolom] = str(aantalMijnen(rij, kolom, speelveld))

def speelveldUitschrijven(speelveld):
    
    """
    Aan deze functie moet een speelveld doorgegeven worden als een matrix (lijst
    van lijsten) waarin posities waar een mijn ligt worden voorgesteld door '*'
    en posities waar geen mijn ligt worden voorgesteld door '.'. De functie 
    schrijft het speelveld uit naar standaard uitvoer.
    """

    # speelveld uitschrijven
    print('\n'.join(''.join(rij) for rij in speelveld))

# gegeven speelvelden uit invoer overlopen
velden = int(input())
for veld in range(velden):

    # speelveld inlezen
    speelveld = speelveldInlezen()
    
    # speelveld aanvullen met aantal mijnen
    speelveldAanvullen(speelveld)
    
    # speelveld uitschrijven
    if veld:
        # lege regel uitschrijven tussen speelvelden
        print()
    speelveldUitschrijven(speelveld)
