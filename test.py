# -*- coding: utf-8 -*-

import config, user_config, content
import time, sqlite3, telebot
from telebot import types





bot.message_handler(content_types=['text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message'])
def handler_file(message):
    bot.send_message(message.chat.id, message)

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

        bot.send_message(517561825, message.chat.username + ' загрузил файлы')
        bot.send_message(392874912, message.chat.username + ' загрузил файлы')
    finally:
        pass
