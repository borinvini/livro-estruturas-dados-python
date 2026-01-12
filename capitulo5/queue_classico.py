# =============================================================================
# ESTRUTURA DE DADOS: FILA (QUEUE) - IMPLEMENTAÇÃO COM CLASSE
# =============================================================================
# Implementação didática de fila circular sem uso de métodos prontos do Python
# Métodos renomeados para evitar conflito com métodos nativos do Python
# =============================================================================


class Fila:
    """
    Classe que implementa uma Fila Circular com array de tamanho fixo.
    
    Atributos:
        capacidade (int): Tamanho máximo da fila
        dados (list): Array que armazena os elementos
        inicio (int): Índice do primeiro elemento (frente da fila)
        fim (int): Índice do último elemento (final da fila)
        quantidade (int): Contador de elementos na fila
    """
    
    def __init__(self, capacidade=5):
        self.capacidade = capacidade          # Tamanho do array
        self.dados = [None] * capacidade      # Array com posições vazias
        self.inicio = 0                       # Índice do início da fila
        self.fim = -1                         # Índice do fim (-1 indica fila vazia)
        self.quantidade = 0                   # Contador de elementos
    
    
    def esta_vazia(self):
        """
        Verifica se a fila está vazia.
        
        Returns:
            bool: True se vazia, False caso contrário
        """
        return self.quantidade == 0
    
    
    def esta_cheia(self):
        """
        Verifica se a fila está cheia.
        
        Returns:
            bool: True se cheia, False caso contrário
        """
        return self.quantidade == self.capacidade
    
    
    def enfileirar(self, elemento):
        """
        Insere um elemento no final da fila (operação ENQUEUE).
        Utiliza aritmética modular para comportamento circular.
        
        Args:
            elemento: Valor a ser inserido
            
        Returns:
            bool: True se inserido com sucesso, False se fila cheia
        """
        if self.esta_cheia():
            return False
        
        # Incrementa circularmente
        self.fim = (self.fim + 1) % self.capacidade  
        self.dados[self.fim] = elemento              # Insere na posição
        self.quantidade = self.quantidade + 1        # Incrementa contador
        return True
    
    
    def desenfileirar(self):
        """
        Remove e retorna o elemento do início da fila (operação DEQUEUE).
        Utiliza aritmética modular para comportamento circular.
        
        Returns:
            O elemento removido, ou None se a fila estiver vazia
        """
        if self.esta_vazia():
            return None
        
        elemento = self.dados[self.inicio]       # Guarda o elemento
        self.dados[self.inicio] = None           # Limpa a posição
        # Incrementa circularmente
        self.inicio = (self.inicio + 1) % self.capacidade  
        self.quantidade = self.quantidade - 1    # Decrementa contador
        return elemento
    
    
    def consultar_inicio(self):
        """
        Retorna o elemento do início sem removê-lo (operação PEEK/FRONT).
        
        Returns:
            O elemento do início, ou None se a fila estiver vazia
        """
        if self.esta_vazia():
            return None
        return self.dados[self.inicio]
    
    
    def tamanho(self):
        """
        Retorna a quantidade de elementos na fila.
        
        Returns:
            int: Número de elementos armazenados
        """
        return self.quantidade
    
    
    def exibir(self):
        """
        Exibe o conteúdo da fila do início até o fim.
        """
        print('\n--- CONTEÚDO DA FILA ---')
        
        if self.esta_vazia():
            print('  (fila vazia)')
            return
        
        print('Início → Fim (ordem de atendimento)')
        print('-' * 40)
        
        # Percorre do início até o fim usando aritmética modular
        posicao_atual = self.inicio
        contador = 0
        
        while contador < self.quantidade:
            print(f'  {contador + 1}º da fila: [{posicao_atual}] → {self.dados[posicao_atual]}')
            posicao_atual = (posicao_atual + 1) % self.capacidade
            contador = contador + 1
        
        print('-' * 40)
        print(f'Total de elementos: {self.quantidade}/{self.capacidade}')
        print(f'Próximo a ser atendido: {self.dados[self.inicio]}')


# =============================================================================
# PROGRAMA PRINCIPAL - MENU INTERATIVO
# =============================================================================

def main():
    """Função principal com menu interativo para testar a fila."""
    
    fila = Fila(capacidade=5)  # Cria fila com 5 posições
    
    print("=" * 50)
    print("ESTRUTURA DE DADOS: FILA (QUEUE)")
    print("Implementação com Classe - Fila Circular")
    print("=" * 50)
    
    while True:
        print('\n--- MENU DE OPERAÇÕES ---')
        print('1 - Inserir na fila (ENQUEUE)')
        print('2 - Remover da fila (DEQUEUE)')
        print('3 - Consultar início (PEEK)')
        print('4 - Listar a fila')
        print('5 - Sair')
        print('-' * 25)
        
        op = int(input("Escolha uma opção: "))
        
        if op == 1:  # Operação ENQUEUE
            dado = int(input('Qual número deseja inserir? '))
            
            if fila.enfileirar(dado):
                print(f'Número {dado} inserido com sucesso!')
                print(f'Posição no fim: {fila.fim}')
                print(f'Elementos na fila: {fila.quantidade}')
            else:
                print('Fila cheia! Impossível inserir.')
                print(f'Capacidade máxima: {fila.capacidade} elementos')
        
        elif op == 2:  # Operação DEQUEUE
            dado_removido = fila.desenfileirar()
            
            if dado_removido is not None:
                print(f'Número {dado_removido} removido com sucesso!')
                print(f'Foi atendido(a) e saiu da fila')
                print(f'Elementos restantes: {fila.quantidade}')
            else:
                print('Fila vazia! Impossível remover.')
        
        elif op == 3:  # Operação PEEK
            elemento_inicio = fila.consultar_inicio()
            
            if elemento_inicio is not None:
                print(f'→ Próximo a ser atendido: {elemento_inicio}')
            else:
                print('→ Fila vazia!')
        
        elif op == 4:  # Listar fila
            fila.exibir()
        
        elif op == 5:  # Sair
            print('\n' + '=' * 50)
            print('Encerrando o programa...')
            print('=' * 50)
            break
        
        else:
            print('Opção inválida! Selecione uma opção de 1 a 5.')


# Executa o programa
if __name__ == "__main__":
    main()