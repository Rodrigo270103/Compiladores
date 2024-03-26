definir factorial_iterativo(n){
resultado = 1
para i en rango(1, n+1){
resultado *= i
}
numero = 5
factorial = factorial_iterativo(numero)
imprimir ("El factorial es:")
imprimir(factorial)