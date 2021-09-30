import requests
pararm = {


}
headers = {'cookie': 'SESSIONID=9fff20f1be362709178ed48385b1ee1c7a553b0d; UM_distinctid=17bc2ce26801e8-07d301f32d1982-3e604809-149c48-17bc2ce26818d3; Hm_lvt_52c42de35032567eb9d7a24a43c84bda=1631060896; CNZZDATA1261815924=182746753-1631060473-https%253A%252F%252Fwww.baidu.com%252F%7C1631149801; Hm_lpvt_52c42de35032567eb9d7a24a43c84bda=1631153665'
}
def postjy(url):
    html = requests.get(url,headers=headers)
    print(html.text)
postjy('https://www.jianyu360.cn/list/stype/ZBGG_ZB.html')
