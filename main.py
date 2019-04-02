import plugins
import pandas as pd
import re
from docx import Document



target_file_path = r'C:\Users\wangminqi\PycharmProjects\EsportsArticleScrape\excel_template\excel模板.xlsx'
df_dota2 = pd.read_excel(target_file_path, sheet_name=0)
df_lol = pd.read_excel(target_file_path, sheet_name=1)
df_csgo = pd.read_excel(target_file_path, sheet_name=2)
df_fn = pd.read_excel(target_file_path, sheet_name=3)
df_pubg = pd.read_excel(target_file_path, sheet_name=4)
df_apex = pd.read_excel(target_file_path, sheet_name=5)


for i in df_dota2.copy().index:
    df_dota2.loc[i, 'plugins'] = plugins.website_recognize(df_dota2.loc[i]['标题链接'])

for i in df_lol.copy().index:
    df_lol.loc[i, 'plugins'] = plugins.website_recognize(df_lol.loc[i]['标题链接'])

for i in df_csgo.copy().index:
    df_csgo.loc[i, 'plugins'] = plugins.website_recognize(df_csgo.loc[i]['标题链接'])

for i in df_fn.copy().index:
    df_fn.loc[i, 'plugins'] = plugins.website_recognize(df_fn.loc[i]['标题链接'])

for i in df_pubg.copy().index:
    df_pubg.loc[i, 'plugins'] = plugins.website_recognize(df_pubg.loc[i]['标题链接'])

for i in df_apex.copy().index:
    df_apex.loc[i, 'plugins'] = plugins.website_recognize(df_apex.loc[i]['标题链接'])

document = Document()
document.add_heading('Document Title', 0)
for i in df_dota2.copy().index:
    url = df_dota2.loc[i, '标题链接']
    plugin = df_dota2.loc[i, 'plugins']
    if plugin != 'N/A':
        exec("response = plugins.{}.ArticleScrape.collect_raw_content(df_apex.loc[i, '标题链接'])".format(plugin))
        exec("target = plugins.{}.ArticleScrape.refine_content(response)".format(plugin))
        exec("plugins.{}.ArticleScrape.document_append(document, target, url)".format(plugin))
        df_dota2.loc[i, 'results'] = '完成'
    else:
        df_dota2.loc[i, 'results'] = '网址无法解析，如确认网址内容有效，请联系技术'

document.save('dota2.docx')

document = Document()
document.add_heading('Document Title', 0)
for i in df_lol.copy().index:
    url = df_lol.loc[i, '标题链接']
    plugin = df_lol.loc[i, 'plugins']
    if plugin != 'N/A':
        exec("response = plugins.{}.ArticleScrape.collect_raw_content(df_apex.loc[i, '标题链接'])".format(plugin))
        exec("target = plugins.{}.ArticleScrape.refine_content(response)".format(plugin))
        exec("plugins.{}.ArticleScrape.document_append(document, target, url)".format(plugin))
        df_lol.loc[i, 'results'] = '完成'
    else:
        df_lol.loc[i, 'results'] = '网址无法解析，如确认网址内容有效，请联系技术'

document.save('lol.docx')

document = Document()
document.add_heading('Document Title', 0)
for i in df_csgo.copy().index:
    url = df_csgo.loc[i, '标题链接']
    plugin = df_csgo.loc[i, 'plugins']
    if plugin != 'N/A':
        exec("response = plugins.{}.ArticleScrape.collect_raw_content(df_apex.loc[i, '标题链接'])".format(plugin))
        exec("target = plugins.{}.ArticleScrape.refine_content(response)".format(plugin))
        exec("plugins.{}.ArticleScrape.document_append(document, target, url)".format(plugin))
        df_csgo.loc[i, 'results'] = '完成'
    else:
        df_csgo.loc[i, 'results'] = '网址无法解析，如确认网址内容有效，请联系技术'

document.save('csgo.docx')

document = Document()
document.add_heading('Document Title', 0)
for i in df_fn.copy().index:
    url = df_fn.loc[i, '标题链接']
    plugin = df_fn.loc[i, 'plugins']
    if plugin != 'N/A':
        exec("response = plugins.{}.ArticleScrape.collect_raw_content(df_apex.loc[i, '标题链接'])".format(plugin))
        exec("target = plugins.{}.ArticleScrape.refine_content(response)".format(plugin))
        exec("plugins.{}.ArticleScrape.document_append(document, target, url)".format(plugin))
        df_fn.loc[i, 'results'] = '完成'
    else:
        df_fn.loc[i, 'results'] = '网址无法解析，如确认网址内容有效，请联系技术'

document.save('fortnight.docx')

document = Document()
document.add_heading('Document Title', 0)
for i in df_pubg.copy().index:
    url = df_pubg.loc[i, '标题链接']
    plugin = df_pubg.loc[i, 'plugins']
    if plugin != 'N/A':
        exec("response = plugins.{}.ArticleScrape.collect_raw_content(df_apex.loc[i, '标题链接'])".format(plugin))
        exec("target = plugins.{}.ArticleScrape.refine_content(response)".format(plugin))
        exec("plugins.{}.ArticleScrape.document_append(document, target, url)".format(plugin))
        df_pubg.loc[i, 'results'] = '完成'
    else:
        df_pubg.loc[i, 'results'] = '网址无法解析，如确认网址内容有效，请联系技术'

document.save('pubg.docx')

document = Document()
document.add_heading('Document Title', 0)
for i in df_apex.copy().index:
    url = df_apex.loc[i, '标题链接']
    plugin = df_apex.loc[i, 'plugins']
    if plugin != 'N/A':
        exec("response = plugins.{}.ArticleScrape.collect_raw_content(df_apex.loc[i, '标题链接'])".format(plugin))
        exec("target = plugins.{}.ArticleScrape.refine_content(response)".format(plugin))
        exec("plugins.{}.ArticleScrape.document_append(document, target, url)".format(plugin))
        df_apex.loc[i, 'results'] = '完成'
    else:
        df_apex.loc[i, 'results'] = '网址无法解析，如确认网址内容有效，请联系技术'

document.save('apex.docx')




target_file_path = r'C:\Users\wangminqi\PycharmProjects\EsportsArticleScrape\excel_template\excel模板2.xlsx'
with pd.ExcelWriter(target_file_path) as writer:
    df_dota2.to_excel(writer, 'dota2')
    df_lol.to_excel(writer, 'lol')
    df_csgo.to_excel(writer, 'csgo')
    df_fn.to_excel(writer, 'fortnight')
    df_pubg.to_excel(writer, 'pubg')
    df_apex.to_excel(writer, 'apex')













