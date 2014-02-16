from pykakao import kakaotalk

kakao = kakaotalk("SESSION KEY", "DEVICE ID", USER ID)
if kakao.login():
    while True:
        packet = kakao.translate_response()

        if not packet:
            print "connection closed."

        if packet["command"] == "MSG":
            if packet["body"]["chatLog"]["authorId"] != kakao.user_id:
                kakao.write(packet["body"]["chatLog"]["chatId"], packet["body"]["chatLog"]["message"])
else:
    print "login failed."
