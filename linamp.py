# Importando a biblioteca gráfica
import tkinter as tk
 
# Importando um seletor de arquivos
from tkinter import filedialog
 
# Biblioteca pygame para tocar audio
import pygame
 
# Biblioteca para manipular nomes de arquivos
import os
 
# Inicializa o módulo de som do pygame
pygame.mixer.init()
 
playlist = []       # Lista que vai guardar os caminhos das músicas
indice_atual = 0    # Índice da música atual (posição na lista)
pausado = False     # Controle de pause (True = pausado)
 
# Função: Carregar os arquivos MP3
def carregar_arquivos():
    arquivos = filedialog.askopenfilename(
        title = "Selecione músicas",
        filetypes = [("Arquivos MP3", "*.mp3")]
 
    )
 
    for arquivo  in arquivos:
 
        # Adiciona o caminho completo  na playlist
 
        playlist.append(arquivo)
 
        # Mostra apenas o nome do arquivo na lista visual
 
        lista_musicas.insert(tk.END, *elements:os.path.basename(arquivo))
 
 
# Função Tocar Música
 
def tocar_musica():
    # Toca a música atual na playlist
    global pausado
 
    # Se não houver músicas, não faz nada
    if not playlist:
        return
   
    # Carregar a música atual no player
    pygame.mixer.music.load(playlist[indice_atual])
 
    # Inicia a reprodução
    pygame.mixer.music.play()
 
    # Define que nao esta pausado 
    pausdo = False
   
    # Atualizar o nome das músicas na tela
    atualizar_label()

 # Função: pausar e continuar

 def pausar_musica():

    global pausado 

    # Se estiver pausado, volta a tocar 

    if pausado:
        pygame.mixer.music.unpause()
        pausado = False

    else:
        # Caso contário, pausa
        pygame.mixer.music.pause()
        pausado = True
 
 
 
 
 
 
 