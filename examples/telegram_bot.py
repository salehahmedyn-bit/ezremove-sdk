import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# استيراد مكتبتك التي صممتها
from ezremove import EzRemoveClient, EzRemoveError

# إعداد السجلات (Logging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# توكن البوت الخاص بك من BotFather
TOKEN = '8580089339:AAHFAyuHTPO0YcqX9Tq6LttMh7f5DJfHhmY'

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    photo_file = await update.message.photo[-1].get_file()
    
    # مسار مؤقت لحفظ الصورة
    input_path = f"temp_{user.id}_{photo_file.file_id}.png"
    
    try:
        sent_msg = await update.message.reply_text("⏳ جاري رفع الصورة ومعالجتها...")
        
        # تحميل الصورة من تليجرام
        await photo_file.download_to_drive(input_path)
        
        # استخدام مكتبتك (salah-ahmedyn)
        client = EzRemoveClient()
        result_url = await client.remove_background(input_path)
        
        # إرسال النتيجة للمستخدم
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=sent_msg.message_id,
            text=f"✅ تمت إزالة الخلفية بنجاح!\n\n🔗 الرابط المباشر:\n{result_url}"
        )
        
        # اختياري: إرسال الصورة كملف أو صورة مباشرة
        # await update.message.reply_document(document=result_url, caption="النتيجة")

    except EzRemoveError as e:
        await update.message.reply_text(f"❌ خطأ في المعالجة: {str(e)}")
    except Exception as e:
        await update.message.reply_text(f"⚠️ حدث خطأ غير متوقع: {str(e)}")
    finally:
        # تنظيف الملفات المؤقتة
        if os.path.exists(input_path):
            os.remove(input_path)

if __name__ == '__main__':
    # التأكد من وجود توكن
    if 'ضغ_هنا_توكن_بوتك' in TOKEN:
        print("❌ من فضلك ضع توكن البوت أولاً!")
    else:
        print("🤖 البوت يعمل الآن...")
        app = ApplicationBuilder().token(TOKEN).build()
        
        # التعامل مع الصور فقط
        app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
        
        app.run_polling()
