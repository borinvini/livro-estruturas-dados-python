# Implementação de Fila (Queue) usando métodos prontos do Python

TAM_MAX = 5  # Inicialização da fila
fila = []  # Lista dinâmica vazia

print("=" * 50)
print("ESTRUTURA DE DADOS: FILA (QUEUE)")
print("=" * 50)

while True:
    print('\n--- MENU DE OPERAÇÕES ---')
    print('1 - Inserir na fila (ENQUEUE)')
    print('2 - Remover da fila (DEQUEUE)')
    print('3 - Listar a fila')
    print('4 - Sair')
    print('-' * 25)
    
    op = int(input("Escolha uma opção: "))
    
    if op == 1:
        # Operação ENQUEUE usando append()
        dado = int(input('Qual número deseja inserir? '))
        
        if len(fila) < TAM_MAX:
            fila.append(dado)  # Método pronto: adiciona no final da fila
            print(f'✓ Número {dado} inseriu na fila com sucesso!')
            print(f'  Posição na fila: {len(fila)}º')
            print(f'  Pessoas na fila: {len(fila)}')
        else:
            print('✗ Fila cheia! Impossível inserir.')
            print(f'  Capacidade máxima: {TAM_MAX} elementos')
    
    elif op == 2:
        # Operação DEQUEUE usando pop(0)
        if len(fila) > 0:
            dado_removido = fila.pop(0)  # Método pronto: remove do início
            print(f'✓ Número {dado_removido} removido com sucesso!')
            print(f'  Foi atendido(a) e saiu da fila')
            print(f'  Pessoas restantes: {len(fila)}')
        else:
            print('✗ Fila vazia! Impossível remover.')
    
    elif op == 3:
        # Listar elementos da fila usando enumerate()
        print('\n--- CONTEÚDO DA FILA ---')
        
        if len(fila) > 0:
            print('Início → Fim (ordem de atendimento)')
            print('-' * 40)
            
            # enumerate() retorna índice e valor automaticamente
            for i, item in enumerate(fila):
                print(f'  Posição {i + 1}º: [{i}] → {item}')
            
            print('-' * 40)
            print(f'Total de elementos: {len(fila)}/{TAM_MAX}')
            print(f'Próximo a ser atendido: {fila[0]}')
        else:
            print('  (fila vazia)')
    
    elif op == 4:
        print('\n' + '=' * 50)
        print('Encerrando o programa...')
        print('=' * 50)
        break
    
    else:
        print('✗ Opção inválida! Selecione uma opção de 1 a 4.')