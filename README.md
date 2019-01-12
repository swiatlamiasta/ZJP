# Zaawansowane Języki Programowania - PyCharmers

### Informacje podstawowe:

| Wykonawcy | Prowadzący | Język<br>programowania | Narzędzie<br>analizy kodu | Źródło kodu | Data oddania |
:-:|:-:|:-:|:-:|:-:|:-:
| Adamczyk Tomasz<br>Bilikiewicz Semen<br>Gołębiewski Artur | dr Bzyl Włodzimierz | [Python](https://www.python.org/) | [PyLint](https://www.pylint.org/) | [Gilded Rose<br>Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) | 12.01.2019

---

### Wprowadzenie:

__Python__ - język programowania wysokiego poziomu ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek standardowych, którego ideą przewodnią jest czytelność i klarowność kodu źródłowego. Jego składnia cechuje się przejrzystością i zwięzłością.

__PyLint__ - narzędzie do analizy statycznej kodu Pythona, które szuka błędów programistycznych, pomaga w egzekwowaniu standardu kodowania, wykrywa "zapachy kodu" i oferuje proste propozycje refaktoryzacji.

__Halstead Effort (złożoność Halsteada)__ - takie metryki jak: liczba unikatowych operatorów, liczba unikatowych operandów, całkowita liczba wystąpień operatorów oraz całkowita liczba wystąpień operandów, które dotyczą rozmiaru programu, pozwalają na zdefiniowanie bardziej skomplikowanych metryk złożoności. Wyróżnia się wśród nich m. in. trudność, poziom programu, wysiłek, czas, szacunkową liczbę błędów. Im mniejsza wartość, tym lepiej.

---

### Wykres wartości Halstead Effort:

Na poniższym wykresie znajdują się wartości metryki wysiłku dla złożoności Halsteada. Z każdym kolejnym krokiem refaktoryzacji jest widoczny progres (im mniejsza wartość, tym lepiej):

<p align="center">
  <img src="wykres1.png"/>
</p>

---

### Proces refaktoryzacji kodu:

Krok __#1__:

W tym kroku postanowiliśmy przenieść całe ciało pierwszej pętli metody *update_quality(self)* do osobnej metody *update_one_item(self, item)*. Dzięki temu wynik naszej złożoności zmalał z 4205 do 3423.

````diff
  def update_quality(self):
    for item in self.items:
-     if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
-       if item.quality > 0:
-         if item.name != "Sulfuras, Hand of Ragnaros":
-           item.quality = item.quality - 1
+     self.update_one_item(item)
+
+  def update_one_item(self, item):
+    if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
+      if item.quality > 0:
+        if item.name != "Sulfuras, Hand of Ragnaros":
+          item.quality = item.quality - 1
+    else:
+      if item.quality < 50:
+        item.quality = item.quality + 1
+        if item.name == "Backstage passes to a TAFKAL80ETC concert":
+          if item.sell_in < 11:
+            if item.quality < 50:
+              item.quality = item.quality + 1
+          if item.sell_in < 6:
+            if item.quality < 50:
+              item.quality = item.quality + 1
+      if item.name != "Sulfuras, Hand of Ragnaros":
+        item.sell_in = item.sell_in - 1
+      if item.sell_in < 0:
+        if item.name != "Aged Brie":
+          if item.name != "Backstage passes to a TAFKAL80ETC concert":
+            if item.quality > 0:
+              if item.name != "Sulfuras, Hand of Ragnaros":
+                item.quality = item.quality - 1
+              else:
+                item.quality = item.quality - item.quality
          else:
            if item.quality < 50:
              item.quality = item.quality + 1
-               if item.name == "Backstage passes to a TAFKAL80ETC concert":
-                 if item.sell_in < 11:
-                   if item.quality < 50:
-                     item.quality = item.quality + 1
-                   if item.sell_in < 6:
-                     if item.quality < 50:
-                       item.quality = item.quality + 1
-          if item.name != "Sulfuras, Hand of Ragnaros":
-            item.sell_in = item.sell_in - 1
-          if item.sell_in < 0:
-            if item.name != "Aged Brie":
-              if item.name != "Backstage passes to a TAFKAL80ETC concert":
-                if item.quality > 0:
-                  if item.name != "Sulfuras, Hand of Ragnaros":
-                    item.quality = item.quality - 1
-                  else:
-                    item.quality = item.quality - item.quality
-              else:
-                if item.quality < 50:
-                  item.quality = item.quality + 1
````

Krok __#2__:

W tym kroku postanowiliśmy wyodrębnić do osobnej metody zawartość pierwszego *if'a* z metody *update_one_item(self, item)*. Można powiedzieć, że dzięki tej zmianie zmierzamy powoli w stronę pojedynczej odpowiedzialności metody. Dzięki temu zabiegowi uzyskaliśmy ponownie mniejszy wynik, wynoszący tym razem 3142.

````diff
  def update_one_item(self, item):
+   self.update_part1(item)
+   if item.name != "Sulfuras, Hand of Ragnaros":
+     item.sell_in = item.sell_in - 1
+   if item.sell_in < 0:
+     if item.name != "Aged Brie":
+       if item.name != "Backstage passes to a TAFKAL80ETC concert":
+         if item.quality > 0:
+           if item.name != "Sulfuras, Hand of Ragnaros":
+             item.quality = item.quality - 1
+            else:
+              item.quality = item.quality - item.quality
+          else:
+            if item.quality < 50:
+              item.quality = item.quality + 1
+
+   def update_part1(self, item):
    if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
      if item.quality > 0:
        if item.name != "Sulfuras, Hand of Ragnaros":
          if item.sell_in < 6:
            if item.quality < 50:
              item.quality = item.quality + 1
-       if item.name != "Sulfuras, Hand of Ragnaros":
-         item.sell_in = item.sell_in - 1
-       if item.sell_in < 0:
-         if item.name != "Aged Brie":
-           if item.name != "Backstage passes to a TAFKAL80ETC concert":
-             if item.quality > 0:
-               if item.name != "Sulfuras, Hand of Ragnaros":
-                 item.quality = item.quality - 1
-               else:
-                 item.quality = item.quality - item.quality
-             else:
-               if item.quality < 50:
-                 item.quality = item.quality + 1
````

Krok __#3__:

W kolejnym kroku postanowiliśmy wydzielić drugiego głównego *if'a* z metody aktualizującej wartość przedmiotów oraz trzeciego z głównych *if'ów* również przenieść do dwóch nowych metod. Dzięki temu nasza metoda *update_one_item(self, item)* stała się znacznie czytelniejsza.

````diff
  def update_one_item(self, item):
    self.update_part1(item)
+   self.update_part2(item)
+   if self.has_expired(item):
+     self.update_expired(item)
+
+   def has_expired(self, item):
+     return item.sell_in < 0
+
+   def update_expired(self, item):
+     if item.name != "Aged Brie":
+       if item.name != "Backstage passes to a TAFKAL80ETC concert":
+         if item.quality > 0:
+           if item.name != "Sulfuras, Hand of Ragnaros":
+             item.quality = item.quality - 1
+       else:
+         item.quality = item.quality - item.quality
+      else:
+        if item.quality < 50:
+          item.quality = item.quality + 1
+
+   def update_part2(self, item):
      if item.name != "Sulfuras, Hand of Ragnaros":
        item.sell_in = item.sell_in - 1
-       if item.sell_in < 0:
-         if item.name != "Aged Brie":
-           if item.name != "Backstage passes to a TAFKAL80ETC concert":
-             if item.quality > 0:
-               if item.name != "Sulfuras, Hand of Ragnaros":
-                 item.quality = item.quality - 1
-           else:
-             item.quality = item.quality - item.quality
-         else:
-           if item.quality < 50:
-             item.quality = item.quality + 1
````

Przyklad refaktoryzacji jeden z metod krok po kroku:

![](https://github.com/swiatlamiasta/ZJP/blob/master/pics/p5/1.png)
![](https://github.com/swiatlamiasta/ZJP/blob/master/pics/p5/2.png)
![](https://github.com/swiatlamiasta/ZJP/blob/master/pics/p5/3.png)
![](https://github.com/swiatlamiasta/ZJP/blob/master/pics/p5/4.png)
![](https://github.com/swiatlamiasta/ZJP/blob/master/pics/p5/5.png)
![](https://github.com/swiatlamiasta/ZJP/blob/master/pics/p5/6.png)
![](https://github.com/swiatlamiasta/ZJP/blob/master/pics/p5/7.png)


---

#### I efekt końcowy:

Poniżej znajduje się kod wynikowy stanowiący rezultat dokonanych poprawek oraz refaktoryzacji. Uzyskaliśmy kod czytelny i przejrzysty, posiadający cechy "dobrego, czystego kodu". Z jednej klasy wyodrębniliśmy ich kilka, z jednej metody powstało wiele metod, umieszczonych w odrębnych klasach... __Raj perfekcjonisty :)__

Wynik końcowy przyjętej przez nas metryki wynosi 1031. A zatem jest to dość dobry wynik, biorąc pod uwagę to, że na początku otrzymaliśmy w rezultacie wartość 4205. Brawo my!

````diff
+ class GildedRose(object):
+ 
+   def __init__(self, items):
+     self.items = items
+ 
+   def update_quality(self):
+     for item in self.items:
+       self.update_one_item(item)
+ 
+   def update_one_item(self, item):
+     if item.name == "Aged Brie":
+       item.__class__ = Brie
+     elif item.name == "Sulfuras, Hand of Ragnaros":
+       item.__class__ = Sulfuras
+     elif item.name == "Backstage passes to a TAFKAL80ETC concert":
+      item.__class__ = BackstagePass
+     elif item.name == "Conjured Mana Cake":
+       item.__class__ = Conjured
+     item.update(item)
+ 
+ 
+ class Item:
+ 
+   def __init__(self, name, sell_in, quality):
+     self.name = name
+     self.sell_in = sell_in
+     self.quality = quality
+ 
+   def __repr__(self):
+     return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
+ 
+   def has_expired(self, item):
+     return item.sell_in < 0
+ 
+   def decrement_quality(self, item):
+     if item.quality > 0:
+       item.quality = item.quality - 1
+ 
+   def increment_quality(self, item):
+     if item.quality < 50:
+       item.quality = item.quality + 1
+ 
+   def update(self, item):
+     self.decrement_quality(item)
+     item.sell_in = item.sell_in - 1
+     if self.has_expired(item):
+       self.decrement_quality(item)
+ 
+ 
+ class Brie(Item):
+ 
+   def update(self, item):
+     self.increment_quality(item)
+     item.sell_in = item.sell_in - 1
+     if self.has_expired(item):
+       self.increment_quality(item)
+       item.sell_in = item.sell_in - 1
+ 
+ 
+ class BackstagePass(Item):
+ 
+   def update(self, item):
+     self.increment_quality(item)
+     item.sell_in = item.sell_in - 1
+     if item.sell_in < 11:
+       self.increment_quality(item)
+     if item.sell_in < 6:
+       self.increment_quality(item)
+     if self.has_expired(item):
+       item.quality = 0
+ 
+ class Sulfuras(Item):
+ 
+   def update(self, item):
+     pass
+ 
+ 
+ class Conjured(Item):
+   def decrement_quality(self, item):
+     if item.quality > 0:
+       item.quality = item.quality - 2
````
