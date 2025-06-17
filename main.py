from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

# ✅ /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠✨ স্বাগতম ‘DoSuit Ai’ বটে!\n\n"
        "🔹 আমি আপনার ডিজিটাল সহকারী ‘Wazifa Ai’ 🧕\n"
        "🔹 তৈরি করেছে 🇧🇩 বাংলাদেশি প্ল্যাটফর্ম ‘DoZone’ 🇧🇩\n\n"
        "💼 আমি প্রস্তুত আপনাকে বিভিন্ন প্রফেশনাল সার্ভিস দিতে —\n"
        "🎬 ভিডিও এডিট, 🖼️ ফটো এডিট, 🧠 AI সহায়তা, ☪️ ইসলামিক আলোচনার মতো আরও অনেক কিছু!\n\n"
        "👇 নিচে থাকা '📦 মেনু' তে ক্লিক করে সার্ভিস নির্বাচন করুন\n"
        "ধন্যবাদ আপনাকে ❤️"
    )

# ✅ /menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_page(update, context, 1)

# ✅ মেনু পেজিং
async def send_page(update, context, page):
    if update.callback_query:
        chat_id = update.callback_query.message.chat.id
        await update.callback_query.answer()
    else:
        chat_id = update.message.chat.id

    if page == 1:
        keyboard = [
            [InlineKeyboardButton("🎬 ভিডিও এডিট", callback_data="video_edit")],
            [InlineKeyboardButton("🖼️ ফটো এডিট", callback_data="photo_edit")],
            [InlineKeyboardButton("📼 CapCut/Remini Pro", callback_data="capcut")],
            [InlineKeyboardButton("🛠️ ওয়েব/সফটওয়্যার অর্ডার", callback_data="web_order")],
            [InlineKeyboardButton("📱 ফেসবুক/টিকটক লাইক/ফলোয়ার", callback_data="smm_social")],
            [InlineKeyboardButton("➡️ পরের পেজ", callback_data="page_2")]
        ]
    elif page == 2:
        keyboard = [
            [InlineKeyboardButton("🤖 ওয়াজিফা Ai", callback_data="wazifa_ai")],
            [InlineKeyboardButton("🏚 নুর Ai", callback_data="nur_ai")],
            [InlineKeyboardButton("📞 কাস্টমার কেয়ার", callback_data="customer_care")],
            [InlineKeyboardButton("📲 টেলিকম সার্ভিস", callback_data="telecom")],
            [InlineKeyboardButton("🔥 ফ্রী ফায়ার / পাবজি টপআপ", callback_data="topup")],
            [InlineKeyboardButton("➡️ পেজ ৩", callback_data="page_3"), InlineKeyboardButton("⬅️ পেজ ১", callback_data="page_1")]
        ]
    else:
        keyboard = [
            [InlineKeyboardButton("🔑 সাইনইউপ / সাইনইন", callback_data="auth")],
            [InlineKeyboardButton("💳 এড বেলেন্স", callback_data="add_balance")],
            [InlineKeyboardButton("⬅️ পেছনে", callback_data="page_2")]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=chat_id, text="📦 নিচে থেকে আপনার প্রয়োজনীয় সার্ভিস বেছে নিন:", reply_markup=reply_markup)

# ✅ Callback handler
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    if data.startswith("page_"):
        page_num = int(data.split("_")[1])
        await send_page(update, context, page_num)
    else:
        await update.callback_query.answer("🚧 ফিচারটি এখনো তৈরি হচ্ছে!")

# ✅ Bot Run
token = os.environ.get("BOT_TOKEN")
if not token:
    print("❌ টোকেন পাওয়া যায়নি! দয়া করে .env ফাইলে BOT_TOKEN=... সঠিকভাবে সেট করুন।")
else:
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.run_polling()
