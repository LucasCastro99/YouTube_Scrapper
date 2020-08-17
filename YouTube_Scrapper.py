import pafy #Biblioteca usada para captura de dados da plataforma YouTube.
import csv
import progressbar #Biblioteca usada para personalizar e indicar o carregamento do script.

#Função que faz a criação e escrita de um arquivo CSV para armazenar os dados.
def csv_manipulation(arquivo,titulo,duracao,curtidas,descurtidas,vizualizacoes):
    with open("{}_OUTPUT.csv".format(arquivo), "a", newline="\n") as video_stats:
        escrita = csv.writer(video_stats)
        escrita.writerow([titulo,duracao,curtidas,descurtidas,vizualizacoes])

#Função usada para captura dos dados da URL de um determinado video.
def capture_video(filename, url):
    video = pafy.new(url)
    title = video.title
    duration = video.duration
    likes = video.likes
    dislikes = video.dislikes
    views = video.viewcount
    csv_manipulation(filename, title,duration,likes,dislikes,views)

#Função 
def file_reader(nome_arquivo):
    with open("{}.txt".format(nome_arquivo), "r") as arquivo_texto:
        arquivo = csv.reader(arquivo_texto)
        lista_url = []
        for linha in arquivo:
            lista_url.append(linha[0])
    return lista_url

#Começo do processamento do programa, com a inserção do nome do arquivo baixado.
#Link do site usado para baixar a lista de videos de uma Playlist ou Canal no YouTube:
#https://guihkx.github.io/ulist/
arquivo = input("Insert Name Of Text File (.txt): ")

lista_videos = file_reader(arquivo)

#Trecho que cria o cabeçalho do CSV.
with open("{}_OUTPUT.csv".format(arquivo), "w", newline="\n",) as video_stats:
    escrita = csv.writer(video_stats)
    escrita.writerow(["Título","Duração","Curtidas","Descurtidas","Vizualizações"])

#Iniciação da biblioteca de personalização do carregamento.
bar = progressbar.ProgressBar(max_value=len(lista_videos))
bar_position = 1

#Processamento e atualização do carregamento.
for endereco in lista_videos:
    capture_video(arquivo, endereco)
    bar.update(bar_position)
    bar_position += 1