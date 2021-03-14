import turtle # Importuję bibliotekę.

turtle.bgcolor("black") # Ustawiam tło.
turtle.pensize(2) # Ustawiam wielkość żółwia.
turtle.speed(0) # Ustawiam prędkośc żółwia.

# Tworzę pętlę rysującą koła do momentu, aż wróci do tego samego miejsca i powstanie spirograf.
for i in range(6):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]: # Ustawiam kolory.
        turtle.color(colours) # Ustawiam zmianę kolorów.
        turtle.circle(200) # Ustawiam wielkość kół.
        turtle.left(10) # Odstęp pomiędzy rysowaniem kół w lewo.

turtle.done()  # Ustawiam żółwia, aby nie zamykał się po zakończeniu rysowania.


