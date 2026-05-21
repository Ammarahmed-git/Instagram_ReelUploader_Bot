<div align="center">

# 🎬 Instagram Reel Uploader Bot

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=E4405F&center=true&vCenter=true&width=600&lines=Automate+Your+Instagram+Reels+%F0%9F%9A%80;AI-Powered+Viral+Captions+%F0%9F%A4%96;Set+It+%26+Forget+It+%E2%9C%85" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1--mini-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![Instagram](https://img.shields.io/badge/Instagram-API-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://instagram.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=flat-square)](https://github.com/Ammarahmed-git)

<br/>

> **Fully automated Instagram Reel uploader powered by AI.**  
> Drop your videos in a folder — the bot handles uploads, captions, hashtags & scheduling. Hands-free. 🔥

</div>

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🤖 **AI Captions** | Auto-generates viral captions with emojis & hashtags using GPT-4.1-mini |
| 📅 **Scheduled Uploads** | Posts a Reel every 20 minutes automatically |
| 🎲 **Smart Picker** | Randomly selects an unwatched video from your folder |
| 🕵️ **Human-like Delay** | Randomized 30–120s delay before each upload to mimic real behavior |
| 📁 **Auto-Archiving** | Moves uploaded videos to an `uploaded/` folder to avoid duplicates |
| 🔐 **Secure Credentials** | All sensitive data stored safely in a `.env` file |

---

## 🗂️ Project Structure

```
Instagram_ReelUploader_Bot/
│
├── bot.py              # 🤖 Main bot logic
├── .env                # 🔐 Your credentials (never commit this!)
├── videos/             # 📂 Drop your .mp4 files here
└── uploaded/           # ✅ Processed videos are moved here
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ammarahmed-git/Instagram_ReelUploader_Bot.git
cd Instagram_ReelUploader_Bot
```

### 2️⃣ Install Dependencies

```bash
pip install instagrapi openai schedule python-dotenv
```

### 3️⃣ Configure Your `.env` File

```env
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
OPENAI_API_KEY=your_openai_api_key
```

> ⚠️ **Never push your `.env` file to GitHub.** Add it to `.gitignore`.

### 4️⃣ Add Your Videos

Place your `.mp4` reel files inside the `videos/` folder:

```
videos/
├── clip1.mp4
├── clip2.mp4
└── clip3.mp4
```

### 5️⃣ Run the Bot

```bash
python bot.py
```

The bot will start, log in to Instagram, and begin uploading every **20 minutes**. 🚀

---

## 🔄 How It Works

```
🟢 Bot starts
    │
    ▼
📂 Scans videos/ folder for .mp4 files
    │
    ▼
🎲 Randomly picks one video
    │
    ▼
🤖 Sends video name to GPT-4.1-mini → generates viral caption + hashtags
    │
    ▼
⏱️ Waits 30–120 seconds (human-like behavior)
    │
    ▼
📤 Uploads Reel to Instagram via instagrapi
    │
    ▼
📁 Moves video to uploaded/ folder
    │
    ▼
🔁 Repeats every 20 minutes
```

---

## 📦 Dependencies

| Package | Purpose |
|--------|---------|
| `instagrapi` | Instagram private API client |
| `openai` | GPT-4.1-mini caption generation |
| `schedule` | Task scheduling every 20 minutes |
| `python-dotenv` | Load credentials from `.env` |
| `shutil` | Move uploaded videos to archive |

---

## ⚠️ Disclaimer

> This bot uses Instagram's **private API** via `instagrapi`.  
> Use responsibly and at your own risk. Automating Instagram activity may violate their [Terms of Service](https://help.instagram.com/581066165581870).  
> The author is not responsible for any account restrictions or bans.

---

## 🙋‍♂️ Author

<div align="center">

**Ammar Ahmed** — CS Graduate & Full-Stack Developer 🇵🇰

[![Portfolio](https://img.shields.io/badge/🚀%20Portfolio-Click%20to%20Explore!-ff6b6b?style=for-the-badge&labelColor=000000&logoColor=white)](https://ammarahmed-git.github.io/Portfolio/)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://pk.linkedin.com/in/ammar-ahmed-1606a1242)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ammarahmed-git)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/me._ammar_ammu/)
[![Gmail](https://img.shields.io/badge/-Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:Innoxentammar27@gmail.com)

</div>

---

<div align="center">

*Always learning, always building — made with coffee and love.* 🚀

[![⭐ Star this repo](https://img.shields.io/badge/⭐%20Star%20this%20repo-if%20you%20found%20it%20helpful!-FFD700?style=for-the-badge&labelColor=1a1a2e)](https://github.com/Ammarahmed-git/Instagram_ReelUploader_Bot)

</div>
