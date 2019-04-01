
import pandas as pd
import re


def website_recognize(url):
    url = str(url)
    if url.find('http://pc.07073.com/') != -1:
        return '07073'
    # 07073
    # http://pc.07073.com
    # http://pc.07073.com/arc59454.html
    # http://pc.07073.com/arc59189.html

    if url.find('http://csgo.178.com/') != -1:
        return 'csgo178'
    # csgo178
    # http://csgo.178.com
    # http://csgo.178.com/201903/347837593834.html

    if url.find('https://www.csgo.com.cn/article/details/') != -1:
        return 'csgo_official'
    # csgo官网
    # https://www.csgo.com.cn/article/details
    # https://www.csgo.com.cn/article/details/20190321/213421.html

    if url.find('http://www.demaxiya.com/news/') != -1:
        return 'demaxiya'
    # 德玛西亚
    # http://www.demaxiya.com/news
    # http://www.demaxiya.com/news/20190399474.html

    if url.find('https://www.dota2.com.cn/article/details/') != -1:
        return 'dota2_official'
    # Dota2官网
    # https://www.dota2.com.cn/article/details
    # https://www.dota2.com.cn/article/details/20190306/202141.html

    if url.find('http://dota2.duowan.com/') != -1:
        return 'duowan_dota2'
    # 多玩 Dota2
    # http://dota2.duowan.com/
    # http://dota2.duowan.com/1709/369858520392.html

    if url.find('https://fn.qq.com/webplat/info/') != -1:
        return 'fn_qq'
    # 腾讯堡垒之夜
    # https://fn.qq.com
    # http://fn.qq.com/cp/a20190306missing/index.htm
    # https://fn.qq.com/webplat/info
    # https://fn.qq.com/webplat/info/news_version3/10021/34544/34545/m20913/201903/800110.shtml

    if url.find('https://www.gamersky.com/news/') != -1:
        return 'gamersky'
    # 游民星空
    # https://www.gamersky.com/news
    # https://www.gamersky.com/news/201903/1166223.shtml

    if url.find('http://csgo.gamersky.com/') != -1:
        return 'gamersky_csgo'
    # 游民星空 csgo
    # http://csgo.gamersky.com
    # http://csgo.gamersky.com/201901/1149198.shtml

    if url.find('https://www.gmz88.com/xinwen/') != -1:
        return 'gmz88'
    # 游戏吧
    # https://www.gmz88.com/xinwen
    # https://www.gmz88.com/xinwen/159760.html

    if url.find('https://lol.qq.com/news/detail.shtml?') != -1:
        return 'lol_qq'
    # lol官网
    # https://lol.dianjinghu.com/news
    # https://lol.dianjinghu.com/news/72669.html?docid=10853917297328644882
    # https://lol.qq.com/news/detail.shtml?
    # https://lol.qq.com/news/detail.shtml?docid=11704508428476250875
    # https://l.zhangyoubao.com/news/108659?docid=17957135356846687720
    # https://lol.duowan.com/1903/416398720150.html?docid=2017085560233605719
    # https://www.famulei.com/p/1013190?iframe=qq&docid=15301649744515833369
    # https://chijizs.uuu9.com/zt/lol/201903/590074.html?docid=17741698928880339963

    if url.find('http://fight.pcgames.com.cn/') != -1:
        return 'pcgames'
    # 太平洋
    # http://fight.pcgames.com.cn
    # http://fight.pcgames.com.cn/735/7351216.html

    if url.find('http://wy.pipaw.com/xinwen/') != -1:
        return 'pipaw'
    # 琵琶网
    # http://wy.pipaw.com/xinwen
    # http://wy.pipaw.com/xinwen/news441012.html

    if url.find('http://www.tuwan.com/game/') != -1:
        return 'tuwan'
    # 兔玩网
    # http://www.tuwan.com/game
    # http://www.tuwan.com/game/dota2/393688/

    if url.find('http://dota2.uuu9.com/') != -1:
        return 'u9_dota2'
    # 游久电竞 Dota2
    # http://dota2.uuu9.com/
    # http://dota2.uuu9.com/201903/589724.shtml
    # http://moba.uuu9.com/thread-4920490-1-1.html

    if url.find('http://lol.uuu9.com/') != -1:
        return 'u9_lol'
    # 游久电竞 LOL
    # http://lol.uuu9.com/
    # http://lol.uuu9.com/201903/591152.shtml
    # bbs.uuu9.com/
    # http://bbs.uuu9.com/thread-13046669-1-1.html?tdsourcetag=s_pcqq_aiomsg

    if url.find('https://www.wanplus.com/article/') != -1:
        return 'wanplus'
    # 玩加电竞
    # https://www.wanplus.com/article
    # https://www.wanplus.com/article/207915.html

    if url.find('http://www.ali213.net/news/html/') != -1:
        return 'youxia'
    # 游侠网
    # http://www.ali213.net/news/html
    # http://www.ali213.net/news/html/2019-2/411461.html

    if url.find('http://3g.ali213.net/news/html/') != -1:
        return 'youxia_3g'
    # 游侠网_3g
    # http://3g.ali213.net/news/html/417615.html
    # http://in.ali213.net/news/201902/6346.html

    return 'NA'


target_file_path = r'C:\Users\wangminqi\PycharmProjects\EsportsArticleScrape\excel_template\excel模板.xlsx'
df_dota2 = pd.read_excel(target_file_path, sheet_name=0)
df_lol = pd.read_excel(target_file_path, sheet_name=1)
df_csgo = pd.read_excel(target_file_path, sheet_name=2)
df_fn = pd.read_excel(target_file_path, sheet_name=3)
df_pubg = pd.read_excel(target_file_path, sheet_name=4)
df_apex = pd.read_excel(target_file_path, sheet_name=5)


for i in df_dota2.copy().index:
    df_dota2.loc[i, 'plugins'] = website_recognize(df_dota2.iloc[i]['标题链接'])

for i in df_lol.copy().index:
    df_lol.loc[i, 'plugins'] = website_recognize(df_lol.iloc[i]['标题链接'])

for i in df_csgo.copy().index:
    df_csgo.loc[i, 'plugins'] = website_recognize(df_csgo.iloc[i]['标题链接'])

for i in df_fn.copy().index:
    df_fn.loc[i, 'plugins'] = website_recognize(df_fn.iloc[i]['标题链接'])

for i in df_pubg.copy().index:
    df_pubg.loc[i, 'plugins'] = website_recognize(df_pubg.iloc[i]['标题链接'])

for i in df_apex.copy().index:
    df_apex.loc[i, 'plugins'] = website_recognize(df_apex.iloc[i]['标题链接'])

target_file_path = r'C:\Users\wangminqi\PycharmProjects\EsportsArticleScrape\excel_template\excel模板2.xlsx'
with pd.ExcelWriter(target_file_path) as writer:
    df_dota2.to_excel(writer, 'dota2')
    df_lol.to_excel(writer, 'lol')
    df_csgo.to_excel(writer, 'csgo')
    df_fn.to_excel(writer, 'fortnight')
    df_pubg.to_excel(writer, 'pubg')
    df_apex.to_excel(writer, 'apex')


