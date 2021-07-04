import telebot, re
from sql import SQLITE

bot = telebot.TeleBot('1806915175:AAHQ4q9MJGS7VPTdsVdyMvWECiBwlAaAX-s')
sql = SQLITE()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    mes = message.text
    try:
        result = re.findall(r'^\d+[\s]\w+[\s]\d\d:\d\d+', mes)
        result = re.split(r'[\s]', result[0])
        
        id = result[0]
        name = result[1]
        date = result[2]

        time = re.split(r'[:]', result[2])

        #if(int(time[0]) >= 0 and int(time[0]) <= 23 and int(time[1]) >= 0 and int(time[1]) <= 59):
        result = sql.addRecord(id, name, date, message.chat.id)
        print(result)
        return result
    except Exception as ex:
        print(str(ex))
        

    try:
        result = re.findall(r'^\w+[\s]\w+[\s]\d\d\*\d\d+[\s]\d+', mes)
        result = re.split(r'[\s]', result[0])
        id = result[0]
        name = result[1]
        money = result[2]
        time = result[3]
        result = sql.addReport(id, name, money, time, message.chat.id)
        print(result)
        return result
    except Exception as ex:
        print(str(ex)) 
    
    if mes == 'F75D20100840C0653AAA5F2BC4240F9C4A299FAB84837C4DABA3AF42ACF081A0':
        bot.send_message(message.chat.id, 'Enter group ID')
        bot.register_next_step_handler(message, get_records)

def get_records(message):
    try:
        chat_id = int(message.text)
        final = sql.getRecords(chat_id)
        print(final)
        return final
    except Exception as ex:
        print(str(ex))
        bot.send_message(message.chat.id, 'Wrong group ID')

bot.polling(none_stop=True, interval=0)
