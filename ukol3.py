"""
V předchozím úkole se Ti možná nelíbilo,
že se výsledek vždycky napsal až na další řádku.
To se dá opravit takhle:
"""

x = 6
y = 5
rozdil = x - y

print(f"x - y = {rozdil}")

"""
Teď jsme udělali trochu chytřejší print.
Tím, že je tam f mu říkáme, že to co následuje chcem zformátovat.
A co to znamená? do složených závorek {} můžu napsat nějakou proměnnou
a ono ji to normálně napíše.

Dej si jenom pozor na to, že za f musí být uvozovky, a na konci taky.
Takže: print(f"něco")

Možná se Ti taky nelíbí, že když se to vypíše, tak tam je napsáno 
prostě "x - y" a ne jejich skutečné hodnoty "8 - 5".
Teď už ale víš, jak to změnit! Zkusíš to?

Rada - jak napsat složené závorky:
- na české klávesnici:
    Vpravo od mezerníku je AltGr, ten drž a u toho kliknu na B a pak N.
- na anglické klávesnici:
    Drž shift a klikni tam, kde je 'ú' (kousek od enteru).
"""

print(f"{x} - y = rozdil")

"""
Až si to vyzkoušíš, mám pro Tebe další super novinku!
Do složených závorek se dá napsat víc, než jenom proměnná.
Můžeš do nich napsat celou funkci/matematickou operaci:
"""

print(f"x krát y je {x * y}")

"""
Zkus si na dalších řádkách pomocí printu napsat
jak dopadnou všechny čtyři operace mezi číslem 1 a 2
bez toho, aby sis je někam ukládal.
To, co se pak napíše by mělo vypadat asi takhle:
77 + 17 = 94
77 - 17 = 60
...
"""
cislo1 = 77
cislo2 = 17

print(f"{cislo1} + {cislo2} = {cislo1 + cislo2}")