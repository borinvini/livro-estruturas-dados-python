# =============================================================================
# ESTRUTURA DE DADOS: PILHA (STACK) - IMPLEMENTAÇÃO COM CLASSE
# =============================================================================
# Implementação didática USANDO métodos prontos do Python
# Demonstra encapsulamento dos métodos nativos em uma classe
# =============================================================================


class Pilha:
    """
    Classe que implementa uma Pilha usando métodos prontos do Python.
    
    Atributos:
        capacidade (int): Tamanho máximo da pilha
        dados (list): Lista dinâmica que armazena os elementos
    """
    
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.dados = []  # Lista dinâmica vazia
    
    
    def esta_vazia(self):
        """
        Verifica se a pilha está vazia.
        
        Returns:
            bool: True se vazia, False caso contrário
        """
        return len(self.dados) == 0
    
    
    def esta_cheia(self):
        """
        Verifica se a pilha está cheia.
        
        Returns:
            bool: True se cheia, False caso contrário
        """
        return len(self.dados) == self.capacidade
    
    
    def empilhar(self, elemento):
        """
        Insere um elemento no topo da pilha (operação PUSH).
        Utiliza o método append() do Python.
        
        Args:
            elemento: Valor a ser inserido
            
        Returns:
            bool: True se inserido com sucesso, False se pilha cheia
        """
        if self.esta_cheia():
            return False
        
        self.dados.append(elemento)  # Método pronto: adiciona no final
        return True
    
    
    def desempilhar(self):
        """
        Remove e retorna o elemento do topo da pilha (operação POP).
        Utiliza o método pop() do Python.
        
        Returns:
            O elemento removido, ou None se a pilha estiver vazia
        """
        if self.esta_vazia():
            return None
        
        return self.dados.pop()  # Método pronto: remove do final
    
    
    def consultar_topo(self):
        """
        Retorna o elemento do topo sem removê-lo (operação PEEK/TOP).
        
        Returns:
            O elemento do topo, ou None se a pilha estiver vazia
        """
        if self.esta_vazia():
            return None
        return self.dados[-1]  # Acesso ao último elemento
    
    
    def tamanho(self):
        """
        Retorna a quantidade de elementos na pilha.
        
        Returns:
            int: Número de elementos armazenados
        """
        return len(self.dados)
    
    
    def exibir(self):
        """
        Exibe o conteúdo da pilha do topo até a base.
        Utiliza a função reversed() do Python.
        """
        print('\n--- CONTEÚDO DA PILHA ---')
        
        if self.esta_vazia():
            print('  (pilha vazia)')
            return
        
        print('Topo → Base')
        print('-' * 15)
        
        # reversed() retorna iterador reverso sem modificar a lista
        for i, item in enumerate(reversed(self.dados)):
            indice_real = len(self.dados) - 1 - i
            print(f'  [{indice_real}] → {item}')
        
        print('-' * 15)
        print(f'Total de elementos: {self.tamanho()}/{self.capacidade}')


# =============================================================================
# PROGRAMA PRINCIPAL - MENU INTERATIVO
# =============================================================================

def main():
    """Função principal com menu interativo para testar a pilha."""
    
    pilha = Pilha(capacidade=5)  # Cria pilha com 5 posições
    
    print("=" * 50)
    print("ESTRUTURA DE DADOS: PILHA (STACK)")
    print("Implementação com Classe (métodos prontos)")
    print("=" * 50)
    
    while True:
        print('\n--- MENU DE OPERAÇÕES ---')
        print('1 - Inserir na pilha (PUSH)')
        print('2 - Remover da pilha (POP)')
        print('3 - Consultar topo (PEEK)')
        print('4 - Listar a pilha')
        print('5 - Sair')
        print('-' * 25)
        
        op = int(input("Escolha uma opção: "))
        
        if op == 1:  # Operação PUSH
            dado = int(input('Qual número deseja inserir? '))
            
            if pilha.empilhar(dado):
                print(f'Número {dado} inserido com sucesso!')
                print(f'Posição no topo: {pilha.tamanho() - 1}')
            else:
                print('Pilha cheia! Impossível inserir.')
                print(f'Capacidade máxima: {pilha.capacidade} elementos')
        
        elif op == 2:  # Operação POP
            dado_removido = pilha.desempilhar()
            
            if dado_removido is not None:
                print(f'Número {dado_removido} removido com sucesso!')
                novo_topo = pilha.tamanho() - 1 if not pilha.esta_vazia() else "vazio"
                print(f'Novo topo: {novo_topo}')
            else:
                print('Pilha vazia! Impossível remover.')
        
        elif op == 3:  # Operação PEEK
            elemento_topo = pilha.consultar_topo()
            
            if elemento_topo is not None:
                print(f'→ Elemento no topo: {elemento_topo}')
            else:
                print('→ Pilha vazia!')
        
        elif op == 4:  # Listar pilha
            pilha.exibir()
        
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