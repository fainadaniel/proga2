from telebot import TeleBot
import random
bot = TeleBot('746049434:AAF_y6I35j56jWUqXzPxMh4UrzDKooe-ypE')


def f(x):
    return True


def accents(line):
    line = list(line)
    vowels = ["а", "у", "о", "и", "э", "я", "ю", "ё", "ы", "е"]
    cnt = 0
    for x in range(len(line)):
        if line[x] in vowels:
            cnt += 1
        if cnt % 2 == 0 and line[x] in vowels:
            line[x] = line[x].upper()
    line = ''.join(line)
    return(line)


@bot.message_handler(func=f)
def main(mes):
    put_in = mes.text.strip()
    given = put_in.split()[-1]
    given = ''.join(given.split('.'))
    given = ''.join(given.split(','))
    given = ''.join(given.split('-'))
    given = ''.join(given.split(':'))
    given = ''.join(given.split(';'))
    given = ''.join(given.split('"'))
    given = ''.join(given.split("'"))
    given = ''.join(given.split('!'))
    given = ''.join(given.split('?'))
    given = ''.join(given.split(')'))
    given = ''.join(given.split(']'))
    given = ''.join(given.split('>'))
    given = ''.join(given.split('}'))
    given = ''.join(given.split('»'))
    if given == "/start":
        bot.reply_to(mes, "Hey! Give me a russian word or a phrase.\
        I'm still a little bit stupid so please mark\
        the accent of the last word with an uppercase letter,\
        for example: 'механИзма' or 'ты совсем идиОт'")
        return
    with open("EO.txt", "r", encoding='utf_8') as f:
        eo = []
        for x in f.readlines():
            eo.append(x.strip().lower())
            eo[-1] = ''.join(eo[-1].split('.'))
            eo[-1] = ''.join(eo[-1].split(','))
            eo[-1] = ''.join(eo[-1].split('-'))
            eo[-1] = ''.join(eo[-1].split(':'))
            eo[-1] = ''.join(eo[-1].split(';'))
            eo[-1] = ''.join(eo[-1].split('"'))
            eo[-1] = ''.join(eo[-1].split("'"))
            eo[-1] = ''.join(eo[-1].split('!'))
            eo[-1] = ''.join(eo[-1].split('?'))
            eo[-1] = ''.join(eo[-1].split(')'))
            eo[-1] = ''.join(eo[-1].split(']'))
            eo[-1] = ''.join(eo[-1].split('>'))
            eo[-1] = ''.join(eo[-1].split('}'))
            eo[-1] = ''.join(eo[-1].split('»'))

        rhymes = []

        for line in eo:
            word = (line.split(' ')[-1]).lower()
            if word[-5:] == given[-5:].lower() and word != given.lower():
                stroka = accents(line)
                if stroka[-5:] == given[-5:]:
                    rhymes.append(line)
        if len(rhymes) < 1:
            for line in eo:
                word = (line.split(' ')[-1]).lower()
                if word[-4:] == given[-4:].lower() and word != given.lower():
                    stroka = accents(line)
                    if stroka[-4:] == given[-4:]:
                        rhymes.append(line)
        if len(rhymes) < 1:
            for line in eo:
                word = (line.split(' ')[-1]).lower()
                if word[-3:] == given[-3:].lower() and word != given.lower():
                    stroka = accents(line)
                    if stroka[-3:] == given[-3:]:
                        rhymes.append(line)
        if len(rhymes) < 1:
            for line in eo:
                word = (line.split(' ')[-1]).lower()
                if word[-2:] == given[-2:].lower() and word != given.lower():
                    stroka = accents(line)
                    if stroka[-2:] == given[-2:]:
                        rhymes.append(line)
                        if len(rhymes) == 1:
                            bot.reply_to(mes,
                                         "Sorry I know this is a shitty rhyme")
    if len(rhymes) == 0:
        bot.reply_to(mes,
                        "Come on woman, even Pushkin didn't\
                     write things like this")
    else:
        bot.reply_to(mes, rhymes[random.randint(0, len(rhymes)-1)])


bot.polling()
