def fatorial_recursivo(n):
    """
    Calcula n! usando recursão
    Baseia-se na definição: n! = n × (n-1)!
    """
    # Validação de entrada
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    
    # Caso base: quando chegamos em 0 ou 1
    if n == 0 or n == 1:
        return 1
    
    # Passo recursivo: n! = n × (n-1)!
    return n * fatorial_recursivo(n - 1)

# Exemplo de uso
print("5! =", fatorial_recursivo(5))  # Saída: 5! = 120