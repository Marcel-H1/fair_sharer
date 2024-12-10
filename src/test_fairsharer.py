from fair_sharer import fair_sharer  # Importiere deine Funktion

def test_fair_sharer():
    # Testfall 1: Einfacher Fall
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]

    # Testfall 2: Mehrere Iterationen
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]

    # Testfall 3: Keine Iterationen
    assert fair_sharer([0, 1000, 800, 0], 0) == [0, 1000, 800, 0]

    # Testfall 4: Edge Case mit nur einem Element
    assert fair_sharer([1000], 1) == [1000]
