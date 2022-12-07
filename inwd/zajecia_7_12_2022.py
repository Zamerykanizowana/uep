# 1. Funkcja, która przymuje tabelę studentów i oblicza srednią ocen tych studentów. Oczekiwany output:
# Średnia ocen studentów wynosi: 4.4375

def srednia_ocen_studentów(tabela_studentow):
  # TODO

# 2. Funkcja, która przyjmuje tabelę i numer rocznika i oblicza srednią ocen tych studentów. Oczekiwany output:
# Średnia ocen studentów roku 1 wynosi: 4.525
# Średnia ocen studentów roku 2 wynosi: 4.475
# Średnia ocen studentów roku 3 wynosi: 4.375
# Średnia ocen studentów roku 4 wynosi: 3.875
# Średnia ocen studentów roku 5 wynosi: nan

def srednia_ocen_studentow_danego_rocznika(tabela_studentow, rok):
  # TODO

# 3. Funkcja, która przyjmuje tabelę, numer rocznika, status dot. Erasmusa i oblicza srednią ocen tych studentów, którzy 
# są lub nie są na Ersmusie. Erasmus powinien być typu prawda / fałsz (boolean).
# Oczekiwany output:
# Średnia ocen studentów roku 3 na Erasmusie wynosi: 4.375
# Średnia ocen studentów roku 2 na uczelni macierzystej wynosi: 4.46875

def srednia_ocen_studentow_danego_rocznika_status_erasmus(tabela_studentow, rok, erasmus):
  if erasmus:
    # TODO
  else:
    # TODO


# 4. Funkcja wyszukująca studenta o najwyższej średniej. Oczekiwany output:
# Student o najwyższej średniej: Jan Ignasiak, uzyskana średnia: 5.0
# Czy ta funkcja jest poprawna?

def student_najwyzsza_srednia(tabela_studentow):
  # TODO

# 5. Funkcja wyszukująca studenta o najwyższej średniej na danym roku. Oczekiwany output:
# Student o najwyższej średniej na roku 2: Małgorzata Piotrowska, uzyskana średnia: 4.5
# Czy ta funkcja jest poprawna?
def student_najwyzsza_srednia_na_roku(tabela_studentow, rok):
  # TODO

# 6. Funkcja wyszukująca studenta o najwyższej średniej na danym roku i danym statusie. Oczekiwany output:
# Student o najwyższej średniej na roku 3 na Ersmusie: Karolina Przypadkowa, uzyskana średnia: 4.375
# Student o podanych parametrach nie istnieje


def student_najwyzsza_srednia_na_roku_status_erasmus(tabela_studentow, rok, erasmus):
  try:
    if erasmus:
      # TODO
    else:
      # TODO
  except:
    # TODO

