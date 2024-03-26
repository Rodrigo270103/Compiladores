definir factorial_recursivo(n){
     si n ==0{
     retorna 1
     }
       sino {
       retorna n * factorial_recursivo(n-1)
       }
}
numero = 5
factorial = factorial_recursivo(n)
imprimir ("el factorial es:" )
imprimir (factorial)