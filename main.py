from telethon.sync import TelegramClient, events
import os
api_id = 16849961
api_hash = "9cfc747e09ea7147f6132ecc53ec84f6"
bot = TelegramClient('SecretBot', api_id, api_hash).start()

@bot.on(events.NewMessage(pattern=r'(بصبر دان بشه|بصبر دان شه|بصب دان شه|بصب دان بشه)', func=lambda e: e.is_reply))
async def show_image(event):
    userid = await bot.get_me()
    if event.sender_id == userid.id:
        try:
            message = await event.get_reply_message()
            download = await bot.download_media(message)
            await bot.send_message('me', f'عکس نابود شونده از مرحوم 😂😂', file=download)
            os.remove(download)
        except Exception as e:
            await bot.send_message('me', f"خطایی دریافت شد:\n\n{e}")

bot.run_until_disconnected()
