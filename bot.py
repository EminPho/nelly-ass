# -*- coding: utf-8 -*-

import config
import user_config
import content

import time
import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot(config.token_main)



@bot.message_handler(commands=['start', 'help', 'admin'])
def handler_commands (message):
    try:
        db = sqlite3.connect('nelly_v-ass.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM user WHERE login = ?', (message.chat.username,))
        access = cursor.fetchone()
        if message.text == '/start':
            if access is None:
                cursor.execute("""INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (message.chat.id, message.chat.username, message.chat.first_name, 0, 1000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000))
                bot.send_message(message.chat.id, "Вы впервые зашли! Для доступа к курсу напишите @nelly_white")
            elif access[3] > 0:
                main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                but11 = types.KeyboardButton("🗓 Расписание")
                but12 = types.KeyboardButton("📜 Информация")
                but13 = types.KeyboardButton("⚙️ Связь")
                but21 = types.KeyboardButton("📌 1")
                but22 = types.KeyboardButton("📌 2")
                but23 = types.KeyboardButton("🔒 3")
                but24 = types.KeyboardButton("🔒 4")
                but25 = types.KeyboardButton("🔒 5")
                but26 = types.KeyboardButton("🔒 6")
                but27 = types.KeyboardButton("🔒 7")
                but28 = types.KeyboardButton("🔒 8")
                but29 = types.KeyboardButton("🎁")
                but31 = types.KeyboardButton("📚 Статистика")
                but32 = types.KeyboardButton("📖 Отзывы")
                but0 = types.KeyboardButton("Admin_Panel")
                main_markup.row(but11, but12, but13)
                main_markup.row(but21, but22, but23, but24, but25, but26, but27, but28, but29)
                main_markup.row(but31, but32)
                # Отправка стикера приветствия и главной клавиатуры
                sticker = open (config.sticker_funny, 'rb')
                bot.send_sticker (message.chat.id, sticker, reply_markup=main_markup)
                # Отправка кнопки на подписаться
                markup_type=types.InlineKeyboardMarkup()
                hello_stick = types.InlineKeyboardButton("Подпишись на чат", url='https://t.me/joinchat/Wj-K4YgwOog1NTQ6')
                markup_type.row(hello_stick)
                bot.send_message(message.chat.id, content.hello, reply_markup=markup_type)
            else:
                bot.send_message(message.chat.id, "У вас нет доступа! Напишите @nelly_white")
        elif message.text == '/help':
            bot.send_message(message.chat.id, 'В разработке. Плановая реализация в Version Betta')
        elif message.text == '/admin':
            if access[3] == 2:
                admin_markup = types.InlineKeyboardMarkup()
                admin_message = types.InlineKeyboardButton("Сообщение", callback_data='admin_message')
                admin_users = types.InlineKeyboardButton("Пользователи", callback_data='admin_users')
                admin_markup.row(admin_message, admin_users)
                bot.send_message(message.chat.id, "Вы вошли в Админ Панель.", reply_markup = admin_markup)
            else:
                bot.send_message(message.chat.id, 'Низкий уровень доступа! Обратитесь к @Emin_Pho')
        else:
            bot.send_message(message.chat.id, "Неверная команда")
            bot.send_message(517561825, 'Введена команда'+message.text)
    except Exception as warring:
        bot.send_message(517561825, warring)
    else:
        bot.send_message(517561825, message.chat.username + ' ввел команду: ' + message.text)
    finally:
        db.commit()



@bot.message_handler(content_types=['photo'])
def handler_file(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'users/' + message.chat.username + '/lesson_1/' + user_config.Emin_Pho.get('handover') + '/' + str(message.date)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
    except Exception as warring:
        bot.send_message(517561825, warring)
    else:
        if message.chat.username == "Emin_Pho":
            if user_config.Emin_Pho.get ('handover_hw') == True:
                user_config.Emin_Pho.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.Emin_Pho.get ('handover_cw') == True:
                user_config.Emin_Pho.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        if message.chat.username == "nelly_white":
            if user_config.nelly_white.get ('handover_hw') == True:
                user_config.nelly_white.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.nelly_white.get ('handover_cw') == True:
                user_config.nelly_white.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        if message.chat.username == "AnyaDD":
            if user_config.AnyaDD.get ('handover_hw') == True:
                user_config.AnyaDD.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.AnyaDD.get ('handover_cw') == True:
                user_config.AnyaDD.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        if message.chat.username == "heytanne":
            if user_config.heytanne.get ('handover_hw') == True:
                user_config.heytanne.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.heytanne.get ('handover_cw') == True:
                user_config.heytanne.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        if message.chat.username == "Kamila_Usmanova":
            if user_config.Kamila_Usmanova.get ('handover_hw') == True:
                user_config.Kamila_Usmanova.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.Kamila_Usmanova.get ('handover_cw') == True:
                user_config.Kamila_Usmanova.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        if message.chat.username == "lowely_pony":
            if user_config.lowely_pony.get ('handover_hw') == True:
                user_config.lowely_pony.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.lowely_pony.get ('handover_cw') == True:
                user_config.lowely_pony.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        if message.chat.username == "Mr_Moony007":
            if user_config.Mr_Moony007.get ('handover_hw') == True:
                user_config.Mr_Moony007.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.Mr_Moony007.get ('handover_cw') == True:
                user_config.Mr_Moony007.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        if message.chat.username == "Nikpleskach":
            if user_config.Nikpleskach.get ('handover_hw') == True:
                user_config.Nikpleskach.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.Nikpleskach.get ('handover_cw') == True:
                user_config.Nikpleskach.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        if message.chat.username == "yannnut":
            if user_config.yannnut.get ('handover_hw') == True:
                user_config.yannnut.update({'handover_hw': False})
                bot.send_message(message.chat.id, "Домашняя работа принято на проверку!")
            elif user_config.yannnut.get ('handover_cw') == True:
                user_config.yannnut.update({'handover_cw': False})
                bot.send_message(message.chat.id, "Креативное задание принято на проверку!")
            else:
                pass
        bot.send_message(517561825, message.chat.username + ' загрузил файлы')
        bot.send_message(392874912, message.chat.username + ' загрузил файлы')
    finally:
        pass



@bot.message_handler(content_types=["text"])
def handler_text(message):




















 # Костыль на обновление
    db = sqlite3.connect('nelly_v-ass.db')
    cursor = db.cursor()
    cursor.execute("""UPDATE user SET id=? WHERE login=?""", (message.chat.id, message.chat.username))
    db.commit()


    if message.text == '🗓 Расписание':
        bot.send_message(message.chat.id, content.schedule)
    elif message.text == '📜 Информация':
        bot.send_message(message.chat.id, content.melted)
        file_description = open(config.info, 'rb')
        bot.send_document(message.chat.id, file_description)
    elif message.text == '⚙️ Связь':
        bot.send_message(message.chat.id, "Если есть вопросы, пиши @nelly_white")
    elif message.text == '📚 Статистика':
        bot.send_message(message.chat.id, 'В разработке. Плановая реализация в Version Betta')
    elif message.text == '📖 Отзывы':
        bot.send_message(message.chat.id, 'В разработке. Плановая реализация в Version Betta')
    elif message.text in ('🔒 1', '🔒 2', '🔒 3', '🔒 4', '🔒 5', '🔒 6', '🔒 7', '🔒 8'):
        bot.send_message(message.chat.id, 'Сначала пройти предыдущий урок!')
    elif message.text in ('🎁',):
        bot.send_message(message.chat.id, content.the_end)
    elif message.text in ('📌 1', '📌 2', '📌 3', '📌 4', '📌 5', '📌 6', '📌 7', '📌 8'): # вызов любого урока

        # костыльный блок, рефакторинг
        if message.text == '📌 1': lesson = content.lesson_1.get
        if message.text == '📌 2': lesson = content.lesson_2.get
        if message.text == '📌 3': lesson = content.lesson_3.get
        if message.text == '📌 4': lesson = content.lesson_4.get
        if message.text == '📌 5': lesson = content.lesson_5.get
        if message.text == '📌 6': lesson = content.lesson_6.get
        if message.text == '📌 7': lesson = content.lesson_7.get
        if message.text == '📌 8': lesson = content.lesson_8.get






        if lesson ('access') == 0: # Урок закрыт
            markup_timetable = types.InlineKeyboardMarkup()
            button_timetable = types.InlineKeyboardButton("Мое расписание", callback_data='timetable')
            markup_timetable.row(button_timetable)
            bot.send_message(message.chat.id, 'Сначала пройти предыдущий урок!', reply_markup = markup_timetable)

        elif lesson ('access') == 1: # Урок ожидается
            markup_future_lessons = types.InlineKeyboardMarkup()
            button__future_lessons = types.InlineKeyboardButton("Урок пройдет 05.08 в Zoom", url=config.url_zoom)
            markup_future_lessons.row(button__future_lessons)
            bot.send_message(message.chat.id, content.lesson_1.get('topic'), reply_markup=markup_future_lessons)

        elif lesson ('access') == 2: # Урок прошел
            markup_lessons=types.InlineKeyboardMarkup()
            les1_url = types.InlineKeyboardButton("Скачать Урок", url=content.lesson_1.get('url_lesson')) #Текст, ссылка на фаил и форма отправки
            les1_hq = types.InlineKeyboardButton("Скачать ДЗ", callback_data='les1_hq') #Текст, ссылка на фаил и форма отправки
            les1_cq = types.InlineKeyboardButton("Скачать КДЗ", callback_data='les1_cq') #Текст, ссылка на фаил и форма отправки
            les1_t = types.InlineKeyboardButton("Пройти Тест (Google Forms)", url='https://forms.gle/tdGSpsLBXyUY5oddA')
            les1_hw = types.InlineKeyboardButton("Сдать ДЗ/КЗ", callback_data='les1_hw')
            markup_lessons.row(les1_url)
            markup_lessons.row(les1_hq, les1_cq, les1_t)
            markup_lessons.row(les1_hw)

            bot.send_message(message.chat.id, content.lesson_1.get('topic'), reply_markup=markup_lessons)

        else: # Обработка исключений
            pass
    else:
        db = sqlite3.connect('nelly_v-ass.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM user WHERE id = ?', (message.chat.id,))
        access = cursor.fetchone()
        db.commit()
        if access[3] == 2:
            content.admin_sent_message = message.text
            bot.send_message(message.chat.id, '...сообщение записанно...')
        else:
            bot.send_message(message.chat.id, 'Я не знаю ответа')



@bot.callback_query_handler(func=lambda call: True)
def commands (call):

    if call.data == 'timetable':
        bot.send_message(call.message.chat.id, content.schedule)

    elif call.data == 'les1_hw': # Обработчик ДЗ|КДЗ
        markup_handover = types.InlineKeyboardMarkup()
        button_handover_hw = types.InlineKeyboardButton("Домашнее задание", callback_data='button_handover_hw')
        button_handover_cw = types.InlineKeyboardButton("Креативное задание", callback_data='button_handover_cw')
        markup_handover.row(button_handover_hw, button_handover_cw)
        bot.send_message(call.message.chat.id, "Урок 1. Какое задание ты хочешь сдать?", reply_markup=markup_handover)
    elif call.data == 'button_handover_hw':
        if user_config.Emin_Pho.get('handover_hw') == True:
            bot.send_message(call.message.chat.id, "Пришли фото в чат, (прикрепить => фото или видео => быстрая отправка).")
            user_config.Emin_Pho.update({'handover': 'homework'})
        else:
            bot.send_message(call.message.chat.id, "Работа на проверке!")

    elif call.data == 'button_handover_cw':
        if user_config.Emin_Pho.get('handover_cw') == True:
            bot.send_message(call.message.chat.id, "Пришли фото в чат, (прикрепить => фото или видео => быстрая отправка).")
            user_config.Emin_Pho.update({'handover': 'creativework'})
        else:
            bot.send_message(call.message.chat.id, "Работа на проверке!")

# при отправке файла    такжепринимать документы    добавить пользователей
# что то в админке и перепроверка    и обновления


    elif call.data == 'les1_les':
        file_homeches = open(content.lesson_1.get ('lesson'), 'rb')
        bot.send_document(call.message.chat.id, file_homeches)

    elif call.data == 'les1_hq': # Текст, фаил и возможность сдать дз (КАК будет пересдача?)
        file_homeches = open(content.lesson_1.get ('homework'), 'rb')
        bot.send_document(call.message.chat.id, file_homeches)

    elif call.data == 'les1_cq': # ()
        file_homeches = open(content.lesson_1.get ('create_work'), 'rb')
        bot.send_document(call.message.chat.id, file_homeches)

    elif call.data == 'admin_message': # Отправка сообщения в бот
        admin_markup_mail = types.InlineKeyboardMarkup()
        admin_message_see = types.InlineKeyboardButton("Просмотр", callback_data='admin_message_see')
        admin_message_saw = types.InlineKeyboardButton("Отправить", callback_data='admin_message_saw')
        admin_markup_mail.row(admin_message_see, admin_message_saw)
        bot.send_message(call.message.chat.id, "Введите сообщение", reply_markup = admin_markup_mail)
    elif call.data == 'admin_message_see': # Проверка сообщения при отправка
        bot.send_message(call.message.chat.id, content.admin_sent_message)
    elif call.data == 'admin_message_saw': # Отправка сообщения в бот
        user_pull = ["392874912", "517561825", "166254027", "900799157", "962932095", "581487686", "446664973", "328643465"]
        for i in user_pull:
            bot.send_message(i, content.admin_sent_message)

    elif call.data == 'admin_users': # Просмотр всех пользователей
        db = sqlite3.connect('nelly_v-ass.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM user')
        admin_access = cursor.fetchall()
        access = cursor.fetchone()
        db.commit()
        bot.send_message(call.message.chat.id, '\n'.join(map(str, admin_access)))
    else:
        bot.send_message(call.message.chat.id, text='Ошибка 101. Напиши @Emin_Pho.')



bot.polling(none_stop=True, interval=0, timeout=6) #RUN
