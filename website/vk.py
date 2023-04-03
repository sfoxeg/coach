from datetime import datetime
import requests


def vk_user(id):
    req = requests.get(
        f'https://api.vk.com/method/users.get?access_token=vk1.a'
        f'.hhkoLLWfHCvvCVuRa4pZ4OP2BuNo6VOhKc3rkIRw2hRXus9KbE09mC9pBLlQvzT5i'
        f'-qs6gN1F3Fd_0NR82M8y3Dxn_FxEYtTJExeiKP119y4QUdirUS6hwJXIiLeRA8sLX11FWwfOH4WM8_kPSDzReNO0O'
        f'-XQAdsc9bj3Hho5QIjdRBdXN-NNvMtjxaRyLku7uBtDPjG3O7ranBjmkTFXQ&v=5.131&fields=photo_200&user_ids={id}'
    )
    data = req.json()
    return data['response']


def comments():
    comments = []
    req = requests.get(
        'https://api.vk.com/method/board.getComments?group_id=206202301&topic_id=48151352&count=10&sort=desc&v=5.131'
        '&access_token=55ba544455ba544455ba5444a056a8bd0d555ba55ba544431bba40cd2e621aaf549dc1e')
    data = req.json()
    for comment in data['response']['items']:
        if comment['from_id'] != 319118654:
            date = datetime.fromtimestamp(comment['date']).strftime("%d.%m.%y %H:%M")
            text = comment['text']
            user = vk_user(comment['from_id'])
            name = user[0]['first_name'] + " " + user[0]['last_name'].strip()
            ava = user[0]['photo_200']
            comments.append({"name": name, "ava": ava, "date": date, "text": text})
    return comments
