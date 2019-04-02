plugins_url_prefix = {'csgo178': 'http://csgo.178.com/',
                      'csgo_official': 'https://www.csgo.com.cn/article/details/',
                      'demaxiya': 'http://www.demaxiya.com/news/',
                      'dota2_official': 'https://www.dota2.com.cn/article/details/',
                      'duowan_dota2': 'http://dota2.duowan.com/',
                      'fn_qq': 'https://fn.qq.com/webplat/info/',
                      'gamersky': 'https://www.gamersky.com/news/',
                      'gamersky_csgo': 'http://csgo.gamersky.com/',
                      'gmz88': 'https://www.gmz88.com/xinwen/',
                      'lol_qq': 'https://lol.qq.com/news/detail.shtml?',
                      'pc07073': 'http://pc.07073.com/',
                      'pcgames': 'http://fight.pcgames.com.cn/',
                      'pipaw': 'http://wy.pipaw.com/xinwen/',
                      'tuwan': 'http://www.tuwan.com/game/',
                      'u9_dota2': 'http://dota2.uuu9.com/',
                      'u9_lol': 'http://lol.uuu9.com/',
                      'wanplus': 'https://www.wanplus.com/article/',
                      'youxia': 'http://www.ali213.net/news/html/',
                      'youxia_3g': 'http://3g.ali213.net/news/html/'}
plugins_list = [#'csgo178',
                #'csgo_official',
                #'demaxiya',
                #'dota2_official',
                #'duowan_dota2',
                #'fn_qq',
                #'gamersky',
                #'gamersky_csgo',
                #'gmz88',
                #'lol_qq',
                #'pc07073',
                #'pcgames',
                #'pipaw',
                #'tuwan',
                #'u9_dota2',
                #'u9_lol',
                #'wanplus',
                'youxia']
#                'youxia_3g']
# for i in range(len(plugins_list)):
#     exec('import {}.ArticleScrape'.format(plugins_list[i]))


def website_recognize(url):
    url = str(url)
    for i in plugins_list:
        if url.find(plugins_url_prefix[i]) != -1:
            return i
    return 'N/A'
    # csgo178
    # http://csgo.178.com
    # http://csgo.178.com/201903/347837593834.html

    # csgo官网
    # https://www.csgo.com.cn/article/details
    # https://www.csgo.com.cn/article/details/20190321/213421.html

    # 德玛西亚
    # http://www.demaxiya.com/news
    # http://www.demaxiya.com/news/20190399474.html

    # Dota2官网
    # https://www.dota2.com.cn/article/details
    # https://www.dota2.com.cn/article/details/20190306/202141.html

    # 多玩 Dota2
    # http://dota2.duowan.com/
    # http://dota2.duowan.com/1709/369858520392.html

    # 腾讯堡垒之夜
    # https://fn.qq.com
    # http://fn.qq.com/cp/a20190306missing/index.htm
    # https://fn.qq.com/webplat/info
    # https://fn.qq.com/webplat/info/news_version3/10021/34544/34545/m20913/201903/800110.shtml

    # 游民星空
    # https://www.gamersky.com/news
    # https://www.gamersky.com/news/201903/1166223.shtml

    # 游民星空 csgo
    # http://csgo.gamersky.com
    # http://csgo.gamersky.com/201901/1149198.shtml

    # 游戏吧
    # https://www.gmz88.com/xinwen
    # https://www.gmz88.com/xinwen/159760.html

    # lol官网
    # https://lol.dianjinghu.com/news
    # https://lol.dianjinghu.com/news/72669.html?docid=10853917297328644882
    # https://lol.qq.com/news/detail.shtml?
    # https://lol.qq.com/news/detail.shtml?docid=11704508428476250875
    # https://l.zhangyoubao.com/news/108659?docid=17957135356846687720
    # https://lol.duowan.com/1903/416398720150.html?docid=2017085560233605719
    # https://www.famulei.com/p/1013190?iframe=qq&docid=15301649744515833369
    # https://chijizs.uuu9.com/zt/lol/201903/590074.html?docid=17741698928880339963

    # 07073
    # http://pc.07073.com
    # http://pc.07073.com/arc59454.html
    # http://pc.07073.com/arc59189.html

    # 太平洋
    # http://fight.pcgames.com.cn
    # http://fight.pcgames.com.cn/735/7351216.html

    # 琵琶网
    # http://wy.pipaw.com/xinwen
    # http://wy.pipaw.com/xinwen/news441012.html

    # 兔玩网
    # http://www.tuwan.com/game
    # http://www.tuwan.com/game/dota2/393688/

    # 游久电竞 Dota2
    # http://dota2.uuu9.com/
    # http://dota2.uuu9.com/201903/589724.shtml
    # http://moba.uuu9.com/thread-4920490-1-1.html

    # 游久电竞 LOL
    # http://lol.uuu9.com/
    # http://lol.uuu9.com/201903/591152.shtml
    # bbs.uuu9.com/
    # http://bbs.uuu9.com/thread-13046669-1-1.html?tdsourcetag=s_pcqq_aiomsg

    # 玩加电竞
    # https://www.wanplus.com/article
    # https://www.wanplus.com/article/207915.html

    # 游侠网
    # http://www.ali213.net/news/html
    # http://www.ali213.net/news/html/2019-2/411461.html

    # 游侠网_3g
    # http://3g.ali213.net/news/html/417615.html
    # http://in.ali213.net/news/201902/6346.html


