

import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
def write_message(sender, message):
    authorize.method('messages.send',{'user_id': sender,'message': message, 'random_id': get_random_id(), 'attachment':','.join(attachments) })
token = 'f857090ca9bd17fc51c3b38d551ff7661f17db8719bb618ac382f024e9d5241ba326e0874492f057e5bfa'
image = 'C:/test/photo_for_bot.jpg'
authorize = vk_api.VkApi(token = token)
longpoll = VkLongPoll(authorize)
upload = VkUpload(authorize)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived_messsage = event.text
        sender = event.user_id
        attachments = []
        upload_image = upload.photo_messages(photos=image)[0]
        attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
        if reseived_messsage.lower() == 'привет' or reseived_messsage.lower() == 'привет!':
            write_message(sender,'Добрый день!')
        elif reseived_messsage.lower() == 'пока' or reseived_messsage.lower() == 'пока!':
            write_message(sender,'До свидания!')
        else:
            write_message(sender, 'Я вас не понимаю....')






