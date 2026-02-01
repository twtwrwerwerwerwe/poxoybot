from telethon import TelegramClient, events

# =================== TELEGRAM API ===================
api_id = 35866911
api_hash = '62b2dda72eb7f9648d09b23110398946'

client = TelegramClient('taxi_session_fast', api_id, api_hash)

# =================== SKIP CHAT ID ===================
SKIP_CHAT_IDS = {
    -1003565381874
}

# =================== TARGET CHAT ID ===================
TARGET_CHAT_IDS = {
    -1003565381874
}

# =================== KALIT SO‘ZLAR ===================
KEYWORDS = [
    # odam bor
    'odam bor','odambor','odam bor ekan','odam bor edi','odam borakan',
    'bitta odam bor','ikkita odam bor','uchta odam bor',"to'rtta odam bor",'tortta odam bor',
    'komplek odam bor','komplekt odam bor','kompilek odam bor','kampilek odam bor',
    '1ta odam bor','2ta odam bor','3ta odam bor','4ta odam bor',
    'odam bor 1','odam bor 2','odam bor 3','odam bor 4',
    'rishtonga odam bor','toshkentga odam bor',"toshkendan farg'onaga odam bor",
    'тўрта одам бор','одам бор','комплект одам бор','компилект odam бор','кампилек одам бор',
    'towga 1kishi', 'toshkentga 1kishi', "farg'onaga 1kishi", 'rishtonga 1kishi', '1kishi bor',
    'towga 2kishi', 'toshkentga 2kishi', "farg'onaga 2kishi", 'rishtonga 2kishi', '2kishi bor',
    'towga 3kishi', 'toshkentga 3kishi', "farg'onaga 3kishi", 'rishtonga 3kishi', '3kishi bor',
    'towga 4kishi', 'toshkentga 4kishi', "farg'onaga 4kishi", 'rishtonga 4kishi', '4kishi bor',
    'машина бор','одам бор эди','одам бор экан','одам бор 1','одам бор 2','одам бор 3','одам бор 4',
    'битта одам бор','иккита одам бор','учта одам бор','комплек одам бор','1та одам бор','2та одам бор',
    '3та одам бор','4та одам бор', 'toshkentdan bir kishi', 'rishtonga bir kishi', '1 ta qiz bor', 'ayol kishi bor mashina sorashyabdi',
    'Chirchiqdan 1 kishi', 'Yangiyuldan 1 kishi', 'Zangiotadan 1 kishi', 'Qibraydan 1 kishi', '1 kishi bor',
    '2-ta odam bor', '2-kishi bor', '3-ta odam bor', '3-kishi bor', '4-ta odam bor', '4-kishi bor',
    '2-ta kishi bor', '3-ta kishi bor', '4-ta kishi bor', '2-ta ayolkishi bor', '3-ta ayolkishi bor', '4-ta ayolkishi bor', "odam.bor", 
    
    # mashina kerak
    'mashina kerak','mashina kere','mashina kerek','mashina kera','mashina keraa',
    'bagajli mashina kerak','bosh mashina kerak','bosh mashina bormi','boshi bormi',
    'mashina izlayapman','mashina topaman','mashina kerak edi',
    'машина керак','багажли машина керак','бош машина керак','машина кере','машina кераа',

    # pochta bor
    'pochta bor','pochta kerak','pochta ketadi','pochta olib ketadi','pochta bormi',
    'почта бор','почта кетади','почта керак','почта олиб кетади',
    'тошкентга почта бор','тошкентдан почта бор','риштонга почта бор','риштондан почта бор',

    # dostavka
    'dastavka bor','dostavka bor','dastafka','dastafka bor',
    'доставкa бор','даставка бор','доставка бор','доставкa керак',
    "Toshkentdan Rishtonga 1odam bor", '1odam bor', '1ta kamla', 'bitta kamlarga', '1ta kamlarga',
    '1 ta kamlarga', '2kiwimiz', "bagajga yuk bor", '2kishimiz', "2 kiwimiz", "2 kishimiz", "2kiwimiz", 
    "3kiwimiz", "3 kiwimiz", "3 kishimiz", "3kishimiz", "4kishimiz", "4kiwimiz", "4 kishimiz", "4 kiwimiz",
    "Toshkentga 1kishi", "Toshkenga 1kishi", "Rishtonga 1kishi", "Rishotondan 1kiwi", "poshta  bor", "moshina kerak",
    "ayollar bor mashina kerak", "ayollar bor moshina kerak", "Toshkentga 1ta odam bor", "1 ta qiz bola bor", "qiz bola bor",
    "1ta qiz bor", "1ta qiz bola bor", 'одам бор',
    'одам бор экан','одам бор эди','битта одам бор','иккита одам бор','учта одам бор','тўртта одам бор','1та одам бор','2та одам бор','3та одам бор','4та одам бор','одам бор 1','одам бор 2','одам бор 3','одам бор 4',

    'комплек одам бор','комплект одам бор','компилек одам бор','кампилек одам бор',
    'кетади', 'кетвотти', 'кетиши керак', "shopir kerak", "1kishi ayol kishili mashina kerak", 
    "gazalkentdan 1kishi", "g'azalkentdan 1kishi", "gazalkentdan 2kishi", "g'azalkantdan 2 kishi",
    "o'zimizdan 1kishi", "ozimizdan 1kishi", "ozimizdan 2 kishi", "ozimizdan kim bor", "o'zimizdan kim bor",
    "yengil mashina kerak", "amirsoydan 1kishi", "qoqonga 1kishi", "kim yurapti akalar", "pustoy mashina kerak",
    "kobalt kerak", "jentra kerak", "bosh mashina bormi", "uchkoprikda 1kishi", "uchkoprikdan 1kishi", "chirchiqdan 1kishi",
    "yangiqorgondan 1kishi", "tashkentdan rishtonga odam bor", "toshkendan bog'dodga odam bor", "toshkentdan bagdodga odam bor",
    "4 odam bor", "2ta ayol bor", "katta yoshli ayol bor", "bir qiz bir bola bor", "srochni yuradigan taxi kerak",
    "kim yuryabdi", "toshkentga ketaman", "bagdodga ketishi kerak", "bagdodan 1kishi bor", "bog'doddan 2kishi",
    'кетади', 'кетвотти', 'кетиши керак', "шопир керак", "1киши аёл кишили машина керак",
    "газалкентдан 1киши", "ғазалкентдан 1киши", "газалкентдан 2киши", "ғазалкентдан 2 киши",
    "ўзимиздан 1киши", "озимиздан 1киши", "озимиздан 2 киши", "озимиздан ким бор", "ўзимиздан ким бор",
    "енгил машина керак", "амирсойдан 1киши", "қўқонга 1киши", "ким юрапти акалар", "пустой машина керак", "1 kiwi bor",
    "Тунилдан тушямиз бешарика 1киши бор", "Тошкентдан 1 киши бор"
]

# =================== HANDLER ===================
@client.on(events.NewMessage(incoming=True))
async def handler(event):

    if not (event.is_group or event.is_channel):
        return

    if event.chat_id in SKIP_CHAT_IDS:
        return

    text = event.raw_text
    if not text:
        return

    text_l = text.lower()

    # ⚡ ENG TEZ FILTR
    if not any(k in text_l for k in KEYWORDS):
        return

    # 🔗 LINKLAR
    sender_link = f"tg://user?id={event.sender_id}"
    
    # Telegram xabar linki uchun: private chat bo'lsa chat_id musbat, kanal bo'lsa -100xxxx → c/<chat_id>/<msg_id>
    if str(event.chat_id).startswith("-100"):
        chat_link = f"https://t.me/c/{str(event.chat_id)[4:]}/{event.id}"
    else:
        chat_link = f"https://t.me/c/{event.chat_id}/{event.id}"

    msg = (
        "🚖 <b>XAMROH TAXI</b>\n\n"
        f"📝 {text}\n\n"
        f"👤 <a href='{sender_link}'>Profilga o‘tish</a>\n"
        f"🔗 <a href='{chat_link}'>Xabarga o‘tish</a>"
    )

    for target_id in TARGET_CHAT_IDS:
        await client.send_message(target_id, msg, parse_mode="html")


# =================== START ===================
print("🚀 TEZ TAXI BOT ISHGA TUSHDI")
client.start()
client.run_until_disconnected()
