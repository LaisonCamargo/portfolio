import customtkinter as ctk
import yt_dlp
import os
import threading

# Configuração visual inicial
ctk.set_appearance_mode("System")  # Segue o tema do Windows (Claro/Escuro)
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YouTube MP3 Downloader")
        self.geometry("500x320")

        # Elementos da Interface
        self.label = ctk.CTkLabel(self, text="YouTube to MP3", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Cole o link do YouTube aqui...", width=400)
        self.entry.pack(pady=10)

        self.btn_baixar = ctk.CTkButton(self, text="Baixar Áudio", command=self.iniciar_thread)
        self.btn_baixar.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Status: Cole o Link do vídeo", text_color="gray")
        self.status_label.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

    def iniciar_thread(self):
        # Desativa o botão para evitar cliques duplos e inicia o download em segundo plano
        url = self.entry.get()
        if not url:
            self.status_label.configure(text="Erro: Por favor, insira um link!", text_color="red")
            return
            
        self.btn_baixar.configure(state="disabled")
        self.status_label.configure(text="Baixando...", text_color="black")
        self.progress_bar.start() # Barra de progresso animada
        
        thread = threading.Thread(target=self.executar_download, args=(url,))
        thread.start()

    def executar_download(self, url):
        pasta_download = os.path.join(os.path.expanduser("~"), "Downloads")
        # Use o caminho do seu FFmpeg aqui
        caminho_ffmpeg = r'C:\Users\Lin\AppData\Local\Microsoft\WinGet\Links'

        ydl_opts = {
            'format': 'bestaudio/best',
            'ffmpeg_location': caminho_ffmpeg,
            'outtmpl': f'{pasta_download}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # Atualiza a interface após o sucesso (usando after para ser thread-safe)
            self.after(0, lambda: self.finalizar_sucesso())
        except Exception as e:
            self.after(0, lambda: self.finalizar_erro(str(e)))

    def finalizar_sucesso(self):
        self.btn_baixar.configure(state="normal")
        self.progress_bar.stop()
        self.progress_bar.set(1)
        self.status_label.configure(text="Download concluído com sucesso! Verifique a sua pasta 'Downloads'", text_color="green")
        self.entry.delete(0, 'end')

    def finalizar_erro(self, erro):
        self.btn_baixar.configure(state="normal")
        self.progress_bar.stop()
        self.progress_bar.set(0)
        self.status_label.configure(text=f"Erro: {erro[:30]}...", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()