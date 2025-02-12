import os
from tkinter.filedialog import askdirectory  # pop-up

caminho = askdirectory(title="Escolha uma pasta")
print(caminho)

tipos_arquivos = os.listdir(caminho)
print(tipos_arquivos)

local = {
    "imagens": [".png", ".jpg", ".jfif", ".gif", ".ico", ".jpeg", ".webp"],
    "winrar": [".rar", ".zip", ".msi"],
    "executavel": [".exe"],
    "pdf": [".pdf"],
    "video": [".mp4", ".mkv", ".avi", ".ogv"],
    "java": [".jar"],
    "texto": [".txt", ".docx", ".xlsx", ".xls", ".csv"],
    "áudio": [".mp3", ".acc", ".m4a"],
}

for arquivo in tipos_arquivos:
    nome, extensao = os.path.splitext(arquivo)  # Aqui não precisamos do caminho
    for pastinha in local:
        if extensao in local[pastinha]:  # Corrigido para pastinha
            # Verifica se a pasta não existe, se não, cria
            if not os.path.exists(f"{caminho}/{pastinha}"):
                os.mkdir(f"{caminho}/{pastinha}")  # Removido o ":" aqui
            # Renomeia (move) o arquivo para a pasta correta
            os.rename(
                f"{caminho}/{arquivo}", f"{caminho}/{pastinha}/{arquivo}"
            )  # Corrigido o caminho
