def fatorial_iterativo(n):
    """
    Calcula n! usando um laço iterativo
    Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120
    """
    # Validação de entrada
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    
    # Inicializa o resultado
    resultado = 1
    
    # Multiplica todos os números de 1 até n
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

# Exemplo de uso
print("5! =", fatorial_iterativo(5))  # Saída: 5! = 120