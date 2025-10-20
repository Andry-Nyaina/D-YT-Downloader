import customtkinter as ctk
from tkinter import messagebox, filedialog
import threading
import os
import yt_dlp

# Configuration de l'apparence
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("D YT Downloader")
        self.root.geometry("700x650")
        self.root.resizable(True, True)

        # Variables
        self.url_var = ctk.StringVar()
        self.format_var = ctk.StringVar(value="mp4")
        self.quality_var = ctk.StringVar(value="720")
        self.download_path_var = ctk.StringVar(value=os.path.expanduser("~/Downloads"))

        self.downloading = False

        self.setup_ui()

    def setup_ui(self):
        # Main frame avec scroll
        main_frame = ctk.CTkScrollableFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Titre
        title_label = ctk.CTkLabel(main_frame, text="D YT Downloader",
                                   font=ctk.CTkFont(size=24, weight="bold"))
        title_label.pack(pady=(0, 20))

        # Section URL
        url_section = ctk.CTkFrame(main_frame)
        url_section.pack(fill="x", pady=10)

        ctk.CTkLabel(url_section, text="URL de la vidéo:",
                     font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=(10, 5), padx=10)

        url_entry = ctk.CTkEntry(url_section, textvariable=self.url_var, height=40,
                                 placeholder_text="Collez l'URL YouTube ici...")
        url_entry.pack(fill="x", padx=10, pady=(0, 10))

        # Section Options
        options_section = ctk.CTkFrame(main_frame)
        options_section.pack(fill="x", pady=10)

        ctk.CTkLabel(options_section, text="Options de téléchargement",
                     font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=(10, 10), padx=10)

        # Options en grille
        options_grid = ctk.CTkFrame(options_section)
        options_grid.pack(fill="x", padx=10, pady=(0, 10))

        # Ligne 1 - Format et Qualité
        ctk.CTkLabel(options_grid, text="Format:").grid(row=0, column=0, sticky="w", padx=5, pady=10)
        self.format_combo = ctk.CTkComboBox(options_grid, variable=self.format_var,
                                            values=["mp4", "mp3"], width=150,
                                            command=self.on_format_change)
        self.format_combo.grid(row=0, column=1, padx=5, pady=10)

        ctk.CTkLabel(options_grid, text="Qualité:").grid(row=0, column=2, sticky="w", padx=20, pady=10)
        self.quality_combo = ctk.CTkComboBox(options_grid, variable=self.quality_var,
                                             values=["720", "1080", "480", "360", "best"], width=150)
        self.quality_combo.grid(row=0, column=3, padx=5, pady=10)

        # Dossier de destination
        path_section = ctk.CTkFrame(main_frame)
        path_section.pack(fill="x", pady=10)

        ctk.CTkLabel(path_section, text="Dossier de destination:",
                     font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=(10, 5), padx=10)

        path_frame = ctk.CTkFrame(path_section)
        path_frame.pack(fill="x", padx=10, pady=(0, 10))

        path_entry = ctk.CTkEntry(path_frame, textvariable=self.download_path_var)
        path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        ctk.CTkButton(path_frame, text="Parcourir", width=100,
                      command=self.browse_directory).pack(side="right")

        # Section Informations
        info_section = ctk.CTkFrame(main_frame)
        info_section.pack(fill="x", pady=10)

        ctk.CTkLabel(info_section, text="Informations sur la vidéo",
                     font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=(10, 5), padx=10)

        self.info_text = ctk.CTkTextbox(info_section, height=80)
        self.info_text.pack(fill="x", padx=10, pady=(0, 10))
        self.info_text.insert("1.0", "Aucune vidéo sélectionnée\nCollez une URL et cliquez sur 'Obtenir les infos'")
        self.info_text.configure(state="disabled")

        # Section Progression
        progress_section = ctk.CTkFrame(main_frame)
        progress_section.pack(fill="x", pady=10)

        ctk.CTkLabel(progress_section, text="Progression du téléchargement",
                     font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=(10, 5), padx=10)

        self.progress_bar = ctk.CTkProgressBar(progress_section, height=20)
        self.progress_bar.pack(fill="x", padx=10, pady=(0, 5))
        self.progress_bar.set(0)

        self.progress_label = ctk.CTkLabel(progress_section, text="Prêt pour le téléchargement")
        self.progress_label.pack(pady=(0, 10))

        # Section Boutons - BIEN VISIBLE
        button_section = ctk.CTkFrame(main_frame)
        button_section.pack(fill="x", pady=20)

        # Frame pour les boutons principaux
        main_buttons_frame = ctk.CTkFrame(button_section)
        main_buttons_frame.pack(pady=10)

        # BOUTON TÉLÉCHARGER - GRAND ET BIEN VISIBLE
        self.download_btn = ctk.CTkButton(
            main_buttons_frame,
            text="🚀 TÉLÉCHARGER",
            command=self.start_download,
            height=50,
            width=200,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#2AA876",
            hover_color="#228B61"
        )
        self.download_btn.pack(pady=10)

        # Frame pour les boutons secondaires
        secondary_buttons_frame = ctk.CTkFrame(button_section)
        secondary_buttons_frame.pack(pady=5)

        ctk.CTkButton(secondary_buttons_frame, text="Obtenir les infos",
                      command=self.get_video_info,
                      height=35, width=140).pack(side="left", padx=5)

        ctk.CTkButton(secondary_buttons_frame, text="Effacer tout",
                      command=self.clear_all,
                      height=35, width=140).pack(side="left", padx=5)

        ctk.CTkButton(secondary_buttons_frame, text="À propos",
                      command=self.show_about,
                      height=35, width=140).pack(side="left", padx=5)

        ctk.CTkButton(secondary_buttons_frame, text="Quitter",
                      command=self.root.quit,
                      height=35, width=140,
                      fg_color="#D35B58",
                      hover_color="#B34A47").pack(side="left", padx=5)

    def show_about(self):
        """Affiche la fenêtre À propos"""
        about_window = ctk.CTkToplevel(self.root)
        about_window.title("À propos")
        about_window.geometry("600x500")
        about_window.resizable(False, False)
        about_window.transient(self.root)

        # Centrer la fenêtre
        about_window.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - about_window.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - about_window.winfo_height()) // 2
        about_window.geometry(f"+{x}+{y}")

        # Focus et grab après que la fenêtre soit visible
        about_window.after(100, lambda: about_window.grab_set())

        # Contenu de la fenêtre À propos
        main_frame = ctk.CTkFrame(about_window)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Titre
        title_label = ctk.CTkLabel(main_frame, text="D YT Downloader",
                                   font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=(0, 20))

        # Description
        desc_text = (
            "Application de téléchargement YouTube\n"
            "Développée avec Python et CustomTkinter\n\n"
            "📧 Contact : andriniaina.2am@gmail.com\n\n"
            "💡 Transformons vos idées en applications !\n\n"
            "Du concept au code, je vous accompagne pour créer vos projets web et desktop,\n"
            "avec des tarifs abordables."
        )

        desc_label = ctk.CTkLabel(main_frame, text=desc_text,
                                  font=ctk.CTkFont(size=14),
                                  justify="center")
        desc_label.pack(pady=10)

        # Signature
        signature_label = ctk.CTkLabel(main_frame, text="Développé par DR4KEN ☠️",
                                       font=ctk.CTkFont(size=16, weight="bold"))
        signature_label.pack(pady=(20, 10))

        # Bouton Fermer
        ctk.CTkButton(main_frame, text="Fermer",
                      command=about_window.destroy,
                      width=100).pack(pady=20)

    def on_format_change(self, choice):
        """Met à jour les options de qualité selon le format"""
        if self.format_var.get() == "mp3":
            self.quality_combo.configure(values=["best", "128k", "192k", "320k"])
            self.quality_var.set("best")
        else:
            self.quality_combo.configure(values=["720", "1080", "480", "360", "best"])
            self.quality_var.set("720")

    def browse_directory(self):
        """Ouvre une boîte de dialogue pour choisir le dossier de destination"""
        directory = filedialog.askdirectory()
        if directory:
            self.download_path_var.set(directory)

    def get_video_info(self):
        """Récupère les informations de la vidéo"""
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Erreur", "Veuillez entrer une URL YouTube")
            return

        self.progress_label.configure(text="Récupération des informations...")

        def info_thread():
            try:
                ydl_opts = {
                    'quiet': True,
                    'no_warnings': True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    self.root.after(0, self.update_video_info, info)

            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Erreur",
                                                                f"Impossible de récupérer les informations:\n{str(e)}"))
                self.root.after(0, lambda: self.progress_label.configure(text="Erreur lors de la récupération"))

        threading.Thread(target=info_thread, daemon=True).start()

    def update_video_info(self, info):
        """Met à jour les informations de la vidéo dans l'interface"""
        title = info.get('title', 'Titre inconnu')
        duration = info.get('duration', 0)
        uploader = info.get('uploader', 'Inconnu')
        view_count = info.get('view_count', 0)

        # Convertir la durée
        if duration:
            minutes, seconds = divmod(duration, 60)
            hours, minutes = divmod(minutes, 60)
            if hours > 0:
                duration_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            else:
                duration_str = f"{minutes:02d}:{seconds:02d}"
        else:
            duration_str = "Inconnue"

        # Formater le nombre de vues
        if view_count:
            if view_count > 1000000:
                views_str = f"{view_count / 1000000:.1f}M"
            elif view_count > 1000:
                views_str = f"{view_count / 1000:.1f}K"
            else:
                views_str = str(view_count)
        else:
            views_str = "Inconnu"

        info_text = f"""📹 Titre: {title}
👤 Auteur: {uploader}
⏱️ Durée: {duration_str}
👁️ Vues: {views_str}
📊 Format: {self.format_var.get().upper()}
🎯 Qualité: {self.quality_var.get()}

✅ Prêt pour le téléchargement!"""

        self.info_text.configure(state="normal")
        self.info_text.delete("1.0", "end")
        self.info_text.insert("1.0", info_text)
        self.info_text.configure(state="disabled")

        self.progress_label.configure(text="Informations récupérées - Prêt à télécharger!")

    def start_download(self):
        """Démarre le téléchargement"""
        if self.downloading:
            return

        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Erreur", "Veuillez entrer une URL YouTube")
            return

        if not os.path.exists(self.download_path_var.get()):
            try:
                os.makedirs(self.download_path_var.get())
            except:
                messagebox.showerror("Erreur", "Impossible de créer le dossier de destination")
                return

        self.downloading = True
        self.download_btn.configure(state='disabled', text="⏳ Téléchargement en cours...")
        self.progress_bar.set(0)
        self.progress_label.configure(text="Démarrage du téléchargement...")

        def download_thread():
            try:
                self.download_video()
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Erreur", f"Erreur lors du téléchargement:\n{str(e)}"))
            finally:
                self.root.after(0, self.download_finished)

        threading.Thread(target=download_thread, daemon=True).start()

    def progress_hook(self, d):
        """Hook pour suivre la progression du téléchargement"""
        if d['status'] == 'downloading':
            if 'total_bytes' in d and d['total_bytes']:
                percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
            elif 'total_bytes_estimate' in d and d['total_bytes_estimate']:
                percent = (d['downloaded_bytes'] / d['total_bytes_estimate']) * 100
            else:
                percent = 0

            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            status = f"Vitesse: {speed} | ETA: {eta}"

            self.root.after(0, self.update_progress, percent, status)

        elif d['status'] == 'finished':
            self.root.after(0, self.update_progress, 100, "Téléchargement terminé!")

    def update_progress(self, percent, status):
        """Met à jour la barre de progression"""
        self.progress_bar.set(percent / 100)
        self.progress_label.configure(text=f"{percent:.1f}% - {status}")

    def download_video(self):
        """Effectue le téléchargement avec yt-dlp"""
        url = self.url_var.get().strip()
        format_type = self.format_var.get()
        quality = self.quality_var.get()

        # Configuration yt-dlp
        ydl_opts = {
            'outtmpl': os.path.join(self.download_path_var.get(), '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
        }

        # Configuration selon le format
        if format_type == "mp3":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': quality.replace('k', '') if quality != 'best' else '192',
                }],
            })
        else:
            # Pour mp4
            if quality == 'best':
                ydl_opts['format'] = 'best[ext=mp4]/best'
            else:
                ydl_opts['format'] = f'best[height<={quality}]/best[ext=mp4]/best'

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.root.after(0, lambda: messagebox.showinfo("Succès", "✅ Téléchargement terminé avec succès!"))

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Erreur", f"❌ Erreur: {str(e)}"))

    def download_finished(self):
        """Appelé quand le téléchargement est terminé"""
        self.downloading = False
        self.download_btn.configure(state='normal', text="TÉLÉCHARGER")

    def clear_all(self):
        """Efface tous les champs"""
        self.url_var.set("")
        self.info_text.configure(state="normal")
        self.info_text.delete("1.0", "end")
        self.info_text.insert("1.0", "Aucune vidéo sélectionnée\nCollez une URL et cliquez sur 'Obtenir les infos'")
        self.info_text.configure(state="disabled")
        self.progress_bar.set(0)
        self.progress_label.configure(text="Prêt pour le téléchargement")


def main():
    root = ctk.CTk()
    app = YouTubeDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()