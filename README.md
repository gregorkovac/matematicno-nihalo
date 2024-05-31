# Matematično nihalo

## 3. domača naloga pri predmetu Numerična matematika

Gregor Kovač

## Opis naloge

Simulirati želimo nedušeno nihanje matematičnega nihala, ki je podano z diferencialno enačbo

$\frac{g}{l}\sin{\theta(t)} + \theta''(t) = 0$

z začetnima pogojema $\theta(0)=\theta_0$ in $\theta'(0)=\theta'_0$, kjer je $g=9.80665 \frac{m}{s^2}$ gravitacijski pospešek in $l$ dolžina nihala. To enačbo rešujemo z metodo Runge Kutta reda 4, ampako jo za to moramo najprej prevesti na sistem diferencialnih enačb prvega reda.

## Struktura projekta

- [nihalo.py](./nihalo.py) - Python skripta z rešitvijo naloge
- [test_nihalo.py](./test_nihalo.py) - Python skripta s testi
- [demo.ipynb](./demo.ipynb) - Jupyter Notebook dokument za dinamično generiranje poročila
- [report.pdf](./report.pdf) - poročilo projekta

## Potrebne Python knjižnice

- Numpy
- MatPlotLib

## Uporaba testov

Če želimo pognati teste za projekt, v ukazno vrstico napišemo `python test_nihalo.py`. Lahko uporabimo tudi vgrajeno funkcijo za testiranje v našem razvojnem okolju.

## Generiranje poročila

Za (ponovno) generiranje odpremo datoteko `demo.ipynb`. To lahko storimo v svojem razvojnem okolju, ali pa v ukazni vrstici napišemo `jupyter notebook`. Nato v seznamu poiščemo pravo datoteko, jo odpremo, po želji spremenimo in poženemo vse celice, nato pa v orodni vrstici izberemo `File > Save and Export Notebook As > PDF`.
