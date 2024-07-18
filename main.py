def q1():
    '''Escrever um programa para ler o ano em que a criança toma a 1a dose
    e a periodicidade (intervalo em anos) da vacina e 
    exibir em que outros anos a criança deve tomar as próximas doses desta vacina, 
    sabendo que são 4(quatro) doses ao total.'''

    ano_dose1 = int(input(''))









    pass

def q2():
    '''Faça um programa que leia uma sequencia de números e 
    indique se eles são primos ou não. Você deve parar ao ler o número -1'''

    numero = int(input(''))




    pass

def q3():
    '''Escreva um programa que receba como entrada o valor doado por cada cliente, 
    até que seja informado um valor negativo, e exiba o total arrecadado e o valor médio doado por eles'''

    dinheiro_doado = int(input(''))



    pass

def q4():
    '''Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada 
    por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais'''


    qnt_dias = int(input(''))
    quilo_total = int(input(''))
    if quilo_total <= 100:
        print('90.00')
    elif qnt_dias == 0:
        print('Valor inválido')



    pass

def q5():
    '''Faça um programa para converter um valor de temperatura em uma escala de 
    mediada definida pelo usuário para as outras escalas de medida.'''

    #Multiplicamos a temperatura em ºC por 1,8 e somamos 32 ao resultado(celcius - f)

    pass

if __name__=="__main__":
    # teste sua questão manualmente aqui
    q4()