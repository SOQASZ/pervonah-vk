import vk_api
import time

# Заменить на свой логин и пароль
USERNAME = 'username'
PASSWORD = 'password'

vk_session = vk_api.VkApi(USERNAME, PASSWORD)
vk_session.auth()

vk = vk_session.get_api()

# Группы, по которым будет работать первонах
group_ids = [173936135, 123456789]

# Комментарии
comment_texts = ['Вы лучшие!', 'Хороший контент!']

last_timestamp = int(time.time())

while True:
    # Ждём 30 секунд перед тем, как проверить новые посты
    time.sleep(30)

    for group_id in group_ids:
        # Получаем последний пост в группе
        posts = vk.wall.get(owner_id=-group_id, count=10, offset=0, filter='all', latest=1, fields='post_type')['items']

        # Проходим по постам
        for post in posts:
            if post['date'] > last_timestamp:
                for comment_text in comment_texts:
                    # Оставляем коммент
                    vk.wall.createComment(owner_id=-group_id, post_id=post['id'], message=comment_text)

                # Обновляем timestamp
                last_timestamp = post['date']