import vk_api,random

token = 'b36eb6c42d5090ebd86fb0e391c8c1721dbc5538458fb0aca34de5c7ae7d84250b2d3207c64b7daa5fdb4'

vk = vk_api.VkApi(token = token)
vk._auth_token()

while True:
    messages = vk.method('messages.getConversations', {'offset' : 0, 'count': 20, 'filter' : 'unanswered'})
    if messages['count'] > 0:         
        text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        if text.lower() == 'привет' or text.lower() == 'привет!':
            vk.method('messages.send',{'user_id':user_id,'message':'Привет!','random_id':random.randint(1,1000)})
        elif text.lower() == 'можно фото какого-нибудь заказа?':
            uploader = vk_api.upload.VkUpload(vk)
            img = uploader.photo_messages('1579936923.jpg')
            media_id = str(img[0]['id'])
            owner_id = str(img[0]['owner_id'])
            vk.method('messages.send',{'user_id':user_id,'attachment':'photo' + owner_id + '_' + media_id,'random_id':random.randint(1,1000)})
        else:    
            vk.method('messages.send',{'user_id':user_id,'message':'Я - бот! И я глуп, как валенок','random_id':random.randint(1,1000)})
