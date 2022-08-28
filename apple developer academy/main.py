#Importando as Bibliotecas usadas
import PySimpleGUI as sg
from random import choice


#Criando a funçaõ principal do programa
def main():
    #y é o número de alunos e serve como contador no looping
    y = 20

    #Vetor com todos os alunos
    vetor = ['Laura', 'Pedro', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Beatriz','Eduardo', 'Caio']
    
    #Vetor com a saída de dados
    saida = []

    #Vetores com as possíveis duplas de cada aluno
    vetorPedro = [ 'Carlos', 'Maria', 'Leonardo', 'Ana','Marcos', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Beatriz','Eduardo']
    vetorJoao = [ 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorLaura =['Carlos', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorVinicius = ['Carlos', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Eduardo', 'Caio']
    vetorMaria = ['Pedro', 'João', 'Vinicius', 'Daniela', 'Marcos', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorLeonardo = [ 'Pedro', 'João', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorAna = ['Laura', 'Pedro', 'João', 'Vinicius', 'Daniela', 'Marcos','Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorDaniela = ['Laura', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana',  'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Beatriz','Eduardo']
    vetorMarcos = ['Laura', 'Pedro', 'João', 'Carlos', 'Maria', 'Leonardo', 'Ana',  'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Eduardo', 'Caio']
    vetorWesley = ['Laura', 'Pedro', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorLuiza = ['Laura', 'Pedro', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Felipe', 'Helena', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorDaiane = ['Laura', 'Pedro', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorFelipe = ['Laura', 'Pedro', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Luiza','Beatriz','Eduardo', 'Caio']
    vetorTeodoro = ['Laura', 'Pedro', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorHelena = ['Laura', 'Pedro', 'Vinicius', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Luiza', 'Natalia','Beatriz','Eduardo', 'Caio']
    vetorNatalia = ['Laura', 'Pedro', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Luiza', 'Daiane', 'Teodoro', 'Helena']
    vetorBeatriz = ['Laura', 'Pedro', 'João', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena']
    vetorEduardo = ['Laura', 'Pedro', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Daniela', 'Marcos', 'Wesley', 'Luiza', 'Daiane', 'Teodoro', 'Helena']
    vetorCaio = ['Laura', 'João', 'Vinicius', 'Carlos', 'Maria', 'Leonardo', 'Ana', 'Marcos', 'Wesley', 'Luiza', 'Daiane', 'Felipe', 'Teodoro', 'Helena']

    #Função que remove o aluno sorteado para ser dupla do cabeça de chave de todos os vetores de possibilidade
    def removerSorteado():
        #laura
        if resultado2 in vetorLaura:
            vetorLaura.remove(resultado2)
        #pedro
        if resultado2 in vetorPedro:
            vetorPedro.remove(resultado2)
        #vinicius
        if resultado2 in vetorVinicius:
            vetorVinicius.remove(resultado2)
        #maria
        if resultado2 in vetorMaria:
            vetorMaria.remove(resultado2)
        #leonardo
        if resultado2 in vetorLeonardo:
            vetorLeonardo.remove(resultado2)
        #Ana
        if resultado2 in vetorAna:
            vetorAna.remove(resultado2)
        #daiane
        if resultado2 in vetorDaiane:
            vetorDaiane.remove(resultado2)
        #marcos
        if resultado2 in vetorMarcos:
            vetorMarcos.remove(resultado2)
        #wesley
        if resultado2 in vetorWesley:
            vetorWesley.remove(resultado2)
        #luiza
        if resultado2 in vetorLuiza:
            vetorLuiza.remove(resultado2)
        #daniela
        if resultado2 in vetorDaniela:
            vetorDaniela.remove(resultado2)
        #felipe
        if resultado2 in vetorFelipe:
            vetorFelipe.remove(resultado2)
        #Teodoro
        if resultado2 in vetorTeodoro:
            vetorTeodoro.remove(resultado2)
        #Helena
        if resultado2 in vetorHelena:
            vetorHelena.remove(resultado2)
        #Natalia
        if resultado2 in vetorNatalia:
            vetorNatalia.remove(resultado2)
        #Beatriz
        if resultado2 in vetorBeatriz:
            vetorBeatriz.remove(resultado2)
        #Eduardo
        if resultado2 in vetorEduardo:
            vetorEduardo.remove(resultado2)
        #Caio
        if resultado2 in vetorCaio:
            vetorCaio.remove(resultado2)
    

    #looping que sorteia os alunos até que as duplas estejam completas
    while y != 0:
        i=0
        resultado = choice(vetor)

        #Cada if faz parte de uma série de condições que analiza qual aluno foi sorteado como cabeça de chave
        if resultado == "Laura":
            resultado2 =  choice(vetorLaura)
            vetor.remove(resultado)
            
            #Looping que sorteia a dupla de Laura
            while resultado2 not in vetor:
                resultado2 = choice(vetorLaura)
            vetor.remove(resultado2)
            removerSorteado()
    
            resultado3 = "Laura e "+ resultado2
            saida.append(resultado3)
            y=y-2
            
        #As condições se repetem para todos, serve como um switch case.

        if resultado == "Pedro":
            resultado2 =  choice(vetorPedro)
        
            vetor.remove(resultado)
            while resultado2 not in vetor:
                resultado2 = choice(vetorPedro)
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Pedro e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "João":
            resultado2 =  choice(vetorJoao)
        
            vetor.remove(resultado)

            while resultado2 not in vetor:
                resultado2 = choice(vetorJoao)
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'João e ' + resultado2
            y=y-2
            saida.append(resultado3)

        if resultado == "Vinicius":
            resultado2 = choice(vetorVinicius)
            vetor.remove(resultado)
            while resultado2 not in vetor:
                resultado2 = choice(vetorVinicius)
        
            vetor.remove(resultado2)
            removerSorteado()



            resultado3 = 'Vinícius e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Maria":
            resultado2 = choice(vetorMaria)
            vetor.remove(resultado)
            while resultado2 not in vetor:
                resultado2 = choice(vetorMaria)
            vetor.remove(resultado2)
            removerSorteado()
        
            resultado3 = 'Maria e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == 'Leonardo':
            resultado2 = choice(vetorLeonardo)
            vetor.remove(resultado)
            while resultado2 not in vetor:    
                resultado2 = choice(vetorLeonardo)
            vetor.remove(resultado2)
            removerSorteado()


            resultado3 = 'Leonardo e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Ana":
            resultado2 = choice(vetorAna)
            vetor.remove(resultado)
            
            while resultado2 not in vetor:    
                resultado2 = choice(vetorAna)
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Ana e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Daniela":
            resultado2 = choice(vetorDaniela)
            vetor.remove(resultado)
        
            while resultado2 not in vetor:
                resultado2 = choice(vetorDaniela)
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Daniela e ' + resultado2
            y=y-2
            saida.append(resultado3)      
            ####Não funciona o metodo de criar um vetor pra cada if
            ####Se for sortear há a chance de sortear alguem que já foi sorteado e deletado no resultado 2
    
    
        if resultado == "Marcos":
            resultado2 = choice(vetorMarcos)
            vetor.remove(resultado)
        
            while resultado2 not in vetor:
                resultado2 = choice(vetorMarcos)
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Marcos e ' + resultado2
            y=y-2
            saida.append(resultado3)

        if resultado == "Wesley":
            resultado2 = choice(vetorWesley)
            vetor.remove(resultado)
            while resultado2 not in vetor:
                resultado2 = choice(vetorWesley)
            
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Wesley e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Luiza":
            resultado2 = choice(vetorLuiza)
            vetor.remove(resultado)
        
            while resultado2 not in vetor:
                resultado2 = choice(vetorLuiza)
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Luiza e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Daiane":
            resultado2 = choice(vetorDaiane)
            vetor.remove(resultado)
            while resultado2 not in vetor:
                resultado2 = choice(vetorDaiane)
            
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Daiane e ' + resultado2
            y=y-2
            saida.append(resultado3)

    
        if resultado == "Felipe":
            resultado2 = choice(vetorFelipe)
            vetor.remove(resultado)
            while resultado2 not in vetor:
                resultado2 = choice(vetorFelipe)
            
            vetor.remove(resultado2)
            removerSorteado()
        
            resultado3 = 'Felipe e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Helena":
            resultado2 = choice(vetorHelena)
            vetor.remove(resultado)
        
            while resultado2 not in vetor:
                resultado2 = choice(vetorHelena)
            vetor.remove(resultado2)
            removerSorteado()


            resultado3 = 'Helena e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Natalia":
            resultado2 = choice(vetorNatalia)
            vetor.remove(resultado)
        
            while resultado2 not in vetor:
                resultado2 = choice(vetorNatalia)
            
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Natalia e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Beatriz":
            resultado2 = choice(vetorBeatriz)
            vetor.remove(resultado)
        
            while resultado2 not in vetor:
                resultado2 = choice(vetorBeatriz)
            
            vetor.remove(resultado2)
            removerSorteado()


            resultado3 = 'Beatriz e ' + resultado2
            y=y-2
            saida.append(resultado3)

    
        if resultado == "Eduardo":
            resultado2 = choice(vetorEduardo)
            vetor.remove(resultado)
            while resultado2 not in vetor:
                resultado2 = choice(vetorEduardo)
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Eduardo e ' + resultado2
            y=y-2
            saida.append(resultado3)


        if resultado == "Caio":
            resultado2 = choice(vetorCaio)
            vetor.remove(resultado)
            while resultado2 not in vetor:
                resultado2 = choice(vetorCaio)
        
            vetor.remove(resultado2)
            removerSorteado()

            resultado3 = 'Caio e ' + resultado2
            y=y-2
            saida.append(resultado3)
    
    #Declara as variáveis para serem utilizadas na interface
    global saida1,saida2,saida3,saida4,saida5, saida6,saida7,saida8,saida9,saida10

    saida1=saida[0]
    saida2=saida[1]
    saida3=saida[2]
    saida4=saida[3]
    saida5=saida[4]
    saida6=saida[5]
    saida7=saida[6]
    saida8=saida[7]
    saida9=saida[8]
    saida10=saida[9]
