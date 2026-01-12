def fibonacci_recursivo(n):
    """
    Calcula o n-ésimo termo da sequência de Fibonacci usando recursão
    Baseia-se na definição: F(n) = F(n-1) + F(n-2)
    """
    # Validação de entrada
    if n <= 0:
        raise ValueError("Fibonacci não definido para números negativos")
    
    # Caso base: quando chegamos nos 2 primeiros termos da série
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Passo recursivo: F(n) = F(n-1) + F(n-2)
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Exemplo de uso
print("F(5) =", fibonacci_recursivo(5))