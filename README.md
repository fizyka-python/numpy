# Ćwiczenia NumPy

1. Napisz funkcję `zastap_zera(A, x)`, która modyfikuje tablicę `A` (o dowolnym kształcie) poprzez zastąpienie wszystkich elementów równych zero liczbą `x`.

2. Napisz funkcję `wysrodkuj(A)`, która zwraca tablicę utworzoną z tablicy `A` (o dowolnym kształcie) w taki sposób, że od każdego jej elementu odejmuje średnią arytmetyczną wszystkich elementów `A`. Sama tablica A powinna pozostać niezmieniona.

3. Napisz funkcję `sumy_ponizej(A)`, która dla tablicy kwadratowej `A` (dowolnego rozmiaru większego niż 1) stworzy tablicę jednowymiarową, której *k*-ty element to suma elementów *k*-tej kolumny tablicy `A` leżących poniżej głównej przekątnej.

4. Napisz funkcję `na_przemian(n)`, która utworzy i zwróci kwadratową tablicę NumPy z naprzemiennymi jedynkami i zerami, o rozmiarze podanym przez jako argument `n`, w postaci:

   ```python
   >>> na_przemian(2)
   array([[ 1.,  0.],
          [ 0.,  1.]])

   >>> na_przemian(3)
   array([[ 1.,  0.,  1.],
          [ 0.,  1.,  0.],
          [ 1.,  0.,  1.]])

   >>> na_przemian(4)
   array([[ 1.,  0.,  1.,  0.],
          [ 0.,  1.,  0.,  1.],
          [ 1.,  0.,  1.,  0.],
          [ 0.,  1.,  0.,  1.]])

   >>> na_przemian(5)
   array([[ 1.,  0.,  1.,  0.,  1.],
          [ 0.,  1.,  0.,  1.,  0.],
          [ 1.,  0.,  1.,  0.,  1.],
          [ 0.,  1.,  0.,  1.,  0.],
          [ 1.,  0.,  1.,  0.,  1.]])
   ```
