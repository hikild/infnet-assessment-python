import socket, os
# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtém o nome da máquina
host = socket.gethostname()
porta = 9090
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
while True:
# Aceita alguma conexão
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
# Recebe pedido do cliente:
    msg = socket_cliente.recv(2048)
    nome_arq = msg.decode('ascii')
    if os.path.isfile(nome_arq):
# Envia primeiro o tamanho
        tamanho = os.stat(nome_arq).st_size
        socket_cliente.send(str(tamanho).encode('ascii'))
# Abre o arquivo no modo leitura de bytes
        arq = open(nome_arq, 'rb')
# Envia os dados
        bytes = arq.read(4096)
        while bytes:
            socket_cliente.send(bytes)
            bytes = arq.read(4096)
# Fecha o arquivo
        arq.close()
    else:
        print("Não encontrou o arquivo")
# tamanho é -1 para indicar que não achou arquivo
        socket_cliente.send('-1'.encode('ascii'))
# Fecha o socket cliente
    socket_cliente.close()