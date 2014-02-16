from pykakao import kakaotalk

kakao = kakaotalk()
if kakao.auth(""):
    print kakao.session_key
    print kakao.user_id
else:
    print "auth failed."
