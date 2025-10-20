# D YT Downloader

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-fedora.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Une application desktop moderne et intuitive pour télécharger des vidéos et audios depuis YouTube, développée avec Python et CustomTkinter. **Aucune installation requise** - versions prêtes à l'emploi disponibles !

## ✨ Fonctionnalités

- 🎬 **Téléchargement vidéo** - Support MP4 avec différentes qualités (360p, 480p, 720p, 1080p)
- 🎵 **Extraction audio** - Conversion en MP3 avec différentes qualités (128k, 192k, 320k)
- 📊 **Informations détaillées** - Affiche le titre, auteur, durée et statistiques des vidéos
- 🚀 **Interface moderne** - Design épuré avec CustomTkinter
- 📁 **Gestion des dossiers** - Choix personnalisé du dossier de destination
- ⏳ **Progression en temps réel** - Barre de progression et statistiques de téléchargement
- 🔍 **Validation des URLs** - Récupération automatique des informations vidéo
- 💻 **Portable** - Aucune installation nécessaire, double-cliquez et utilisez !

## 📦 Téléchargement

### Versions Disponibles

| Plateforme | Fichier | Taille | Statut |
|------------|---------|--------|---------|
| **Windows** | `D_YT_Downloader_Windows.exe` | ~50 MB | ✅ Prêt |
| **Fedora/Linux** | `D_YT_Downloader_Fedora` | ~45 MB | ✅ Prêt |

### 📥 Comment télécharger

1. **Téléchargez la version correspondant à votre système d'exploitation**
2. **Double-cliquez sur le fichier téléchargé**
3. **C'est parti ! 🎉**

## 🚀 Utilisation Rapide

### Pour Windows :
1. 📥 Téléchargez `D_YT_Downloader_Windows.exe`
2. 🖱️ Double-cliquez sur le fichier
3. 🌟 L'application s'ouvre instantanément
4. 🔗 Collez votre URL YouTube et téléchargez !

### Pour Fedora/Linux :
1. 📥 Téléchargez `D_YT_Downloader_Fedora`
2. 🔒 Rendez le fichier exécutable :
   ```bash
   chmod +x D_YT_Downloader_Fedora
   ```

## ✨ Fonctionnalités

- 🎬 **Téléchargement vidéo** - Support MP4 avec différentes qualités (360p, 480p, 720p, 1080p)
- 🎵 **Extraction audio** - Conversion en MP3 avec différentes qualités (128k, 192k, 320k)
- 📊 **Informations détaillées** - Affiche le titre, auteur, durée et statistiques des vidéos
- 🚀 **Interface moderne** - Design épuré avec CustomTkinter
- 📁 **Gestion des dossiers** - Choix personnalisé du dossier de destination
- ⏳ **Progression en temps réel** - Barre de progression et statistiques de téléchargement
- 🔍 **Validation des URLs** - Récupération automatique des informations vidéo

## 📸 Captures d'écran

### Interface principale
<img width="750" height="1010" alt="Capture d’écran du 2025-10-20 09-02-56" src="https://github.com/user-attachments/assets/44f998d0-be0b-48c3-aaec-d3fb1e5bda93" />


### Téléchargement terminé
<img width="707" height="965" alt="Capture d’écran du 2025-10-20 09-32-29" src="https://github.com/user-attachments/assets/69798c83-0eff-416d-81b8-f9d22dec6649" />


### Fenêtre À propos
<img width="650" height="587" alt="Capture d’écran du 2025-10-20 09-03-33" src="https://github.com/user-attachments/assets/5a7785f3-dd65-4989-8369-1eec2e978395" />

## ⚙️ Pour les Développeurs

Développement et Compilation

Si vous souhaitez compiler vous-même l'application :
Prérequis
```bash

pip install customtkinter yt-dlp pyinstaller
```

Compilation pour Windows
```bash

pyinstaller --onefile --windowed --name "D_YT_Downloader_Windows" main.py
```

Compilation pour Linux
```bash

pyinstaller --onefile --name "D_YT_Downloader_Fedora" main.py
```

Structure du code
```text

d-yt-downloader/
├── main.py                 # Application principale
├── build/                  # Fichiers de build
├── dist/                   # Exécutables générés
```
✨ "Simple, rapide, efficace - Téléchargez sans complexité!" ✨

Développé avec ❤️ par DR4KEN ☠️
