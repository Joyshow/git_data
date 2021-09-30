url_config = {
    'abchina': {
        'class1': {
            'selecter': {'title': 'ul > li > span.details_rightC.fl > a', 'time': 'ul > li > span > span.details_rightD.fr'},
            'urls': [
                'http://www.abchina.com/cn/aboutabc/cggg/',
            ]
        },
    },
    }
asdd={"nihao":"wobuhao"}
dict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(url_config.get("abchina"))
