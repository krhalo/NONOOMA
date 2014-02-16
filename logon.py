from pykakao import kakaotalk

kakao = kakaotalk()
if kakao.auth("halo1235@naver.com", "uiop1234", "HALO", "1"):
    print kakao.session_key
    print kakao.user_id
else:
    print "auth failed."
