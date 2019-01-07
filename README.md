# ZJP

(halstead effort na poczatku = 4205, w kazdym kolejnym kroku podawany w nawiasach)

Wskaznik effort bierze pod uwage inne wskazniki halsteada wiec chyba jest najlepszy do naszych celów.
Pokazanie code smells za pomoca Pylinta

Kolejne kroki refaktoryzacji: 
- extract method update_one_item (4205) (wnetrze petli for jako metoda)
- extract method update_part1 (3423) (pierwszy nadrzedny if)
- extract method update_part2 (3142) (drugi nadrzedny if)
- extract method update_expired (3060) (wewnetrzna czesc trzeciego if'a)


- w update_part1 robimy invert if condition (3060) nic to nie zmienia ofc, ale
pozwala nam na kolejny krok
- extract method brie_or_ticket_update (2840)