def get_absolute_url(url, *args, **kwargs):
    s = ''
    s = s +url
    for i in args:
        s = s +'/' +i
    s = s +'?'
    for k, v in kwargs.items():
        s = s +k +'=' +v +'&'
    s = s[:len(s)-1]
    return s


print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))
