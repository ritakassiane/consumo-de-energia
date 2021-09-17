###############################################################################################################################################################
# Autor: Rita Kassiane Santos dos Santos                                                                                                                                        #
# Componente Curricular: Algoritmos I                                                                                                                         #
# Concluido em: 16/04/2019                                                                                                                                    #
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de outro colega ou de outro autor,                   #
# tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código de outra autoria que                  #
# não a minha está destacado com uma citação para o autor e a fonte do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.#
###############################################################################################################################################################

logo = """
################################################  S I M U L A D O R  D E  C O N S U M O  D E  E N E R G I A ######################################################## 
                                                            Universidade Estadual de Feira de Santana
                                                                 RITA KASSIANE SANTOS DOS SANTOS 
 

"""










n = 1
consumoDosAparelhos = 0
consumoDoSetor = 0


# A variável "t" ler e salva o valor da Tarifa Residencial de Baixa tensão #
print (logo)
t = float(input('Digite a Tarifa Residencial de Baixa Tensão:'))

# Enquanto n receber 1, um contador, denominado "continuargeral", iniciará de 0 até o número definido pelo usuário na variável "aparelho" #





while n == 1:

# As variáveis potGeral, qntdGeral, horasDia, diasMes, leem e salvam, respectivamente, a potência do aparelho, a quantidade de aparelhos com essa mesma potência, 
# a quantidade de horas de uso por dia e a quantidade de dias de uso por mês#

# A variável "potDiferentes" certifica se existem aparelhos de mesmo tipo com potências diferentes, em caso afirmativo, enquanto existir, as variáveis "pa", "qa" , "hpd","dpm"
# irão ler a potência, quantidade de aparelhos desse tipo, horas de uso por dia, dias de uso por mês e somar com as variáveis cuja a função é a mesma mas foram estabelecidas anteriormente (essas são potGeral e qntdGeral)
    print ('Iniciando setor...')
    aparelhosDoSetor = int (input("""Digite a quantidade dos tipos de aparelhos diferentes existentes neste setor:
                                         Ex: Se existe 1 geladeira e 1 TV => você deve digitar: 2 [dois tipos de aparelhos diferentes]
                                         Ex': Se existe 100 Lampadas, 2 computadores e 1 TV => você deve digitar: 3 [3 tipos de aparelhos diferentes]
"""))
    for continuargeral in range(0,aparelhosDoSetor):
    

        potGeral = int(input('Digite a potencia do aparelho(em Watts):'))
        qntdGeral = int(input('Quantos aparelhos existem com essa mesma potência nesse setor?'))
        horasDia = int(input('Quantidade de horas de uso por dia:')) 
        diasMes = int(input('Quantidade de dias de uso no mês:'))
        potDiferentes = int(input("""
                                                 -------------------------------------------------------
                                                |     1    | Adicionar potência diferente para aparelho |            
                                                |     0    | Finalizar cálculo do aparelho              |
                                                 -------------------------------------------------------
 

                    Digite aqui o número da ação que deseja realizar:"""))
    
# O consumo do aparelho será atribuido à variável "consumoDosAparelhos" a qual irá ser atribuída ao consumoDoSetor, para que, posteriormente à essa atribuição #
#  seja possível zerar o consumoDosAparelhos e reutilizar todas as variáveis anteriormente utilizadas #
        if potDiferentes == 1:
            potTemp = 0
            qntdTemp = 0
            hpdTemp = 0
            dpmTemp = 0
            while True:
                pa = int(input('Existe alguma potência diferente deste aparelho? Se sim, digite-a, se não, digite 0 em todos:'))
                qa = int(input('Quantidade de aparelhos desse tipo:'))
                hpd = int(input('Digite a quantidade de horas de uso por dia:'))
                dpm = int(input('Digite a quantidade de dias de uso por mês:'))

                if pa == 0:
                    break
                potTemp += pa
                qntdTemp += qa
                hpdTemp += hpd
                dpmTemp += dpm
                
                consumoDosAparelhos += ((potTemp * hpdTemp * dpmTemp)* qntdTemp) + ((potGeral*horasDia*diasMes)*qntdGeral) # FAZENDO A SOMA DO CONSUMO DE DOIS APARELHOS DE MESMO TIPO CUJO SUAS POTÊNCIAS SEJAM DIFERENTES #
                
        else:
            consumoDosAparelhos += ((potGeral * horasDia * diasMes) * qntdGeral) # CALCULAND0 O CONSUMO DE UM APARELHO QUALQUER E ATRIBUINDO ESSE VALOR A UMA VARIÁVEL #
            

        # A VARIÁVEL "CONSUMO DOS APARELHOS" GUARDA A SOMA DO CONSUMO DE TODOS OS APARELHOS DIGITADOS # 

    ValorReal1 = (consumoDosAparelhos/1000)*t # CALCULANDO O CONSUMO EM DINHEIRO, SEM LEVAR EM CONTA OS IMPOSTOS #
    print('O consumo do setor, em dinheiro, equivale a {} reais'.format(ValorReal1))
    
    consumoDoSetor += consumoDosAparelhos # ATRIBUINDO A SOMA DO CONSUMO DE TODOS OS APARELHOS A UMA NOVA VARIÁVEL
    consumoDosAparelhos = 0 
    
    
    
    n = int(input("""


                                                ------------------
                                                |     1    | SIM |            
                                                |     0    | NÃO |
                                                ------------------


Deseja adicionar outro setor?"""))
ValorReal2 = (consumoDoSetor/1000)*t
ValorFinal = (((36.25*ValorReal2)/100)+ValorReal2) # CALCULANDO O CONSUMO EM DINHEIRO, LEVANDO EM CONTA OS IMPOSTOS #
print('O valor final, em dinheiro, da sua conta de luz é {}'.format(ValorFinal))



# APÓS A EXECUÇÃO DO CÓDIGO SER FINALIZADA, SERÁ NECESSÁRIO QUE O USUÁRIO APERTE QUALQUER BOTÃO PARA QUE SE FECHE A ABA DO PROGRAMA # 
import os
os.system("pause")







