# Sistema de Gerenciamento de Fila de Atendimento
fila = []

def exibir_menu():
    print("\n" + "=" * 30)
    print("  SISTEMA DE FILA DE ATENDIMENTO")
    print("=" * 30)
    print("1. Adicionar cliente à fila")
    print("2. Chamar próximo cliente")
    print("3. Visualizar fila atual")
    print("4. Sair")
    print("=" * 30)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            nome = input("Digite o nome do cliente: ").strip()
            if nome:
                fila.append(nome)  # Adiciona ao final da lista
                print(f"\n[SUCESSO] '{nome}' entrou na posição {len(fila)} da fila.")
            else:
                print("\n[ERRO] Nome não pode ser vazio!")

        elif opcao == "2":
            if len(fila) > 0:
                atendido = fila.pop(0)  # Remove o primeiro elemento da lista
                print(f"\n[ATENDIMENTO] Próximo cliente: {atendido}")
            else:
                print("\n[AVISO] A fila está vazia no momento.")

        elif opcao == "3":
            if not fila:
                print("\n[INFO] A fila está completamente vazia.")
            else:
                print("\n--- Fila de Espera Atual ---")
                for i, cliente in enumerate(fila, start=1):
                    print(f"{i}º lugar: {cliente}")

        elif opcao == "4":
            print("\nEncerrando o programa... Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()