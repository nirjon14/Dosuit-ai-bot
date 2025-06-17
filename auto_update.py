import os
import requests

# ✅ GitHub RAW URL (main.py এর সরাসরি লিংক)
GITHUB_RAW_URL = "https://raw.githubusercontent.com/nirjon14/Dosuit-ai-bot/main/main.py"

def download_and_run():
    # 🔽 কোড নামান
    response = requests.get(GITHUB_RAW_URL)
    if response.status_code == 200:
        with open("main.py", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("✅ কোড আপডেট সম্পন্ন!")
    else:
        print("❌ কোড ডাউনলোড করতে সমস্যা হয়েছে")

    # ▶️ চালু করুন
    os.system("python main.py")

if __name__ == "__main__":
    download_and_run()
