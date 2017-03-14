
main_url = 'http://www.imooc.com'
video_url = 'http://www.imooc.com/course/ajaxmediainfo/?mid={mid}&mode=flash'
user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/36.0.1985.143 Safari/537.36")
headers = {
    'User-Agent': user_agent,
    'Referer': main_url,
}

QUALITY = ['H', 'M', 'L']
