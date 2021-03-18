from concurrent.futures.process import ProcessPoolExecutor
from itertools import zip_longest
import psutil
import os
import subprocess
import random
import time
import csv
import multiprocessing
import threading

def run(func):
    if __name__ == '__main__':
        print('\U0001f918\U0001f3fb' * 3, func.__name__, '\U0001f918\U0001f3fb' * 3)
        func()


# Questão 01:
def listaProcessos():
    for proc in psutil.process_iter():
        proc_info = proc.as_dict(attrs=['pid', 'name', 'memory_percent'])
        cpu = psutil.cpu_percent(interval=0.1)
        proc_info.update({'Uso da CPU': cpu})
        print(F'Processo: {proc_info["pid"]} - PID: {proc_info["name"]} (Uso da CPU {cpu} - "Uso de memória": {proc_info["memory_percent"]:.0%})')

# Questão 02:
def execArquivo():
    arq = input("Nome do arquivo: ")
    if os.path.exists(arq):
        subprocess.Popen(["notepad", arq])
    else:
        return print('{} não encontrado.'.format(arq))

# Questão 03:
def armazenamentoArq():
    arqs = ['arq_exemplo.txt', 'arq_at.txt', 'arq_infnet.txt']
    bytes = []
    dados = list()
    novo_arq = open('resultado.txt', 'a')
    for arq in arqs:
        print(f'Nome: {os.path.basename(arq)} - Tamanho: {os.stat(arq).st_size}')
        print(f'Diretório usuário: {os.path.join(os.getcwd(), arq)}')
        bytes.append(os.stat(arq).st_size)
        dados.append(f'Nome: {os.path.basename(arq)} - Tamanho: {os.stat(arq).st_size} \n')
        dados.append(f'Diretório usuário: {os.path.join(os.getcwd(), arq)} \n')
    dados.append(f'Numero de bytes decrescente: {sorted(bytes, reverse=True)} \n')
    novo_arq.writelines(dados)

# Questão 04:
def lerArquivo():
    try:
        arq = open(('arq_infnet.txt'))
        dados = list()
        for texto in arq.readlines():
            dados.append(texto)
        for reverse in reversed(dados):
            print(reverse[::-1])
    except Exception as error:
        print(error)

# Questão 05:
def somarElementos():
    arq1 = open('a.txt', 'r')
    arq2 = open('b.txt', 'r')

    a = arq1.read().split(" ")
    b = arq2.read().split(" ")
    arq1.close()
    arq2.close()
    soma_total = 0
    for n1, n2 in zip_longest(a, b, fillvalue=0):
        soma = int(n1) + int(n2)
        soma_total += int(n1) + int(n2)
        print(f' {n1} + {n2} = {soma} \n')
    print(f'soma de todos os elementos: {soma_total}')

#Questão 08:
valores = []
def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * 1
    return print(fat)

@run
def sequencial():
    vetor_valor = int(input("Entre com o tamanho do vetor: "))
    tempo_inicial = float(time.time())
    lista = []
    for i in range(vetor_valor):
        lista.append(random.randint(-50, 51))
    soma = 0
    for i in lista:
        soma = soma + i
    tempo_final = float(time.time())
    print(f"Tempo total: {tempo_final - tempo_inicial:0.2f}s")

@run
def threading():
    def somaThread(lista, soma_parcial, id):
        soma = 0
        for i in lista:
            soma = soma + i
        soma_parcial[id] = soma

    vetor_valor = int(input("Entre com o tamanho do vetor: "))

    tempo_inicial = float(time.time())
    lista = []
    for i in range(vetor_valor):
        lista.append(random.randint(-50, 51))

    num_threads = 4

    soma_parcial = num_threads * [0]
    lista_threads = []

    for i in range(num_threads):
        init = i * int(vetor_valor/num_threads)
        final = (i + 1) * int(vetor_valor/num_threads)
        thread = threading.Thread(target=somaThread, args=(lista_threads[init:final], soma_parcial, i))
        thread.start()
        lista_threads.append(thread)

    for t in lista_threads:
        t.join()

    soma = 0
    for i in soma_parcial:
        soma = soma + i

    tempo_final = float(time.time())

    print(f"Tempo total: {tempo_final - tempo_inicial:0.2f}s")


def somarProcesso(q1, q2):
    lista = q1.get()
    soma = 0
    for i in lista:
        soma = soma + i
    q2.put(soma)

@run
def multiprocessos():
    if __name__ == "__main__":
        pass

    vetor_valor = int(input("Entre com o tamanho do vetor: "))
    tempo_inicial = float(time.time())
    lista = []
    for i in range(vetor_valor):
        lista.append(random.randint(-50, 51))

    num_proc = 4

    q_entrada = multiprocessing.Queue()
    q_saida = multiprocessing.Queue()

    lista_proc = []
    for i in range(num_proc):
        init = i * int(vetor_valor/num_proc)
        final = (i + 1) * int(vetor_valor/num_proc)
        q_entrada.put(lista[init:final])
        process = multiprocessing.Process(target=somarProcesso, args=(q_entrada, q_saida))
        process.start()
        lista_proc.append(process)

    for p in lista_proc:
        p.join()

    soma = 0
    for i in range(0, num_proc):
        soma = soma + q_saida.get()

    tempo_final = float(time.time())

    print(f"Tempo total: {tempo_final - tempo_inicial:0.2f}s")

