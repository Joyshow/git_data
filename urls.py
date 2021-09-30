

#关键词列表
keywords = ['外部数据', '数据核验', '大数据', '风险验证', '反欺诈', '服务认证', '大数据服务', '三方数据', '数据采购', '数据认证',
            '大数据风控', '风控数据', '身份认证', '运营商数据', '司法涉诉信息', '信息识别', '身份证', '手机号码', '风险核验', '信息识别',
            '人脸识别', '银行卡', '实名', '个人信息', '一键登录', '免密登录', '本机核验']

#URL地址词典
url_config = {
    'abchina': {
        'class1': {
            'selecter': {'title': 'ul > li > span.details_rightC.fl > a', 'time': 'ul > li > span > span.details_rightD.fr'},
            'urls': [
                'http://www.abchina.com/cn/aboutabc/cggg/',
            ]
        },
    },
    'dlzb': {
        'class1': {
            'selecter': {'title': 'ul.c_ul3 > li > a', 'time': 'ul.c_ul3 > li > span'},
            'urls': [
                'https://zggdjt.dlzb.com/', 'https://rmbx.dlzb.com/', 'https://rsbx.dlzb.com/', 'https://zgpa.dlzb.com/',
            ]
        },
        'class2': {
            'selecter': {'title': 'div.con_list > ul > li > a.gccon_title', 'time': 'div.con_list > ul > li > span.gc_date'},
            'urls': [
                'https://www.dlzb.com/zb/kw-hengqinrenshoubaoxianyouxiangongsi.html',
            ]
        },
        'class3': {
            'selecter': {'title': 'tr > td:nth-child(1) > a', 'time': 'tr > td.ttime'},
            'urls': [
                'https://www.dlzb.com/dxdl/',
            ]
        },
        'class4': {
            'selecter': {'title': 'li.bg_li > a:nth-child(1)', 'time': 'li.bg_li > span'},
            'urls': [
                'https://www.dlzb.com/c-65739/', 'https://www.dlzb.com/c-41113/', 'https://www.dlzb.com/c-82063/',
                'https://www.dlzb.com/c-41483/', 'https://www.dlzb.com/c-51769/',
            ]
        },
    },
    'zhaobiao': {
        'class1': {
            'selecter': {'title': 'ul > li > span > a', 'time': 'ul > li > span.r'},
            'urls': [
                'https://www.zhaobiao.cn/company_id_404534.html',
            ]
        },
    },
    'okcis': {
        'class1': {
            'selecter': {'title': 'ul.lefts.yinying > li > samp.zuo > a:nth-child(1)', 'time': 'ul.lefts.yinying > li > samp.you'},
            'urls': [
                'https://www.okcis.cn/o3/141034', 'https://www.okcis.cn/o3/133321', 'https://www.okcis.cn/o3/122004',
                'https://www.okcis.cn/o3/126913', 'https://www.okcis.cn/o3/28975', 'https://www.okcis.cn/o3/138363',
                'https://www.okcis.cn/o3/119673', 'https://www.okcis.cn/o3/140568', 'https://www.okcis.cn/o3/119172',
                'https://www.okcis.cn/o3/123276', 'https://www.okcis.cn/o3/130072', 'https://www.okcis.cn/o3/119085',
                'https://www.okcis.cn/o3/122974', 'https://www.okcis.cn/o3/122968', 'https://www.okcis.cn/o3/122748',
                'https://www.okcis.cn/o3/118526', 'https://www.okcis.cn/o3/136594',
            ]
        },
        'class2': {
            'selecter': {'title': '#contentspace > div:nth-child(1) > div > h4 > a', 'time': '#contentspace > div:nth-child(1) > div > p.cgggz_p01_20150117'},
            'urls': [
                'https://www.okcis.cn/zhaobiaoyezhu/1729677.html',
            ]
        }
    },
    'chinabidding': {
        'class1': {
            'selecter': {'title': 'ul > li.td_1.td_a > a', 'time': 'ul > li.td_2.dq_rq'},
            'urls': [
                'https://www.chinabidding.cn/18478_cw/',
                'https://www.chinabidding.cn/13295_cw/',
                'https://w087_cww.chinabidding.cn/13w/',
            ]
        },
    },
    'boc': {
        'class1': {
            'selecter': {'title': 'div.main > div > ul > li > a', 'time': 'div.main > div > ul > li > span'},
            'urls': [
                'https://www.boc.cn/aboutboc/bi6/',
            ]
        },
    },
    'bidcenter': {
        'class1': {
            'selecter': {'title': 'span.aa > a', 'time': 'span.a3'},
            'urls': [
                'https://www.bidcenter.com.cn/newssearchyz-9581512.html', 'https://www.bidcenter.com.cn/newssearchyz-77230991.html',
                'https://www.bidcenter.com.cn/newssearchyz-63090125.html', 'https://www.bidcenter.com.cn/newssearchyz-70055233.html',
                'https://www.bidcenter.com.cn/newssearchyz-42503033.html', 'https://www.bidcenter.com.cn/newssearchyz-25782653.html',
                'https://www.bidcenter.com.cn/newssearchyz-35149384.html', 'https://www.bidcenter.com.cn/newssearchyz-50095188.html',
                'https://www.bidcenter.com.cn/newssearchyz-24941692.html', 'https://www.bidcenter.com.cn/newssearchyz-35082659.html',
                'https://www.bidcenter.com.cn/newssearchyz-49989502.html', 'https://www.bidcenter.com.cn/newssearchyz-66515539.html',
                'https://www.bidcenter.com.cn/newssearchyz-16594009.html', 'https://www.bidcenter.com.cn/newssearchyz-8696369.html',
                'https://www.bidcenter.com.cn/newssearch-15010437.html', 'https://www.bidcenter.com.cn/newssearchyz-21203517.html',
                'https://www.bidcenter.com.cn/newssearchyz-62853163.html', 'https://www.bidcenter.com.cn/newssearchyz-41637044.html',
                'https://www.bidcenter.com.cn/newssearchyz-61167030.html', 'https://www.bidcenter.com.cn/newssearchyz-15391767.html',
                'https://www.bidcenter.com.cn/newssearchyz-32770132.html', 'https://www.bidcenter.com.cn/newssearchyz-28087600.html',
                'https://www.bidcenter.com.cn/newssearchyz-15342507.html', 'https://www.bidcenter.com.cn/newssearchyz-50158126.html',
                'https://www.bidcenter.com.cn/newssearchyz-4621740.html', 'https://www.bidcenter.com.cn/newssearchyz-61279796.html',
                'https://www.bidcenter.com.cn/newssearchyz-24083334.html', 'https://www.bidcenter.com.cn/newssearchyz-61883039.html',
                'https://www.bidcenter.com.cn/newssearchyz-16328685.html', 'https://www.bidcenter.com.cn/newssearchyz-47147146.html',
                'https://www.bidcenter.com.cn/newssearchyz-25294952.html', 'https://www.bidcenter.com.cn/newssearchyz-25957909.html',
                'https://www.bidcenter.com.cn/newssearchyz-48980492.html', 'https://www.bidcenter.com.cn/newssearchyz-51125039.html',
                'https://www.bidcenter.com.cn/',
            ]
        },
        'class2': {
            'selecter': {'title': 'div.aa > a', 'time': 'span.a3 > span.a3'},
            'urls': [
                'https://www.bidcenter.com.cn/gongshangyinxing/',
            ]
        },
        'class3': {
            'selecter': {'title': 'div.zz_list > div:nth-child(1) > a', 'time': 'div.zz_list > div:nth-child(1) > p'},
            'urls': [
                'https://www.bidcenter.com.cn/zhaobiao/zbkeyw-23610.html', 'https://www.bidcenter.com.cn/zhaobiao/zbkeyw-51465.html',
            ]
        },
    },
    'hbx': {
        'class1': {
            'selecter': {'title': 'div.pro_contlist > ul > li > a > span.fl.pro_word', 'time': 'div.pro_contlist > ul > li > a > span.fr.pro_time'},
            'urls': [
                'http://www.hxb.com.cn/jrhx/hxzx/hxxw/cggg/',
            ]
        },
    },
    'chinapost': {
        'class1': {
            'selecter': {'title': '#ReportIDname > a', 'time': '#ReportIDIssueTime'},
            'urls': [
                'http://www.chinapost.com.cn/html1/category/181313/7338-1.htm',
            ]
        },
    },
    'ccgp': {
        'class1': {
            'selecter': {'title': 'div.vF_detail_relcontent.mt13 > div.vF_detail_relcontent_lst > ul > li > a',
                         'time': 'div.vF_detail_relcontent.mt13 > div.vF_detail_relcontent_lst > ul > li > em:nth-child(3)'},
            'urls': [
                'http://www.ccgp.gov.cn/cggg/dfgg/', 'http://www.ccgp.gov.cn/',
            ]
        },
    },
    'qmzhaobiao': {
        'class1': {
            'selecter': {'title': 'div.page_left_div > dl > dd > a', 'time': 'div.page_left_div > dl > dd > span.bidSpan2'},
            'urls': [
                'https://bulletin.cebpubservice.com/biddingBulletin/2021-04-01/4595319.html',
                'http://bulletin.cebpubservice.com/',
                'http://qmzhaobiao.com/bidding/org_59131.html'
            ]
        }
    },
    'tianyancha': {
        'class1': {
            'selecter' : {'title': 'div.data-content > table > tbody > tr > td.left-col > a', 'time': 'div.data-content > table > tbody > tr > td:nth-child(2)'},
            'urls': [
                'https://www.tianyancha.com/sbid/17416832-066b', 'https://www.tianyancha.com/sbid/24614259-8180',
                'https://www.tianyancha.com/sbid/22440622-c479', 'https://www.tianyancha.com/sbid/26085742-8eaa',
                'https://www.tianyancha.com/sbid/24509193-317e', 'https://www.tianyancha.com/sbid/2349720591-17ff',
                'https://www.tianyancha.com/sbid/2316088447-2beb',
            ]
        },
    },
    'qianlima': {
        'class1': {
            'selecter': {'title': 'div.con-top > p:nth-child(1) > a', 'time': 'div.con-top > p:nth-child(3)'},
            'urls': [
                'http://www.qianlima.com/caizhao_1006552/', 'http://www.qianlima.com/caizhao_875454/',
                'http://www.qianlima.com/caizhao_933989/', 'http://www.qianlima.com/caizhao_1285966/',
                'http://www.qianlima.com/caizhao_793869/', 'http://www.qianlima.com/caizhao_1244973/',
                'http://www.qianlima.com/gjxx/196167/index.html', 'http://www.qianlima.com/gjxx/276936/index.html',
                'http://www.qianlima.com',
            ]
        },
    },
    'cpic': {
        'class1': {
            'selecter': {'title': 'div.left > div:nth-child(1) > div.m-list > li > a > span.bidLink',
                         'time': 'div.left > div:nth-child(1) > div.m-list > li > a > span.bidDate',
                         'url': 'div.left > div:nth-child(1) > div.m-list > li > a'},
            'urls': [
                'http://purchase.cpic.com.cn/cms/',
            ]
        },
    },
    'echinalife': {
        'class1': {
            'selecter': {'title': '#WorkAreaContent3 > div > ul > li > a', 'time': '#WorkAreaContent3 > div > ul > li > span.right'},
            'urls': [
                'http://cpmsx.e-chinalife.com/xycms/',
            ]
        },
    },
    'bao361': {
        'class1': {
            'selecter': {'title': 'div.layui-col-md8 > div > article > header > h2 > a',
                         'time': 'div.layui-col-md8 > div > article > p > span:nth-child(1)'},
            'urls': [
                'https://www.bao361.cn/toutiao/133989/',
            ]
        },
    },
    'bidchance': {
        'class1': {
            'selecter': {'title': 'li > span.qypdqyxlconr-qyxx-spanl > a:nth-child(2)', 'time': 'li > span.qypdqyxlconr-qyxx-spanr'},
            'urls': [
                'https://www.bidchance.com/company-375814.html',
                'https://www.bibenet.com/'
            ]
        },
    },
    'job592': {
        'class1': {
            'selecter': {'title': 'div.artlist > div > h2 > a', 'time': 'div.artlist > div > p.afoot > span:nth-child(2)'},
            'urls': [
                'https://www.job592.com/zb/yz/33393.html', 'http://www.ztb365.cn/',
                'www.365trade.com.cn', 'https://www.shabidding.com',
                'https://tendering.sinosteel.com/zgzb/',

            ]
        },
    },
    'cfcpn': {
        'class1': {
            'selecter': {'title': ''}
        }
    }
    }
