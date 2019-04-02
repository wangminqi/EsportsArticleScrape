import plugins
import pandas as pd
import re



target_file_path = r'C:\Users\wangminqi\PycharmProjects\EsportsArticleScrape\excel_template\excel模板.xlsx'
df_dota2 = pd.read_excel(target_file_path, sheet_name=0)
df_lol = pd.read_excel(target_file_path, sheet_name=1)
df_csgo = pd.read_excel(target_file_path, sheet_name=2)
df_fn = pd.read_excel(target_file_path, sheet_name=3)
df_pubg = pd.read_excel(target_file_path, sheet_name=4)
df_apex = pd.read_excel(target_file_path, sheet_name=5)


for i in df_dota2.copy().index:
    df_dota2.loc[i, 'plugins'] = plugins.website_recognize(df_dota2.iloc[i]['标题链接'])

for i in df_lol.copy().index:
    df_lol.loc[i, 'plugins'] = plugins.website_recognize(df_lol.iloc[i]['标题链接'])

for i in df_csgo.copy().index:
    df_csgo.loc[i, 'plugins'] = plugins.website_recognize(df_csgo.iloc[i]['标题链接'])

for i in df_fn.copy().index:
    df_fn.loc[i, 'plugins'] = plugins.website_recognize(df_fn.iloc[i]['标题链接'])

for i in df_pubg.copy().index:
    df_pubg.loc[i, 'plugins'] = plugins.website_recognize(df_pubg.iloc[i]['标题链接'])

for i in df_apex.copy().index:
    df_apex.loc[i, 'plugins'] = plugins.website_recognize(df_apex.iloc[i]['标题链接'])

target_file_path = r'C:\Users\wangminqi\PycharmProjects\EsportsArticleScrape\excel_template\excel模板2.xlsx'
with pd.ExcelWriter(target_file_path) as writer:
    df_dota2.to_excel(writer, 'dota2')
    df_lol.to_excel(writer, 'lol')
    df_csgo.to_excel(writer, 'csgo')
    df_fn.to_excel(writer, 'fortnight')
    df_pubg.to_excel(writer, 'pubg')
    df_apex.to_excel(writer, 'apex')













