from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os

# ✅ /start ফাংশন
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

# ✅ /menu ফাংশন
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_page(update, 1)

# ✅ পেজ ভিত্তিক সার্ভিস মেনু
async def send_page(update, page):
    if isinstance(update, Update) and update.callback_query:
        query = update.callback_query
        await query.answer()
        chat_id = query.message.chat_id
    else:
        chat_id = update.message.chat_id

    if page == 1:
        keyboard = [
            [InlineKeyboardButton("🎬 ভিডিও এডিট", callback_data="video_edit")],
            [InlineKeyboardButton("🖼️ ফটো এডিট", callback_data="photo_edit")],
            [InlineKeyboardButton("📼 CapCut/Remini Pro", callback_data="capcut")],
            [InlineKeyboardButton("🛠️ ওয়েব/সফটওয়্যার অর্ডার", callback_data="web_order")],
            [InlineKeyboardButton("📱 ফেসবুক/টিকটক লাইক/ফলোয়ার", callback_data="smm_social")],
            [InlineKeyboardButton("➡️ পরের পেজ", callback_data="page_2")]
        ]
    else:
        keyboard = [
            [InlineKeyboardButton("🤖 ওয়াজিফা Ai", callback_data="wazifa_ai")],
            [InlineKeyboardButton("🕌 নুর Ai", callback_data="nur_ai")],
            [InlineKeyboardButton("📞 কাস্টমার কেয়ার", callback_data="customer_care")],
            [InlineKeyboardButton("📲 টেলিকম সার্ভিস", callback_data="telecom")],
            [InlineKeyboardButton("🔥 ফ্রী ফায়ার / পাবজি টপআপ", callback_data="topup")],
            [InlineKeyboardButton("⬅️ আগের পেজ", callback_data="page_1")]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=chat_id, text="📦 নিচে থেকে আপনার প্রয়োজনীয় সার্ভিস বেছে নিন:", reply_markup=reply_markup)

# ✅ Callback handler
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    if data == "page_1":
        await send_page(update, 1)
    elif data == "page_2":
        await send_page(update, 2)
    else:
        await query.answer("🚧 এই ফিচারটি এখনো তৈরি হচ্ছে!")

# ✅ বট রান কনফিগার
app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CallbackQueryHandler(handle_button))
app.run_polling()
