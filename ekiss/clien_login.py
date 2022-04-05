# parser.py
import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보를 넣어줍시다. (모두 문자열입니다!)
LOGIN_INFO = {
    'userId': 'FILL user id',
    'userPassword': 'FILL password'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # 우선 클리앙 홈페이지에 들어가 봅시다.
    first_page = s.get('https://www.clien.net/')
    html = first_page.text
    soup = bs(html, 'html.parser')
    csrf = soup.find('input', {'name': '_csrf'}) # input태그 중에서 name이 _csrf인 것을 찾습니다.
    print(csrf['value']) # 위에서 찾은 태그의 value를 가져옵니다.

    # 이제 LOGIN_INFO에 csrf값을 넣어줍시다.
    # (p.s.)Python3에서 두 dict를 합치는 방법은 {**dict1, **dict2} 으로 dict들을 unpacking하는 것입니다.
    LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}
    print(LOGIN_INFO)

    # 이제 다시 로그인을 해봅시다.
    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    # 어떤 결과가 나올까요? (200이면 성공!)
    print(login_req.status_code)
    # 로그인이 되지 않으면 경고를 띄워줍시다.
    if login_req.status_code != 200:
        raise Exception('로그인이 되지 않았어요! 아이디와 비밀번호를 다시한번 확인해 주세요.')

    # -- 여기서부터는 로그인이 된 세션이 유지됩니다 --
    # 이제 장터의 게시글 하나를 가져와 봅시다. 아래 예제 링크는 중고장터 공지글입니다.
    post_one = s.get('https://www.clien.net/service/board/rule/10707408')
    soup = bs(post_one.text, 'html.parser') # Soup으로 만들어 줍시다.
    # 아래 CSS Selector는 공지글 제목을 콕 하고 집어줍니다.
    title = soup.select('#div_content > div.post-title > div.title-subject > div')
    contents = soup.select('#div_content > div.post.box > div.post-content > div.post-article.fr-view')
    # HTML을 제대로 파싱한 뒤에는 .text속성을 이용합니다.
    print(title[0].text) # 글제목의 문자만을 가져와봅시다.
    # [0]을 하는 이유는 select로 하나만 가져와도 title자체는 리스트이기 때문입니다.
    # 즉, 제목 글자는 title이라는 리스트의 0번(첫번째)에 들어가 있습니다.
    print(contents[0].text) # 글내용도 마찬가지겠지요?

