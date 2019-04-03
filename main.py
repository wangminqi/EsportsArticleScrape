#import plugins
import plugins.youxia.ArticleScrape
import pandas as pd
import re
from docx import Document


def Scrape_main(df, game_category):
    for i in df.copy().index:
        df.loc[i, 'plugins'] = plugins.website_recognize(df.loc[i]['标题链接'])
    document = Document()
    document.add_heading('Document Title', 0)
    for i in df.copy().index:
        url = df.loc[i, '标题链接']
        plugin = df.loc[i, 'plugins']
        if plugin != 'N/A':
            loc = locals()
            exec("response = plugins.{}.ArticleScrape.collect_raw_content(url)".format(plugin))
            response = loc['response']
            exec("target = plugins.{}.ArticleScrape.refine_content(response)".format(plugin))
            target = loc['target']
            if target is None:
                df.loc[i, 'results'] = '网址结构特殊，请联系数据部'
            else:
                exec("document = plugins.{}.ArticleScrape.document_append(document, target, url)".format(plugin))
                df.loc[i, 'results'] = '完成'
        else:
            df.loc[i, 'results'] = '网址无法解析，如确认网址内容有效，请联系数据部'

    document.save('.\运营使用\\' + game_category + '.docx')
    return df


target_file_path = r'.\运营使用\excel输入url.xlsx'
df_dota2 = pd.read_excel(target_file_path, sheet_name=0)
df_lol = pd.read_excel(target_file_path, sheet_name=1)
df_csgo = pd.read_excel(target_file_path, sheet_name=2)
df_fn = pd.read_excel(target_file_path, sheet_name=3)
df_pubg = pd.read_excel(target_file_path, sheet_name=4)
df_apex = pd.read_excel(target_file_path, sheet_name=5)

df_dota2 = Scrape_main(df_dota2, 'dota2')
df_lol = Scrape_main(df_lol, 'lol')
df_csgo = Scrape_main(df_csgo, 'csgo')
df_fn = Scrape_main(df_fn, 'fortnight')
df_pubg = Scrape_main(df_pubg, 'pubg')
df_apex = Scrape_main(df_apex, 'apex')

target_file_path = r'.\运营使用\excel结果.xlsx'
with pd.ExcelWriter(target_file_path) as writer:
    df_dota2.to_excel(writer, 'dota2')
    df_lol.to_excel(writer, 'lol')
    df_csgo.to_excel(writer, 'csgo')
    df_fn.to_excel(writer, 'fortnight')
    df_pubg.to_excel(writer, 'pubg')
    df_apex.to_excel(writer, 'apex')




