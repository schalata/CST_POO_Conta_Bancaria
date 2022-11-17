from conta import Conta
from cliente import Cliente
# import time

if __name__ == '__main__':
    pedro = Cliente('Pedro', 'Souza', '999.999.999-99')
    maria = Cliente('Maria', 'Silva', '888.888.888-88')

    conta_pedro = Conta('123-4', pedro, 120.0, 1000.0)
    conta_maria = Conta('567-8', maria, 200.0, 2000.0)

    conta_pedro.extrato()

    conta_pedro.transfere_para(conta_maria, 500.0)
    conta_pedro.saca(200.0)

    # print('Aguardando...')
    # time.sleep(120)
    conta_pedro.extrato()

    # print('Aguardando...')
    # time.sleep(120)
    conta_maria.extrato()