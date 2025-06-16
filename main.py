from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os  # ✅ এনভায়রনমেন্ট ভেরিয়েবল পড়ার জন্য

# ✅ /start ফাংশন
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 স্বাগতম DoSuit Ai বটে, DoZone ডিজিটাল সহকারী ✅")

# ✅ /menu ফাংশন
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 ভিডিও এডিট", callback_data="video_edit")],
        [InlineKeyboardButton("🖼️ ফটো এডিট", callback_data="photo_edit")],
        [InlineKeyboardButton("📼 CapCut/Remini Pro", callback_data="capcut")],
        [InlineKeyboardButton("🛠️ ওয়েব/সফটওয়্যার অর্ডার", callback_data="web_order")],
        [InlineKeyboardButton("📱 ফেসবুক/টিকটক লাইক/ফলোয়ার", callback_data="smm_social")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📦 নিচে থেকে আপনার প্রয়োজনীয় সার্ভিস বেছে নিন:", reply_markup=reply_markup)

# ✅ অ্যাপ রান কনফিগার
app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()

# ✅ বাটন ভাসানো — Menu Command set করা
async def set_menu():
    await app.bot.set_my_commands([
        BotCommand("start", "🤖 বট চালু করুন"),
        BotCommand("menu", "📦 সার্ভিস মেনু দেখুন"),
    ])

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))

# ✅ শুরুতে বাটন সেট করে তারপর চালু
app.post_init = set_menu
app.run_polling()
