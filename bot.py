# -*- coding: utf-8 -*-

import config
import user_config
import content

import os
import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot(config.token_main)

#FUNCTION ZONE

def help (message):
    bot.send_message(message.chat.id, content.help)

def main_markup (message):
    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but11 = types.KeyboardButton("🗓 Расписание")
    but12 = types.KeyboardButton("📜 Информация")
    but13 = types.KeyboardButton("⚙️ Связь")
    but21 = types.KeyboardButton("📌 1")
    but22 = types.KeyboardButton("📌 2")
    but23 = types.KeyboardButton("📌 3")
    but24 = types.KeyboardButton("📌 4")
    but25 = types.KeyboardButton("📌 5")
    but26 = types.KeyboardButton("🔒 6")
    but27 = types.KeyboardButton("🔒 7")
    but28 = types.KeyboardButton("🔒 8")
    but29 = types.KeyboardButton("🎁")
    but31 = types.KeyboardButton("📚 Статистика")
    but32 = types.KeyboardButton("📖 Отзывы")
    main_markup.row(but11, but12, but13)
    main_markup.row(but21, but22, but23, but24, but25, but26, but27, but28, but29)
    main_markup.row(but31, but32)
    sticker = open (content.sticker_funny, 'rb')
    bot.send_sticker (message.chat.id, sticker, reply_markup=main_markup)

#HANDLER ZONE

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
                main_markup (message)
                markup_type=types.InlineKeyboardMarkup()
                hello_stick = types.InlineKeyboardButton("Подпишись на чат", url='https://t.me/joinchat/Wj-K4YgwOog1NTQ6')
                markup_type.row(hello_stick)
                bot.send_message(message.chat.id, content.hello, reply_markup=markup_type)
            else:
                bot.send_message(message.chat.id, "У вас нет доступа! Напишите @nelly_white")
        elif message.text == '/help':
            help (message)
        elif message.text == '/admin':
            if access[3] == 2:
                admin_markup = types.InlineKeyboardMarkup()
                admin_message = types.InlineKeyboardButton("Сообщение", callback_data='admin_message')
                admin_users = types.InlineKeyboardButton("Пользователи", callback_data='admin_users')
                bot_restart = types.InlineKeyboardButton("🔴 BIG RED BUTTON 🔴", callback_data='bot_restart')
                admin_markup.row(admin_message, admin_users)
                admin_markup.row(bot_restart)
                bot.send_message(message.chat.id, "Вы вошли в Админ Панель.", reply_markup = admin_markup)
            else:
                bot.send_message(message.chat.id, 'Низкий уровень доступа! Обратитесь к @Emin_Pho')
        else:
            bot.send_message(message.chat.id, "Неверная команда")
    except Exception as warring:
        bot.send_message(517561825, message.chat.username + ' call EXCEPT handler_warring: ' + str(warring))
    else:
        pass
    finally:
        bot.send_message(517561825, message.chat.username + ' call COMMAND: ' + message.text)
        db.commit()



@bot.message_handler(content_types=["document", "photo"])
def handler_file(message):
    try:
        user = eval('user_config.'+message.chat.username+'.get')
        if message.content_type == 'photo':
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src =   user_config.hand_over.get('folder') + message.chat.username +'/lesson_'+user('log')+'/' + user_config.hand_over.get('handover') + '/'+ file_info.file_path
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
        elif message.content_type == 'document':
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src =  user_config.hand_over.get('folder') + message.chat.username + '/lesson_'+user('log')+'/' + user_config.hand_over.get('handover') + '/' + file_info.file_path
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
        else:
            pass
        bot.send_message(message.chat.id, "Домашнее задание принято на проверку!")
    except Exception as warring:
        bot.send_message(517561825, warring)
    else:
        bot.send_message(392874912, message.chat.username + ' загрузил файлы в урок №' + str(user('log')))
    finally:
        bot.send_message(517561825, message.chat.username + ' загрузил файлы в урок №' + str(user('log')))



@bot.message_handler(content_types=["text"])
def handler_text(message):
    try:
        if message.text == '🗓 Расписание':
            bot.send_message(message.chat.id, content.datatable)
        elif message.text == '📜 Информация':
            bot.send_message(message.chat.id, content.melted)
            file_description = open(content.info, 'rb')
            bot.send_document(message.chat.id, file_description)
        elif message.text == '⚙️ Связь':
            help (message)
        elif message.text == '📚 Статистика':
            store = user_config.score.get(str(message.chat.username))
            text = "Баллы: {}\nМесто в общем рейтинге: {}\nМаксимальный балл на курсе: {}\n\nПринято ДЗ: {}\nПринято КЗ: {}\nПринято тестов: {}\n".format(store.get('point'),store.get('place'),user_config.hand_over.get('max_point'),store.get('homework_done'),store.get('creativework_done'),store.get('test_done'))
            bot.send_message(message.chat.id, text)
        elif message.text == '📖 Отзывы':
            bot.send_message(message.chat.id, content.feedback)
        elif message.text in ('🔒 1', '🔒 2', '🔒 3', '🔒 4', '🔒 5', '🔒 6', '🔒 7', '🔒 8'):
            bot.send_message(message.chat.id, 'Сначала пройти предыдущий урок!')
        elif message.text in ('🎁',):
            bot.send_message(message.chat.id, content.the_end)
        elif message.text in ('📌 1', '📌 2', '📌 3', '📌 4', '📌 5', '📌 6', '📌 7', '📌 8'): # вызов любого урока
            if message.text == '📌 1': lesson = content.lesson_1.get
            if message.text == '📌 2': lesson = content.lesson_2.get
            if message.text == '📌 3': lesson = content.lesson_3.get
            if message.text == '📌 4': lesson = content.lesson_4.get
            if message.text == '📌 5': lesson = content.lesson_5.get
            if message.text == '📌 6': lesson = content.lesson_6.get
            if message.text == '📌 7': lesson = content.lesson_7.get
            if message.text == '📌 8': lesson = content.lesson_8.get




            log = eval("user_config." + message.chat.username)
            log.update({'log': str(message.text[2])})






            if lesson ('access') == 0: # Урок закрыт
                markup_timetable = types.InlineKeyboardMarkup()
                button_timetable = types.InlineKeyboardButton("Мое расписание", callback_data='timetable')
                markup_timetable.row(button_timetable)
                bot.send_message(message.chat.id, 'Сначала пройти предыдущий урок!')
            elif lesson ('access') == 1: # Урок ожидается
                markup_future_lessons = types.InlineKeyboardMarkup()
                button__future_lessons = types.InlineKeyboardButton(content.date_zoom, url=content.url_zoom)
                markup_future_lessons.row(button__future_lessons)
                bot.send_message(message.chat.id, lesson('topic'), reply_markup=markup_future_lessons)
            elif lesson ('access') == 2: # Урок прошел
                main_markup(message)
                markup_lessons=types.InlineKeyboardMarkup()
                url_lesson = types.InlineKeyboardButton("Смотреть урок", url=lesson('url_lesson')) #Текст, ссылка на фаил и форма отправки
                test = types.InlineKeyboardButton("Пройти Тест", url=lesson('test'))
                conspect = types.InlineKeyboardButton("Открыть конспект", callback_data='conspect'+message.text) #Текст, ссылка на фаил и форма отправки
                homework = types.InlineKeyboardButton("Открыть ДЗ", callback_data='homework'+message.text) #Текст, ссылка на фаил и форма отправки
                creativework = types.InlineKeyboardButton("Открыть КДЗ", callback_data='creativework'+message.text) #Текст, ссылка на фаил и форма отправки
                hand_over_work = types.InlineKeyboardButton("Сдать ДЗ/КЗ", callback_data='hand_over_work')
                markup_lessons.row(url_lesson, conspect)
                markup_lessons.row(homework, creativework, test)
                markup_lessons.row(hand_over_work)
                bot.send_message(message.chat.id, lesson('topic'), reply_markup=markup_lessons)
        else:
            db = sqlite3.connect('nelly_v-ass.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM user WHERE id = ?', (message.chat.id,))
            access = cursor.fetchone()
            db.commit()
            if access[3] == 2:
                content.admin_sent_message = message.text
                bot.send_message(message.chat.id, '...сообщение записанно...')
    except Exception as warring:
        bot.send_message(517561825, message.chat.username + ' call EXCEPT handler_text: ' + str(warring))
    else:
        pass
    finally:
        bot.send_message(517561825, message.chat.username + ' write MESSAGE: ' + message.text)



@bot.callback_query_handler(func=lambda call: True)
def handler_call (call):
    try:
        lesson={
        '1':content.lesson_1.get,
        '2':content.lesson_2.get,
        '3':content.lesson_3.get,
        '4':content.lesson_4.get,
        '5':content.lesson_5.get,
        '6':content.lesson_6.get,
        '7':content.lesson_7.get,
        '8':content.lesson_8.get,
        }

#FUNCTIONAL

        if call.data == 'timetable':
            bot.send_message(call.message.chat.id, content.datatable)

# CONTENT ZONE



        elif call.data[:-3] == 'conspect':
            file_homeches = open(lesson[call.data[10]]('lesson'), 'rb')
            bot.send_document(call.message.chat.id, file_homeches)
        elif call.data[:-3] == 'homework':
            file_homeches = open(lesson[call.data[10]]('homework'), 'rb')
            bot.send_document(call.message.chat.id, file_homeches)
        elif call.data[:-3] == 'creativework':
            file_homeches = open(lesson[call.data[14]]('create_work'), 'rb')
            bot.send_document(call.message.chat.id, file_homeches)

#HAND OVER WORK

        elif call.data == 'hand_over_work': # Обработчик ДЗ|КДЗ
            markup_handover = types.InlineKeyboardMarkup()
            handover_homework = types.InlineKeyboardButton("Домашнее задание", callback_data='handover_homework')
            handover_creativework = types.InlineKeyboardButton("Креативное задание", callback_data='handover_creativework')
            markup_handover.row(handover_homework, handover_creativework)
            bot.send_message(call.message.chat.id, "Какое задание ты хочешь сдать?", reply_markup=markup_handover)
        elif call.data == 'handover_homework':
            bot.send_message(call.message.chat.id, "Пришли фото в чат...")
            user_config.hand_over.update({'handover': 'homework'})
        elif call.data == 'handover_creativework':
            bot.send_message(call.message.chat.id, "Пришли фото в чат...")
            user_config.hand_over.update({'handover': 'creativework'})

# ADMIN ZONE

        elif call.data == 'admin_message':
            admin_markup_mail = types.InlineKeyboardMarkup()
            admin_message_see = types.InlineKeyboardButton("Просмотр", callback_data='admin_message_see')
            admin_message_saw = types.InlineKeyboardButton("Отправить", callback_data='admin_message_saw')
            admin_markup_mail.row(admin_message_see, admin_message_saw)
            bot.send_message(call.message.chat.id, "Введите сообщение", reply_markup = admin_markup_mail)
        elif call.data == 'admin_message_see':
            bot.send_message(call.message.chat.id, content.admin_sent_message)
        elif call.data == 'admin_message_saw':
            user_pull = ["392874912", "517561825", "166254027", "900799157", "962932095", "581487686", "446664973", "328643465"]
            for i in user_pull:
                bot.send_message(i, content.admin_sent_message)

        elif call.data == 'admin_users':
            db = sqlite3.connect('nelly_v-ass.db')
            cursor = db.cursor()
            cursor.execute('SELECT login FROM user')
            admin_access = cursor.fetchall()
            access = cursor.fetchone()
            db.commit()
            admin_markup_mail = types.InlineKeyboardMarkup()
            for i in range(len(admin_access)):
                name = str(admin_access[i][0])
                admin_access[i] = types.InlineKeyboardButton(name, callback_data = name)
                admin_markup_mail.row(admin_access[i])
            bot.send_message(call.message.chat.id, "Список пользователей", reply_markup = admin_markup_mail)

#USERS ACCOUNT

        elif call.data in ('Emin_Pho', 'nelly_white', 'Kamila_Usmanova', 'heytanne', 'AnyaDD', 'yannnut', 'lowely_pony', 'Mr_Moony007', 'Nikpleskach'):
            user_config.hand_over.update({'key': call.data})
            user_account = types.InlineKeyboardMarkup()
            ho_les1 = types.InlineKeyboardButton("Урок 1", callback_data='ho_les1')
            ho_les2 = types.InlineKeyboardButton("Урок 2", callback_data='ho_les2')
            ho_les3 = types.InlineKeyboardButton("Урок 3", callback_data='ho_les3')
            ho_les4 = types.InlineKeyboardButton("Урок 4", callback_data='ho_les4')
            ho_les5 = types.InlineKeyboardButton("Урок 5", callback_data='ho_les5')
            ho_les6 = types.InlineKeyboardButton("Урок 6", callback_data='ho_les6')
            ho_les7 = types.InlineKeyboardButton("Урок 7", callback_data='ho_les7')
            ho_les8 = types.InlineKeyboardButton("Урок 8", callback_data='ho_les8')
            static = types.InlineKeyboardButton("Рейтинг", callback_data='static' + str(call.data))
            user_account.row(ho_les1, ho_les2, ho_les3, ho_les4)
            user_account.row(ho_les5, ho_les6, ho_les7, ho_les8)
            user_account.row(static)
            bot.send_message(call.message.chat.id, 'Личный Кабинет пользователя: ' + call.data, reply_markup = user_account)
        elif call.data[:-1] == 'ho_les':
            bot.send_message(call.message.chat.id, 'Загружаю КДЗ...')
            part = content.folder + 'users/' + user_config.hand_over.get ('key') +  '/lesson_'+ call.data[6] + '/creativework/documents/'
            pr = os.listdir(path=part)
            for i in pr:
                if i != '.DS_Store':
                    photo = open(part+i, 'rb')
                    bot.send_photo(call.message.chat.id, photo)
            part = content.folder + 'users/' + user_config.hand_over.get ('key') +  '/lesson_' + call.data[6] + '/creativework/photos/'
            pr = os.listdir(path=part)
            for i in pr:
                if i != '.DS_Store':
                    photo = open(part+i, 'rb')
                    bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, 'КДЗ больше нет')
            bot.send_message(call.message.chat.id, 'Загружаю ДЗ...')
            part = content.folder + 'users/' + user_config.hand_over.get ('key') +  '/lesson_'+ call.data[6] + '/homework/documents/'
            pr = os.listdir(path=part)
            for i in pr:
                if i != '.DS_Store':
                    photo = open(part+i, 'rb')
                    bot.send_photo(call.message.chat.id, photo)
            part = content.folder + 'users/' + user_config.hand_over.get ('key') +  '/lesson_' + call.data[6] + '/homework/photos/'
            pr = os.listdir(path=part)
            for i in pr:
                if i != '.DS_Store':
                    photo = open(part+i, 'rb')
                    bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, 'ДЗ больше нет')



        elif call.data[:6] == 'static':
            x = 1

            while x <= 9 :
                for i in user_config.score:
                    user = user_config.score.get(str(i))
                    if user.get('place') == x:
                        bot.send_message(call.message.chat.id,  str(user.get('place')) + ' | ' + str(i) + ' : ' + str(user.get('point')) + ' points')
                x = x + 1
            bot.send_message(call.message.chat.id, 'Напиши кол-во баллов и тип (дз/кдз/тест)')













        elif call.data == 'bot_restart':
            bot.send_message(call.message.chat.id, 'Функция перезагрузки бота. В разработке')
        else:
            pass
    except Exception as warring:
        bot.send_message(517561825, call.message.chat.username + ' call EXCEPT handler_call: ' + str(warring))
    else:
        pass
    finally:
        bot.send_message(517561825, call.message.chat.username + ' CALLING: ' + call.data)



@bot.message_handler(content_types=[
'sticker', 'video', 'video_note', 'voice', 'location', 'contact', 'new_chat_members', 'left_chat_member',
'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created',
'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'
])
def handler_warring(message):
    try:
        bot.send_message(message.chat.id, "ОШИБКА 601: Неверный тип данных")
    except Exception as warring:
        bot.send_message(517561825, message.chat.username + ' call EXCEPT handler_warring: ' + str(warring))
    else:
        pass
    finally:
        bot.send_message(517561825, message.chat.username + ' calling: ' + str(message))



bot.polling(none_stop=True, interval=0, timeout=6) #RUN
