# ZJP

(halstead effort na poczatku = 4205, w kazdym kolejnym kroku podawany w nawiasach)

Wskaznik effort bierze pod uwage inne wskazniki halsteada wiec chyba jest najlepszy do naszych celów.
Pokazanie code smells za pomoca Pylinta

Kolejne kroki refaktoryzacji: 
- extract method update_one_item (4205) (wnetrze petli for jako metoda)
- extract method update_part1 (3423) (pierwszy nadrzedny if)
- extract method update_part2 (3142) (drugi nadrzedny if)
- extract method update_expired (3060) (wewnetrzna czesc trzeciego if'a)
---

- w update_part1 robimy invert if condition (3060) nic to nie zmienia ofc, ale
pozwala nam na kolejny krok
- extract method brie_or_ticket_update (2840)
---

- extract method increment_quality (1760) - kawalek kodu powtarzajacy sie w 4 miejscach
- wstawiamy metode brie_or_ticket_update z powrotem do metody update_part1 (do pierwszego ifa), zauwazamy ze mozna usunac czesc kodu (1458)
- jak wyzej tylko ze do drugiego ifa, pozbywamy sie metody brie_or_ticket i zbednego kodu (1388)

update_part1 zaczyna wygladac dobrze, kolejne ify zalezne od nazw

---

- w update_expired robimy inverted ify i scalamy zagniezdzone ify w jeden wiekszy praktycznie tak jak poprzednio (1246)
- extract method decrement_quality (wystepowala w 2 miejscach) (1075)
- laczymy z powrotem uproszczone metody w jednego switch-like ifa (1031)
