# Latihan menampilkan deret fibonacci dengan fungsi rekursif

def fibonacci(n):
   if n == 0 or n == 1:
      return n
   else:
      return (fibonacci(n-1) + fibonacci(n-2))

input_nilai = 6

for i in range(input_nilai):
   print(fibonacci(i), end=' ')