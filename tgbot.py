from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import  random
from pyrogram import Client, filters, sync
stop = False
client = Client("session", "21852716", "0e4435a275db20f49d9c647db2e59f80")

client.start()
client.stop()
print("[\033[33mинфо\033[37m] бот запусксется")
print("[\033[33mинфо\033[37m] получить код можно тут:  @tgbotcode_bot")
pas = input('\033[31m[безопасность]\033[37m Введите Пароль : ')
while pas != "PYTHON TG BOT":
    print("\033[31m[безопасность]\033[37m Пароль является неверным")
    pas = input('\033[31m[безопасность]\033[37m Введите Пароль Снова:')
    
print(" ___  __   __  _____   _  _    ___    _  _")
print("| _ \ \ \ / / |_   _| | || |  / _ \  | \| |  ")
print("|  _/  \ V /    | |   | __ | | (_) | | .` |  ")
print("|_|     |_|     |_|   |_||_|  \___/  |_|\_|")

print(" _____    ___ ")
print("|_   _|  / __|")
print("  | |   | (_ |")
print("  |_|    \___|")

print(" ___    ___    _____ ")
print("| _ )  / _ \  |_   _|")
print("| _ \ | (_) |   | |  ")
print("|___/  \___/    |_|  ")

print("https://discord.gg/cZSzNeRH дискорд сервер будет в helpall, help2 и срздатели")

print("бот успешно запушен!")

print("[обязательно] подписка на https://t.me/amongusimostorsus")

print("[помощь] напиши в телеграме .help")

# Команда spam
@client.on_message(
    filters.command(["спам", "spam"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    global stop
    args = message.text.split(" ")
    # if !args[1]:
    # client.send_message(message.chat.id, 'Используйте: /spam <кол-во сообщений> <сообщение>')
    if args[1] == "стоп":
        stop = True
        client.edit_message_text(
            message.chat.id, message.id, "Вы успешно отключили спам!"
        )
    i = int(args[1])
    args.pop(0)
    args.pop(0)
    while i >= 0:
        try:
            if stop == True:
                break
                i = 0
                stop = False
            client.send_message(message.chat.id, " ".join(args))
            sleep(1 / 15)
        except FloodWait as e:
            sleep(e.x)
        i -= 1


# Команда type
@client.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "|"

    while tbp != orig_text:
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)
@client.on_message(filters.command("try", prefixes=".") & filters.me)
def betaloves(_, msg):
	t = ["[Удачно]", "[Не удачно]"]

	try0 = random.choice(t)
	try1 = " ".join(msg.command[1:])

	if not try1:
		msg.edit(f'''
			**mistake for you 👻**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{try1} {try0}''')



# Команда moon
@client.on_message(
    filters.command(["moon", "луна"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, "🌑")
    client.edit_message_text(message.chat.id, message.id, "🌒")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌓")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌔")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌕")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌖")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌗")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌘")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌑")


# Команда moon1
@client.on_message(
    filters.command(["moon2", "луна2"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, "🌝")
    client.edit_message_text(message.chat.id, message.id, "🌚")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌝")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌚")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌝")
    sleep(1 / 2)
    client.edit_message_text(message.chat.id, message.id, "🌚")


# Команда clock
@client.on_message(filters.command("clock", prefixes=".") & filters.me)
async def clock(client, msg):
    text = " ".join(msg.command[1:])
    for i in range(1):
        await msg.edit("🕐")
        sleep(0.3)
        await msg.edit("🕑")
        sleep(0.3)
        await msg.edit("🕒")
        sleep(0.3)
        await msg.edit("🕓")
        sleep(0.3)
        await msg.edit("🕔")
        sleep(0.3)
        await msg.edit("🕕")
        sleep(0.3)
        await msg.edit("🕖")
        sleep(0.3)
        await msg.edit("🕗")
        sleep(0.3)
        await msg.edit("🕘")
        sleep(0.3)
        await msg.edit("🕙")
        sleep(0.3)
        await msg.edit("🕚")
        sleep(0.3)
        await msg.edit("🕛")
        sleep(0.3)


# Команда cloud
@client.on_message(filters.command("cloud", prefixes=".") & filters.me)
async def cloud(client, msg):
    text = " ".join(msg.command[1:])
    for i in range(1):
        await msg.edit("☁️")
        sleep(2)
        await msg.edit("🌥")
        sleep(2)
        await msg.edit("⛅️")
        sleep(2)
        await msg.edit("🌤")
        sleep(2)
        await msg.edit("☀️")
        sleep(1.5)


# Команда world
@client.on_message(filters.command("world", prefixes=".") & filters.me)
async def world(client, msg):
    text = " ".join(msg.command[1:])
    for i in range(5):
        await msg.edit("🌎")
        sleep(0.4)
        await msg.edit("🌍")
        sleep(0.4)
        await msg.edit("🌏")
        sleep(0.3)
        
@client.on_message(filters.command('uno', prefixes='.') & filters.me)
async def uno(client, msg):
	text = ' '.join(msg.command[1:])
	for i in range(1):
		await msg.edit('\n⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇\n')
		
@client.on_message(filters.command('pizza', prefixes='.') & filters.me)
async def pizza(client, msg):
	text = ' '.join(msg.command[1:])
	for i in range(1):
		await msg.edit('\n█████████████████████████\n█────█───█────█────█────█\n█─██─██─████──███──█─██─█\n█────██─███──███──██────█\n█─█████─██──███──███─██─█\n█─████───█────█────█─██─█\n█████████████████████████\n')		

@client.on_message(filters.command('pikachu', prefixes='.') & filters.me)
async def pikachu(client, msg):
	text = ' '.join(msg.command[1:])
	for i in range(1):
		await msg.edit('\n░█▀▀▄░░░░░░░░░░░▄▀▀█\n░█░░░▀▄░▄▄▄▄▄░▄▀░░░█\n░░▀▄░░░▀░░░░░▀░░░▄▀\n░░░░▌░▄▄░░░▄▄░▐▀▀\n░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█\n░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█\n▄▀▀▐▀▀░▄▄▄▄▄░▀▀▌▄▄▄░░░█\n█░░░▀▄░█░░░█░▄▀░░░░█▀▀▀\n░▀▄░░▀░░▀▀▀░░▀░░░▄█▀\n░░░█░░░░░░░░░░░▄▀▄░▀▄\n░░░█░░░░░░░░░▄▀█░░█░░█\n░░░█░░░░░░░░░░░█▄█░░▄▀\n░░░█░░░░░░░░░░░████▀\n░░░▀▄▄▀▀▄▄▀▀▄▄▄█▀\n')
        
@client.on_message(filters.command("love", prefixes=".") & filters.me)
def betaloves(_, msg):

	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍 
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍🧡🧡🤍🧡🧡🤍🤍
	🤍🧡🧡🧡🧡🧡🧡🧡🤍
	🤍🧡🧡🧡🧡🧡🧡🧡🤍 
	🤍🧡🧡🧡🧡🧡🧡🧡🤍
	🤍🤍🧡🧡🧡🧡🧡🤍🤍
	🤍🤍🤍🧡🧡🧡🤍🤍🤍
	🤍🤍🤍🤍🧡🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💛💛🤍💛💛🤍🤍
	🤍💛💛💛💛💛💛💛🤍
	🤍💛💛💛💛💛💛💛🤍
	🤍💛💛💛💛💛💛💛🤍
	🤍🤍💛💛💛💛💛🤍🤍
	🤍🤍🤍💛💛💛🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚💚🤍💚💚🤍🤍
	🤍💚💚💚💚💚💚💚🤍
	🤍💚💚💚💚💚💚💚🤍
	🤍💚💚💚💚💚💚💚🤍
	🤍🤍💚💚💚💚💚🤍🤍
	🤍🤍🤍💚💚💚🤍🤍🤍
	🤍🤍🤍🤍💚🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💙💙🤍💙💙🤍🤍
	🤍💙💙💙💙💙💙💙🤍
	🤍💙💙💙💙💙💙💙🤍
	🤍💙💙💙💙💙💙💙🤍
	🤍🤍💙💙💙💙💙🤍🤍
	🤍🤍🤍💙💙💙🤍🤍🤍
	🤍🤍🤍🤍💙🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💜💜🤍💜💜🤍🤍
	🤍💜💜💜💜💜💜💜🤍
	🤍💜💜💜💜💜💜💜🤍
	🤍💜💜💜💜💜💜💜🤍
	🤍🤍💜💜💜💜💜🤍🤍
	🤍🤍🤍💜💜💜🤍🤍🤍
	🤍🤍🤍🤍💜🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚🧡🤍💛🧡🤍🤍
	🤍🧡🧡💜🧡💚💙💛🤍
	🤍💛💚💙💚💜💚💜🤍
	🤍💙💛💜🧡🧡💚💛🤍
	🤍🤍🧡💚🧡💚💙🤍🤍
	🤍🤍🤍💜💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚🧡🤍❤️🧡🤍🤍
	🤍💙❤️💜❤️💚💙💛🤍
	🤍💛💚💙💚💜💚❤️🤍
	🤍💙❤️💜❤️💙💚💙🤍
	🤍🤍🧡💚🧡❤️💙🤍🤍
	🤍🤍🤍❤️💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💛❤️🤍💛💛🤍🤍
	🤍💙❤️💜💛❤️💙💛🤍
	🤍❤️💚❤️💚💜💚❤️🤍
	🤍💙❤️💜❤️❤️💚💙🤍
	🤍🤍💛💚🧡💛❤️🤍🤍
	🤍🤍🤍❤️💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚🧡🤍💛🧡🤍🤍
	🤍🧡🧡💜🧡💚💙💛🤍
	🤍💛💚💙💚💜💚💜🤍
	🤍💙💛💜🧡🧡💚💛🤍
	🤍🤍🧡💚🧡💚💙🤍🤍
	🤍🤍🤍💜💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💚🧡🤍❤️🧡🤍🤍
	🤍💙❤️💜❤️💚💙💛🤍
	🤍💛💚💙💚💜💚❤️🤍
	🤍💙❤️💜❤️💙💚💙🤍
	🤍🤍🧡💚🧡❤️💙🤍🤍
	🤍🤍🤍❤️💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍💛❤️🤍💛💛🤍🤍
	🤍💙❤️💜💛❤️💙💛🤍
	🤍❤️💚❤️💚💜💚❤️🤍
	🤍💙❤️💜❤️❤️💚💙🤍
	🤍🤍💛💚🧡💛❤️🤍🤍
	🤍🤍🤍❤️💛💜🤍🤍🤍
	🤍🤍🤍🤍💛🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	🤍🤍🤍🤍🤍🤍🤍🤍🤍
	🤍🤍❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️🤍🤍🤍🤍🤍🤍
	🤍🤍❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️🤍🤍
	🤍🤍❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️🤍❤️❤️🤍🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️🤍
	🤍❤️❤️❤️❤️❤️❤️❤️🤍
	🤍🤍❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️🤍🤍
	🤍🤍🤍❤️❤️❤️🤍🤍🤍
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	🤍🤍🤍🤍❤️🤍🤍🤍🤍
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	🤍🤍🤍🤍🤍🤍🤍🤍🤍''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️
	❤️❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️❤️
	❤️❤️❤️❤️
	❤️❤️❤️❤️
	❤️❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️❤️
	❤️❤️❤️
	❤️❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️❤️
	❤️❤️''')
	sleep(0.6) 
	msg.edit(f'''
	❤️''')



# Команда police
@client.on_message(
    filters.command(["police", "полиция"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id, message.id, "🟦🟦🟦⬜️⬜️⬜️🟥🟥🟥🟦🟦🟦⬜️⬜️⬜️🟥🟥🟥🟦🟦🟦⬜️⬜️⬜️🟥🟥🟥"
    )
    client.edit_message_text(
        message.chat.id, message.id, "🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦"
    )
    sleep(1 / 2)
    client.edit_message_text(
        message.chat.id, message.id, "🟦🟦🟦⬜️⬜️⬜️🟥🟥🟥🟦🟦🟦⬜️⬜️⬜️🟥🟥🟥🟦🟦🟦⬜️⬜️⬜️🟥🟥🟥"
    )
    sleep(1 / 2)
    client.edit_message_text(
        message.chat.id, message.id, "🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦"
    )
    sleep(1 / 2)
    client.edit_message_text(
        message.chat.id, message.id, "🟦🟦🟦⬜️⬜️⬜️🟥🟥🟥\n🟦 🟦🟦⬜️⬜️⬜️🟥🟥🟥\n🟦🟦🟦⬜️⬜️⬜️🟥🟥🟥"
    )
    sleep(1 / 2)
    client.edit_message_text(
        message.chat.id, message.id, "🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦🟥🟥🟥⬜️⬜️⬜️🟦🟦🟦"
    )
   
@client.on_message(
    filters.command(["help"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,
        "~Все команды через точку\ntagi тяги\nspasibo спасибо спасибо\nptichki птички летят бомбить поросят\ntyanka ня\ncopibara капибара\nskala🤨\nmemefaceмеме\ntrollfece хех\nhelpall полносьтю весь хелп\nhelp это меню\npolice анимация мегалок \n👎диз/👍 лайк\nr реакция\nspam [число спама] [текст] спам\nworld анимация\ncloud анимация\nclock анимация\nmoon анимация\nmoon2 анимация\nlove анимация\ntype [текст] анимация\nmezalov ААААА ОСУЖДАЮ\nhttps://t.me/amongusimostorsus\nsus sus\nhi привет\npoka пока\nhack взлом пентанона\ntext [текст] анимация\ntry попытка не пытка\npizza пица\nuno уно\npikachu пикачу\nvor песьня\nsecrt до обновление можно было получить обнову\ncreators\npin\nunpin\nunpinall\nxleb\nzaika\nvzlom\ndr\ngifts\nvideo\ngachi\nbank\nkill\nfootball\space\nbogdan\nstop\npong\nhackpc\nvopros\b",
    ) 
    
@client.on_message(filters.command(["brain", "b"], prefixes="."))
def brain(client, msg):
	msg.edit("Твой мозг \n🗑          🧠🏃🏻")
	msg.edit("Твой мозг \n🗑         🧠🏃🏻")
	msg.edit("Твой мозг \n🗑        🧠🏃🏻")
	msg.edit("Твой мозг \n🗑       🧠🏃🏻")
	msg.edit("Твой мозг \n🗑      🧠🏃🏻")
	msg.edit("Твой мозг \n🗑     🧠🏃🏻")
	msg.edit("Твой мозг \n🗑    🧠🏃🏻")
	msg.edit("Твой мозг \n🗑   🧠🏃🏻")
	msg.edit("Твой мозг \n🗑 🧠🏃🏻")
	msg.edit("Твой мозг в мусорке \n🗑 🙍🏼‍♂️")

	sleep(5)
	global number
	number = number + 1

@client.on_message(filters.command("vopros", prefixes=".") & filters.me)
def betaloves(_, msg):
	time = 0.4
	for i in range(1):
		sleep(0.001)
		msg.edit(f'''      
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦''')  # red
		sleep(0.001)
		msg.edit(f'''      
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦''')  # red
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦''')
		sleep(0.001)
		msg.edit(f'''   
🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛️⬛️⬛️🟦🟦
🟦⬛️🟦🟦🟦⬛️🟦
🟦🟦🟦🟦⬛️🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦⬛️🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦
''')
	sleep(5)
	global number
	number = number + 1
	

    
@client.on_message(filters.command("bogdan", prefixes=".") & filters.me)
def betaloves(_, msg):
	kakish1 = 0
	kakish = random.randint(1, 25)

	msg.edit(f'''
	Богдан начел искать какиш.''')
	sleep(0.7)
	msg.edit(f'''
	Богдан начел искать какиш..''')
	sleep(0.7)
	msg.edit(f'''
	Богдан начел искать какиш...''')
	sleep(0.7)
	while kakish1 <= 99:
		sleep(0.1)
		kakish1 += 1
		msg.edit(f'''
		Поиск какиша выполнен на {kakish1}%''')
	if kakish1 >= 99:
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл.''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл..''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл...''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл.''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл..''')
		sleep(0.7)
		msg.edit(f'''
		Богдан считает сколько какиша он нашёл...''')
		sleep(1)
		msg.edit(f'''
		Богдан нашел {kakish} кг какиша!''')


	sleep(5)
	global number
	number = number + 1
    
@client.on_message(filters.command("vzlom", prefixes=".") & filters.me)
async def valentine(_, msg):
	vzlom = 0

	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся.''')
	sleep(1)
	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся..''')
	sleep(1)
	await msg.edit(f'''
		💾 Взлом аккаунта скоро начнётся...''')
	sleep(1)

	while vzlom < 100:
		await msg.edit(f'''
			❗ Происходит взлом аккаунта... {vzlom}%''')
		vzlom += 1
	if vzlom >= 100:
		await msg.edit(f'''
			✅ Взлом акканута успешно завершен!''')
		sleep(0.5)
		await msg.edit(f'''
			📲 Передача данных в базу данных.''')
		sleep(0.5)
		await msg.edit(f'''
			📱 Передача данных в базу данных..''')
		sleep(0.5)
		await msg.edit(f'''
			📲 Передача данных в базу данных...''')
		sleep(0.5)
		await msg.edit(f'''
			✅ Аккаунт успешно взломан!''')
		sleep(0.5)
		sleep(5)
		await msg.delete()
	global number
	number = number + 1
	
@client.on_message(filters.command("vzlomip", prefixes=".") & filters.me)
async def valentine(_, msg):
	vzlomip = 0

	await msg.edit(f'''
		💾 Поиск айпи начался.''')
	sleep(1)
	await msg.edit(f'''
		💾 Поиск айпи начался..''')
	sleep(1)
	await msg.edit(f'''
		💾 Поиск айпи начался...''')
	sleep(1)
	
	client.send_sticker(msg.chat.id, "CAACAgIAAxkBAAEEPJ1iOeGaHrwudfx0VAkPdzcJV7rSsAACLBYAAqlr0EsgtENNn-yMxyME")

	while vzlomip < 100:
		await msg.edit(f'''
			❗ Происходит поиск IP... {vzlomip}%''')
		vzlomip += 1
	if vzlomip >= 100:
		await msg.edit(f'''
			✅ IP-адрес успешно найдён!''')
		sleep(5)
		await msg.delete()
	global number
	number = number + 1
    
@client.on_message(
    filters.command(["creators"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,     "дискорд сервер https://discord.gg/cZSzNeRH\nтелеграм канал https://t.me/amongusimostorsus",
    )
    
@client.on_message(
    filters.command(["vor"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,     "ты🤑ведь😏знаешь😎что😘субботу🥵вор👿ни🙄ходит😫на🥶работу🥳а🤓у😉нас🧢суббота🤗каждый😤день😡",
    )

@client.on_message(filters.command("1000-7", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(
            f"""      
1000 - 7 = 993 
993 - 7 = 986 
986 - 7 = 979 
979 - 7 = 972 
972 - 7 = 965 
965 - 7 = 958 
958 - 7 = 951 
951 - 7 = 944 
944 - 7 = 937 
937 - 7 = 930 
930 - 7 = 923 
923 - 7 = 916 
916 - 7 = 909 
909 - 7 = 902 
902 - 7 = 895 
895 - 7 = 888 
888 - 7 = 881 
881 - 7 = 874 
874 - 7 = 867 
867 - 7 = 860 
860 - 7 = 853 
853 - 7 = 846 
846 - 7 = 839 
839 - 7 = 832 
832 - 7 = 825 
825 - 7 = 818 
818 - 7 = 811 
811 - 7 = 804 
804 - 7 = 797 
797 - 7 = 790 
790 - 7 = 783 
783 - 7 = 776 
776 - 7 = 769 
769 - 7 = 762 
762 - 7 = 755 
755 - 7 = 748 
748 - 7 = 741 
741 - 7 = 734 
734 - 7 = 727 
727 - 7 = 720 
720 - 7 = 713 
713 - 7 = 706 
706 - 7 = 699 
699 - 7 = 692
692 - 7 = 685 
685 - 7 = 678 
678 - 7 = 671 
671 - 7 = 664 
664 - 7 = 657 
657 - 7 = 650 
650 - 7 = 643 
643 - 7 = 636 
636 - 7 = 629 
629 - 7 = 622 
622 - 7 = 615 
615 - 7 = 608 
608 - 7 = 601 
601 - 7 = 594 
594 - 7 = 587 
587 - 7 = 580 
580 - 7 = 573 
573 - 7 = 566 
566 - 7 = 559 
559 - 7 = 552 
552 - 7 = 545 
545 - 7 = 538 
538 - 7 = 531 
531 - 7 = 524 
524 - 7 = 517 
517 - 7 = 510 
510 - 7 = 503 
503 - 7 = 496 
496 - 7 = 489 
489 - 7 = 482 
482 - 7 = 475 
475 - 7 = 468 
468 - 7 = 461 
461 - 7 = 454 
454 - 7 = 447 
447 - 7 = 440 
440 - 7 = 433 
433 - 7 = 426 
426 - 7 = 419 
419 - 7 = 412 
412 - 7 = 405 
405 - 7 = 398 
398 - 7 = 391 
391 - 7 = 384 
384 - 7 = 377 
377 - 7 = 370 
370 - 7 = 363 
363 - 7 = 356 
356 - 7 = 349 
349 - 7 = 342 
342 - 7 = 335 
335 - 7 = 328 
328 - 7 = 321 
321 - 7 = 314 
314 - 7 = 307 
307 - 7 = 300 
300 - 7 = 293 
293 - 7 = 286 
286 - 7 = 279 
279 - 7 = 272 
272 - 7 = 265 
265 - 7 = 258 
258 - 7 = 251 
251 - 7 = 244 
244 - 7 = 237 
237 - 7 = 230 
230 - 7 = 223 
223 - 7 = 216 
216 - 7 = 209 
209 - 7 = 202 
202 - 7 = 195 
195 - 7 = 188 
188 - 7 = 181 
181 - 7 = 174 
174 - 7 = 167 
167 - 7 = 160 
160 - 7 = 153 
153 - 7 = 146 
146 - 7 = 139 
139 - 7 = 132 
132 - 7 = 125 
125 - 7 = 118 
118 - 7 = 111 
111 - 7 = 104 
104 - 7 = 97 
97 - 7 = 90 
90 - 7 = 83 
83 - 7 = 76 
76 - 7 = 69 
69 - 7 = 62 
62 - 7 = 55 
55 - 7 = 48 
48 - 7 = 41 
41 - 7 = 34 
34 - 7 = 27 
27 - 7 = 20 
20 - 7 = 13 
13 - 7 = 6 
6 - 7 = -1"""
        )  # red

@client.on_message(filters.command('pin', prefixes='.') & filters.me)
async def pin(client, msg):
	try:
		await client.pin_chat_message(chat_id=msg.chat.id, message_id=msg.reply_to_message_id)
		await msg.delete()
	except Exception as e:
		await msg.edit('Произошла ошибка!\nОшибка есть в консоли.\n\nВозможно ваше сообщение не было ответом на другое сообщение, или у вас недостаточно прав')
		print(e)
		sleep(2)
		await msg.delete()

@client.on_message(filters.command('unpin', prefixes='.') & filters.me)
async def unpin(client, msg):
	try:
		await client.unpin_chat_message(chat_id=msg.chat.id, message_id=msg.reply_to_message_id)
		await msg.delete()
	except Exception as e:
		await msg.edit('Произошла ошибка!\nОшибка есть в консоли.\n\nВозможно ваше сообщение не было ответом на другое сообщение, или у вас недостаточно прав')
		print(e)
		sleep(2)
		await msg.delete()

@client.on_message(filters.command('unallpin', prefixes='.') & filters.me)
async def unpin(client, msg):
	try:
		await client.unpin_all_chat_messages(chat_id=msg.chat.id)
		await msg.delete()
	except Exception as e:
		await msg.edit('Произошла ошибка!\nОшибка есть в консоли.\n\nВозможно ваше сообщение не было ответом на другое сообщение, или у вас недостаточно прав')
		print(e)
		sleep(2)
		await msg.delete()

@client.on_message(filters.command("👍", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(
            f"""      
🟦"""
        )  # red
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦"""
        )  # red
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦"""
        )
        sleep(5)
        global number
        number = number + 1


@client.on_message(filters.command("👎", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(
            f"""
🟥"""
        )  # red
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥"""
        )  # red
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥"""
        )
        sleep(0.001)
        msg.edit(
            f"""
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥"""
        )


@client.on_message(filters.command("mezalov", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(
            f"""      
А"""
        )  # red
        sleep(0.001)
        msg.edit(
            f"""
АА"""
        )  # red
        sleep(0.001)
        msg.edit(
            f"""
ААА"""
        )
        sleep(0.001)
        msg.edit(
            f"""
АААА"""
        )
        sleep(0.001)
        msg.edit(
            f"""
ААААА"""
        )
        sleep(0.001)
        msg.edit(
            f"""
АААААА"""
        )
        sleep(0.001)
        msg.edit(
            f"""
АААААА О"""
        )
        sleep(0.001)
        msg.edit(
            f"""
АААААА ОС"""
        )
        sleep(0.001)
        msg.edit(
            f"""
АААААА ОСУ"""
        )
        sleep(0.001)
        msg.edit(
            f"""
ААААААА ОСУЖ"""
        )
        sleep(0.001)
        msg.edit(
            f"""
ААААААА ОСУЖД"""
        )
        sleep(0.001)
        msg.edit(
            f"""
ААААААА ОСУЖДА"""
        )
        sleep(0.001)
        msg.edit(
            f"""
ААААААА ОСУЖДАЮ"""
        )
        sleep(0.001)


@client.on_message(filters.command(["sus"], prefixes=[".", "!", "/", "-"]) & filters.me)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,
        "susඞ",
    )


@client.on_message(filters.command(["hi"], prefixes=[".", "!", "/", "-"]) & filters.me)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,
        "привет пупсик",
    )

@client.on_message(filters.command(["poka"], prefixes=[".", "!", "/", "-"]) & filters.me)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,
        "до встречи",
    )
    
@client.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
            
            msg.edit("взлом твоего аккаунта ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "взлом твоего аккаунта ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

@client.on_message(
    filters.command(["cloun"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,
        "клоун: @Andreyvareni",
    )
    
@client.on_message(
    filters.command(["secret2"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,
        "поздравляю ты нашел сикретку напиши @NazarZaZ3999",
    )

@client.on_message(
    filters.command(["secret"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,
        "поздравляю ты нашел сикретку",
    )
    

@client.on_message(filters.command("text", prefixes=".") & filters.me)
def betaloves(_, msg):
	text1 = " ".join(msg.command[1:])

	if not text1:
		msg.edit(f'''
			**Error: Вы не ввели текст!\nИспользование: .text <текст>**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{text1}ㅤㅤㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤ{text1}ㅤㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤ{text1}ㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤ{text1}ㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤㅤ{text1}ㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤㅤㅤ{text1}''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤㅤ{text1}ㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤㅤ{text1}ㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤㅤ{text1}ㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			ㅤ{text1}ㅤㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			{text1}ㅤㅤㅤㅤㅤ''')
		sleep(0.5)
		msg.edit(f'''
			{text1}''')
			
@client.on_message(filters.command('', prefixes='.') & filters.me)
async def valentine(client, msg):
	global number
	number = number + 1 
	try:
		await msg.edit('''
			❤ А у кого это сегодня день рождение? ❤''')
		sleep(1)
		await msg.edit('''
			💜 Да вот же! Ааа 💜''')
		sleep(1)
		await msg.edit('''
			❤ С днём рождения! Симпатулька ❤''')
		sleep(1)
		await msg.edit('''
			🧡 С днём рождения! Бусинка моя 🧡''')
		sleep(1)
		await msg.edit('''
			💛 Пусть невезуха, и безнадега 💛''')
		sleep(1)
		await msg.edit('''
			💚 Всегда стороною обходят тебя 💚''')
		sleep(1)
		await msg.edit('''
			💙 С днём рождения! 💙''')
		sleep(1)
		await msg.edit('''
			❤ С днём рождения! ❤''')
		sleep(1)
		await msg.edit('''
			💚 С днём рождения! 💚''')
		sleep(1)
		await msg.edit('''
			🧡 С днём рождения! 🧡''')
		sleep(1)
	except Exception as e:
		print(f"Error: {e}")
			
@client.on_message(
    filters.command(["tagi"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,     "блять🤑что😏за😎тяги😘такие🥵бархатные👿тяги🙄ребятка😫уфф🥶кэфтэмэ🥳я🤓твою😉цицьку🧢царапал🤗кэфтэмэ😤мэ-мэ😡",
    )
    
@client.on_message(
    filters.command(["ptichki"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,     "птички летят бомбить поросят они взрывают им домики домики\nзапрети мне бомбить поросят птички литят бомбить поросят они взрывают им домики домики\n заприти мне ходить https://t.me/zapritimnexodoti/3",
    )
		
@client.on_message(filters.command('r', prefixes='.') & filters.me)
async def unpin(client, msg):
	emoji = ' '.join(msg.command[1:])
	try:
		await client.send_reaction(chat_id=msg.chat.id, message_id=msg.reply_to_message_id, emoji=emoji)
		await msg.delete()
	except Exception as e:
		await msg.edit('ERORR')
			
@client.on_message(
    filters.command(["spasibo"], prefixes=[".", "!", "/", "-"]) & filters.me
)
def message_handler(client, message):
    client.edit_message_text(
        message.chat.id,
        message.id,     "спасибо спасибо спасибо СПАСИБО",
    )  
    
  
@client.on_message(filters.command(['Ahegao', 'tyanka'], prefixes=['.','!','/', '-']) & filters.me)
def betaloves(_, msg):
 time = 0.6
 for i in range(1):
  msg.edit(f'''      
⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄
⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤
⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄
⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿''')  # red
  sleep(0.001)
  msg.edit(f'''
⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄
⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤
⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄
⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿
⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿ ⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛
⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄
⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄..''')  # red
  sleep(0.001)
  
@client.on_message(filters.command("copybara", prefixes=".") & filters.me)
def betaloves(_, msg):
 time = 0.6
 for i in range(1):
  msg.edit(f'''⠀⠀⢀⣀⠤⠿⢤⢖⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡔⢩⠂⠀⠒⠗⠈⠀⠉⠢⠄⣀⠠⠤⠄⠒⢖⡒⢒⠂⠤⢄⠀⠀⠀⠀
⠇⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠀⠈⠈⡨⢀⠡⡪⠢⡀⠀
⠈⠒⠀⠤⠤⣄⡆⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠀⢕⠱⠀
⠀⠀⠀⠀⠀⠈⢳⣐⡐⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠇''')
  sleep(0.001)
  msg.edit(f'''⠀⠀⢀⣀⠤⠿⢤⢖⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡔⢩⠂⠀⠒⠗⠈⠀⠉⠢⠄⣀⠠⠤⠄⠒⢖⡒⢒⠂⠤⢄⠀⠀⠀⠀
⠇⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠀⠈⠈⡨⢀⠡⡪⠢⡀⠀
⠈⠒⠀⠤⠤⣄⡆⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠀⢕⠱⠀
⠀⠀⠀⠀⠀⠈⢳⣐⡐⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠇
⠀⠀⠀⠀⠀⠀⠀⠑⢤⢁⠀⠆⠀⠀⠀⠀⠀⢀⢰⠀⠀⠀⡀⢄⡜⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡦⠄⡷⠢⠤⠤⠤⠤⢬⢈⡇⢠⣈⣰⠎⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣃⢸⡇⠀⠀⠀⠀⠀⠈⢪⢀⣺⡅⢈⠆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠶⡿⠤⠚⠁⠀⠀⠀⢀⣠⡤⢺⣥⠟⢡⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀''')
  sleep(5)
  global number
  number = number + 1
  
@client.on_message(filters.command(['StupidFace', 'memeface'], prefixes=['.','!','/', '-']) & filters.me)
def betaloves(_, msg):
 time = 0.6
 for i in range(1):
  msg.edit(f'''      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠈⠉⠉⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀
⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠋⢙⣦⡈⣷⡄⠀⠀⠀
⠀⣀⠶⠁⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠿⢿⡟⣌⢿⠀⠀⠀
⣠⡿⠀⢠⣜⠉⠀⠀⠙⢷⢄⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠘⡆⢧⡀⠀
⣯⠃⠀⢾⣿⠗⠀⠀⠀⠀⡽⠀⠀⠀⠈⠳⢄⣀⠀⠀⠀⡰⠃⠘⣵⡄
⡏⠀⠀⠘⡄⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⢱⡇
⡅⠀⠀⠀⠙⠒⠔⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇''')  # red
 sleep(0.001)
 msg.edit(f'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠈⠉⠉⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀
⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠋⢙⣦⡈⣷⡄⠀⠀⠀
⠀⣀⠶⠁⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠿⢿⡟⣌⢿⠀⠀⠀
⣠⡿⠀⢠⣜⠉⠀⠀⠙⢷⢄⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠘⡆⢧⡀⠀
⣯⠃⠀⢾⣿⠗⠀⠀⠀⠀⡽⠀⠀⠀⠈⠳⢄⣀⠀⠀⠀⡰⠃⠘⣵⡄
⡏⠀⠀⠘⡄⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⢱⡇
⡅⠀⠀⠀⠙⠒⠔⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⡗
⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣇
⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠷⣤⣤⣤⣤⠞⠁⠀⠀⠀⠀⠀⠀⣸
⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠇
⠀⠀⢇⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀
⠀⠀⠈⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')  # red
 sleep(0.001)
  
@client.on_message(filters.
command(['UWU', 'УВУ'], prefixes=['.','!','/', '-']) & filters.me)
def betaloves(_, msg):
 time = 0.6
 for i in range(1):
  msg.edit(f'''      
⣿⡇⠀⢸⣿
⣿⡇⠀⢸⣿
⢿⣧⣤⢾⣿''')  # red
  sleep(0.001)
  msg.edit(f'''
⣿⡇⠀⢸⣿⠀⢹⣷⠀⣸⣿⡄⢠⣿⠁
⣿⡇⠀⢸⣿⠀⠘⣿⣆⣿⢹⣷⣼⡇⠀
⢿⣧⣤⢾⣿⠀⠀⢸⣿⡇⠀⣿⡿⠀⠀''')  # red
  sleep(0.001)
  msg.edit(f'''
⣿⡇⠀⢸⣿⠀⢹⣷⠀⣸⣿⡄⢠⣿⠁⢸⣿⠀⠀⣿⡇
⣿⡇⠀⢸⣿⠀⠘⣿⣆⣿⢹⣷⣼⡇⠀⢸⣿⠀⠀⣿⡇
⢿⣧⣤⢾⣿⠀⠀⢸⣿⡇⠀⣿⡿⠀⠀⠸⣿⣤⡼⣿⡇''')
  sleep(5)
  
  
@client.on_message(filters.command(['skala',  'Dwayne'], prefixes=['.','!','/', '-']) & filters.me)
def betaloves(_, msg):
   time = 0.6
   for i in range(1):
    msg.edit(f'''      
⣿⣿⠿⠿⣿⠿⣿⠿⠿⠿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿ ⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿ ⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿ ⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿ ⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿ ⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿''')  # red
   sleep(0.001)
   msg.edit(f'''
⣿⣿⠿⠿⣿⠿⣿⠿⠿⠿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿ ⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿ ⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿ ⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿ ⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿ ⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿ ⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿ ⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿ ⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿ ⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿''')  # red
   sleep(5)
   global number
   number = number + 1
  
@client.on_message(filters.command(['Lovee', 'iloveu'], prefixes=['.','!','/', '-']) & filters.me)
def betaloves(_, msg):
 time = 0.6
 for i in range(1):
  msg.edit(f'''      
╔══╗....<3
╚╗╔╝..('\../')
╔╝╚╗..( •.• )
╚══╝..(,,)(,,)''')  # red
  sleep(0.001)
  msg.edit(f'''
╔══╗....<3
╚╗╔╝..('\../')
╔╝╚╗..( •.• )
╚══╝..(,,)(,,)
╔╗╔═╦╦╦═╗ ╔╗╔╗
║╚╣║║║║╩╣ ║╚╝║
╚═╩═╩═╩═╝ ╚══╝''')  # red
  sleep(0.001)
  
@client.on_message(filters.command(['Trollge', 'trollface'], prefixes=['.','!','/', '-']) & filters.me)
def betaloves(_, msg):
 time = 0.6
 for i in range(1):
  msg.edit(f'''      
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀       ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀       ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀       ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆          ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿     ''')  # red
  sleep(0.001)
  msg.edit(f'''
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀       ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀       ⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀       ⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆          ⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀       ⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀      ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀      ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁''')  # red
  sleep(0.001)

@client.on_message(filters.command('xleb', prefixes='.') & filters.me)
async def valentine(client, message):
	global number
	await message.edit('⠀👩‍🦰          👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰         👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰        👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰       👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰      👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰     👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰    👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰   👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰 👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰  ')
	sleep(0.1)
	await message.edit('⠀👩‍🦰💋👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰  ')
	sleep(0.1)
	await message.edit('⠀👩‍🦰  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰  ')
	sleep(0.1)
	await message.edit('⠀👩‍🦰  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👨‍🦰  ')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶 👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶   👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶    👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶     👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶      👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶       👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶        👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶         👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶')
	sleep(0.2)
	await message.edit('*спустя 5 лет*')
	sleep(3)
	await message.edit('⠀👩‍🦰👶         👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶        👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶       👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶      👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶     👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶    👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶   👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶  👨‍🦰🍞')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞 👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞  👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞   👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞    👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞     👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞      👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞       👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞        👨‍🦰')
	sleep(0.1)
	await message.edit('⠀👩‍🦰👶🍞')	
	
@client.on_message(filters.command("zaika", prefixes=".") & filters.me)
async def valentine(_ , msg):
	zaika = 0
	zaika2 = 0
	while zaika < 100:
		await msg.edit(f'''
			💖 Поиск зайки... {zaika}%''')
		zaika += 1
	if zaika >= 100:
		await msg.edit(f'''
			✅ Зайка успешно найдена!''')
		sleep(1)
		while zaika2 < 100:
			await msg.edit(f'''
				🤔 Подбираю слова что-бы описать тебя... {zaika2}%''')
			zaika2 += 1
		if zaika2 >= 100:
			await msg.edit(f'''
				❤ Ты самый лучший человек которого я видел!''')
			sleep(5)
	number = number + 1
	
@client.on_message(filters.command("dr", prefixes=".") & filters.me)
def valentine(_, msg):
	msg.edit(f'С днём рождения! Желаю тебе...')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	👑 чтобы вся жизнь была полна радости
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	☀️ счастья
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🏋️‍♂️ здоровья
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🌈 улыбок
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	💚 любви
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🔥 приятных сюрпризов
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🥇 Высоких достижений
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🍃 Душевной гармонии
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🌹 Процветания
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	📈 Карьерного роста
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🤝 Хороших друзей
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	💪 Больше силы, чувств, смелости
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🎲 Везения, мира, добра
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🌃 Чтобы сбывались даже самые необычные желания
	''')
	sleep(0.8)
	client.send_message(msg.chat.id, f'''
	🎇 И чтобы каждое начатое дело заканчивалось успешно!
	''')
	
@client.on_message(filters.command("gul2", prefixes=".") & filters.me)
def valentine(client, message):
	global number
	client.send_message(message.chat.id,f'<b>Ты гуль?</b>')
	sleep(2)
	client.send_message(message.chat.id,f'<i>Я тоже</i>')
	sleep(5)
	i = 1000
	while i > 0:
		try:
			client.send_message(message.chat.id, f'{i} - 7 = {i-7}')
		except FloodWait as e:
			sleep(e.x)

		i -= 7
		sleep(0)

	if(end_message != ''):
		client.send_message(message.chat.id, end_message)

@client.on_message(filters.command("mems", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_message(msg.chat.id, f'''
	✨ Меню голосовых мемов:
	(Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
		
	 1) Команда: ".сукаблядьнахуй"
	 2) Команда: ".блядьуходиотсюда"
	 3) Команда: ".татышоахуэл"
	 4) Команда: ".блядьнахуй"
	 5) Команда: ".щясзарежу"
	 6) Команда: ".гдетыблядь"
	 7) Команда: ".даунобосаный"
	 8) Команда: ".ктокуда"
	 9) Команда: ".уменяестьплан"
	 10) Команда: ".ятрахнутебя"

	
	(Все команды нужно писать без ковычек)
	.
		''')
	global number
	number = number + 1

@client.on_message(filters.command("сукаблядьнахуй", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems/syka-blyad-nahyi.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("блядьуходиотсюда", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems/blyat-vixodi-otsyda.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("татышоахуэл", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems/ta-ti-sho-oxyel.mp3")

@client.on_message(filters.command("блядьнахуй", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems/nahui-blyat.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("щясзарежу", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems/schas-zareju.mp3")
	global number
	number = number + 1
	
@client.on_message(filters.command("gifts", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_message(msg.chat.id, f'''
	✨ Меню gif мемов:
	(Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
		
	 1) Команда: ".понимания"
	 2) Команда: ".клоун"
	 3) Команда: ".ктопинганул"
	 4) Команда: ".ладно"
	 5) Команда: ".nosex"
	 6) Команда: ".переделывай"
	 7) Команда: ".пизда"
	 8) Команда: ".пошёлнахуй"
	 9) Команда: ".спокойнойночи"
	 10) Команда: ".хуйстобой"
	 11) Команда: ".сверхукринж"
	 12) Команда: ".разговор"
	 13) Команда: ".всемпохуй"

	
	(Все команды нужно писать без ковычек)
		''')

@client.on_message(filters.command("гдетыблядь", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems/gde-tyi.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("даунобосаный", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems//daun-obosannyii-mat-tvoyu-v-kanavu-kidal.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("ктокуда", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems//kto-kuda-a-ya-po-delam.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("уменяестьплан", prefixes=".") & filters.me)
def sykatest(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems//u-menya-est-takoi-plan.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("ятрахнутебя", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "mems//ya-traxny-tebya.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("gachi", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_message(msg.chat.id, f'''
	💪 Меню голосовых **GACHY** мемов:
	(Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
		
	 1) Команда: ".300"
	 2) Команда: ".woo"
	 3) Команда: ".fuckyou"
	 4) Команда: ".dungeonmaster"
	 5) Команда: ".spank"
	 6) Команда: ".iamsorry"
	 7) Команда: ".ass"
	 8) Команда: ".boynextdoor"
	 9) Команда: ".letsgo"
	
	(Все команды нужно писать без ковычек)
	.
	''')
	global number
	number = number + 1

@client.on_message(filters.command("300", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/fisting-is-300-.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("woo", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/woo.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("fuckyou", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/fuck-you1.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("dungeonmaster", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/dungeon-master.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("spank", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/spank.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("iamsorry", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/oh-shit-iam-sorry.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("ass", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/stick-your-finger-in-my-ass.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("boynextdoor", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/boy-next-door.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("letsgo", prefixes=".") & filters.me)
def gachi(client, msg):
	msg.delete()
	client.send_voice(msg.chat.id, "gachi/come-on-lets-go.mp3")
	global number
	number = number + 1

@client.on_message(filters.command("video", prefixes=".") & filters.me)
def video(client, msg):
	msg.delete()
	client.send_message(msg.chat.id, f'''
	🎞 Меню видео-мемов:
	(Примичание: Они могут подгружатся дольше чем надо, смотря какая скорость у интернета.)
		
	 1) Команда: ".диско"
	 2) Команда: ".ебаныйврот"
	 3) Команда: ".фортилипабаджи"
	 4) Команда: ".мамескажи"
	 5) Команда: ".мнепоебать"
	 6) Команда: ".сасать"
	 7) Команда: ".чтоэтотакое"
	 8) Команда: ".твояматьш"
	 9) Команда: ".япопулярный"
	 10) Команда: ".тыпиздабол"
	 11) Команда: ".хватитдрочить"
	
	(Все команды нужно писать без ковычек)
	.
	''')
	global number
	number = number + 1

@client.on_message(filters.command("диско", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/discko.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("ебаныйврот", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/ebaniy-v-rot.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("фортилипабаджи", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/fortnite-ili-pubg.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("мамескажи", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/mame-ckaji.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("мнепоебать", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/mne-poebat.MP4")
	global number
	number = number + 1

@client.on_message(filters.command("сасать", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/sasatb.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("чтоэтотакое", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/sho-eto-takoe.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("твояматьш", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/tvoya-matb-sh.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("япопулярный", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/ya-popylarniy.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("тыпиздабол", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/syda-po-formyle.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("хватитдрочить", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_video(msg.chat.id, "video/xvatit-drochit.mp4")
	global number
	number = number + 1

@client.on_message(filters.command("всемпохуй", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/vsem-poxui.gif")
	global number
	number = number + 1

@client.on_message(filters.command("разговор", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/razgovor.gif")
	global number
	number = number + 1

@client.on_message(filters.command("понимания", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/100ponimania-0osyjdenia.gif")
	global number
	number = number + 1

@client.on_message(filters.command("клоун", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/kloyn.gif")
	global number
	number = number + 1

@client.on_message(filters.command("ктопинганул", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/kto-pinganyl.gif")
	global number
	number = number + 1

@client.on_message(filters.command("ладно", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/ladno.gif")
	global number
	number = number + 1

@client.on_message(filters.command("nosex", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/no-sex.gif")
	global number
	number = number + 1

@client.on_message(filters.command("переделывай", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/peredelivai.gif")
	global number
	number = number + 1

@client.on_message(filters.command("пизда", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/pizda.gif")
	global number
	number = number + 1

@client.on_message(filters.command("пошёлнахуй", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/poshel-naxui.gif")
	global number
	number = number + 1

@client.on_message(filters.command("спокойнойночи", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/spokoinoi-nochi.gif")
	global number
	number = number + 1

@client.on_message(filters.command("хуйстобой", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/xui-s-toboi.gif")
	global number
	number = number + 1

@client.on_message(filters.command("сверхукринж", prefixes=".") & filters.me)
def mems(client, msg):
	msg.delete()
	client.send_animation(msg.chat.id, "gifs/sverxy-kringe.gif")
	global number
	number = number + 1
	
@client.on_message(filters.command("bank", prefixes=".") & filters.me)
def betaloves(_, msg):
	bank = 0
	bank1 = random.randint(1, 3000)

	msg.edit(f'''
	Идёт взлом банковской карты.''')
	sleep(0.7)
	msg.edit(f'''
	Идёт взлом банковской карты..''')
	sleep(0.7)
	msg.edit(f'''
	Идёт взлом банковской карты...''')
	sleep(0.7)
	msg.edit(f'''
	Получение данных.''')
	sleep(0.7)
	msg.edit(f'''
	Получение данных..''')
	sleep(0.7)
	msg.edit(f'''
	Получение данных...''')
	sleep(0.7)
	while bank <= 99:
		bank += 1
		msg.edit(f'''
		взлом завершён на {bank}%''')
	if bank >= 99:
		msg.edit(f'''
		Взлом банковской карты успешно завершён!\nСо счёта снято {bank1} руб.''')
		
	sleep(5)
	global number
	number = number + 1
	
@client.on_message(filters.command("football", prefixes=".") & filters.me)
def betalove(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f"<b>⚽️ Вы зашли на футбольное поле, вам предстоит забить пенальти, чтобы победить</b>")  # red
		sleep(2)
		msg.edit(f"<b>⏳ Подготовка к игре.</b>")  # orange
		sleep(2)
		msg.edit(f"<b>⌛ Подготовка к игре..</b>")  # orange
		sleep(time)
		msg.edit(f"<b>⏳ Подготовка к игре...</b>")  # red
		sleep(time)
		msg.edit(f"<b>⚽ Удар.</b>")  # orange
		sleep(time)
		msg.edit(f"<b>⚽ Удар..</b>")  # red
		sleep(time)
		msg.edit(f"<b>⚽ Удар...</b>")  # orange
		sleep(time)
		msg.edit(random.choice(foot))
		sleep(5)
		global number
		number = number + 1

foot = ["<b>❌ К сожалению, вы проиграли..</b>", "<b>✅ Вы забили гол и победили в игре!</b>"]

@client.on_message(filters.command("kill", prefixes=".") & filters.me)
def betalove(_, msg):
	time = 0.6
	for i in range(1):
		msg.edit(f"<b>🔪 На тебя заказали убийство.</b>")  # red
		sleep(3)
		msg.edit(f"<b>👀 У тебя есть пару секунд чтобы спрятаться.</b>")  # orange
		sleep(2)
		msg.edit(f"<b>⏳ [ 5s ]</b>")  # orange
		sleep(time)
		msg.edit(f"<b>⌛ [ 4s ]</b>")  # red
		sleep(time)
		msg.edit(f"<b>⏳ [ 3s ]</b>")  # orange
		sleep(time)
		msg.edit(f"<b>⌛ [ 2s ]</b>")  # red
		sleep(time)
		msg.edit(f"<b>⏳ [ 1s ]</b>")  # orange
		sleep(time)
		msg.edit(f"<b>🔪 Убийца вышел на твои поиски, надеюсь ты хорошо спрятался</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск.</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск..</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск...</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск.</b>")  # orange
		sleep(time)
		msg.edit(f"<b>👀 Поиск..</b>")
		sleep(time)
		msg.edit(f"<b>👀 Поиск...</b>")
		sleep(time)
		msg.edit(random.choice(kill))
		sleep(5)
		global number
		number = number + 1

kill = ["<b>🔪 Убийца нашел тебя, к сожалению ты спрятался плохо и был убит</b>", "<b>⚔️Убийца не нашел тебя, вы  очень хорошо спрятались.</b>"]

@client.on_message(filters.command("space", prefixes=".") & filters.me)
async def valentine(client, msg):
	await msg.edit(f'''
		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡''')
	sleep(0.5)
	await msg.edit(f'''
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ ''')
	sleep(0.5)
	await msg.edit(f'''
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡
		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ ''')
	sleep(0.5)
	await msg.edit(f'''
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ ''')
	sleep(0.5)
	await msg.edit(f'''
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ ''')
	sleep(0.5)
	await msg.edit(f'''
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ ''')
	sleep(0.5)
	await msg.edit(f'''
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * ''')
	sleep(0.5)
	await msg.edit(f'''
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ ''')
	sleep(0.5)
	await msg.edit(f'''
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ 
		☆∴｡　* ''')
	sleep(0.5)
	await msg.edit(f'''
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.
		･ ｡ ''')
	sleep(0.5)
	await msg.edit(f'''
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡

		.''')
	sleep(0.5)
	await msg.edit(f'''
		.
		･ ｡ 
		☆∴｡　* 
		　･ﾟ*｡★･ 
		　　･ *ﾟ｡　　 * 
		　 ･ ﾟ*｡･ﾟ★｡ 
		　　　☆ﾟ･｡°*. ﾟ 
		*　　ﾟ｡·*･｡ ﾟ* 
		　　　ﾟ *.｡☆｡★　･ 
		　　* ☆ ｡･ﾟ*.｡ 
			*　★ ﾟ･｡ * ｡ 
			･　　ﾟ☆ ｡''')
	sleep(5)
	await msg.delete()
	global number
	number = number + 1

@client.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(_, msg):
	random_number = str(random.randint(0, int(msg.command[1])))
	msg.edit(roi + random_number)



too = random.randint(0, 100)
roi = f'<b> Случайное число: </b>'

@client.on_message(filters.command("stop", prefixes=".") & filters.me)
def betaloves(_, msg):
	msg.edit('''
		<b>[!] Скрипт в стопе </b>''')
	sleep(1)
	print(Fore.RED + "Скрипт остоновлен командой\n")
	quit()
	
@client.on_message(filters.command("hackpc", prefixes=".") & filters.me)
def go(_, msg):
	perc = 0
	while(perc < 100):
		try:
			text = "👮‍ Взлом твоего ПК в процессе ... " + str(perc) + "%"
			msg.edit(text)
			perc += random.randint(1, 3)
			sleep(0.1)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("🟢 Ты успешно взломан!")
	sleep(3)
	msg.edit("😈 Поиск секретных данных ...")
	perc = 0
	while(perc < 100):
		try:
			text = "😈 Поиск секретных данных ... " + str(perc) + "%"
			msg.edit(text)
			perc += random.randint(1, 5)
			sleep(0.15)
		except FloodWait as e:
			sleep(e.x)
	msg.edit("🤑 Найдены важные данные!!!")

	sleep(5)
	global number
	number = number + 1

@client.on_message(filters.command("run", prefixes="."))
def run(client, msg):
	testr = 0
	while(testr < 50):
		try:
			text = "🏃"
			msg.edit(text)
			sleep(0.1)
			text = "🚶"
			msg.edit(text)
			sleep(0.1)
			testr += random.randint(1, 3)
		except FloodWait as e:
			sleep(e.x)

	msg.edit("добежал")

@client.on_message(filters.command("pong", prefixes="."))
def pong(client, msg):
	testr = 0
	while(testr < 5):
		try:
			text = "▐⠂       ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐⠈       ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐ ⠂      ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐ ⠠      ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐  ⡀     ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐  ⠠     ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐   ⠂    ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐   ⠈    ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐    ⠂   ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐    ⠠   ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐     ⡀  ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐     ⠠  ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐      ⠂ ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐      ⠈ ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐       ⠂▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐       ⠠▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐       ⡀▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐      ⠠ ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐      ⠂ ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐     ⠈  ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐     ⠂  ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐    ⠠   ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐    ⡀   ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐   ⠠    ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐   ⠂    ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐  ⠈     ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐  ⠂     ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐ ⠠      ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐ ⡀      ▌"
			msg.edit(text)
			sleep(0.1)
			text = "▐⠠       ▌"
			msg.edit(text)
			sleep(0.1)
			testr += random.randint(1, 3)
		except FloodWait as e:
			sleep(e.x)

	msg.edit("▐⠂⠂⠂⠂⠂⠂⠂⠂▌")

	sleep(5)
	global number
	number = number + 1

client.run()
