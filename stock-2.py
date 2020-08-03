import pandas as pd
dfs=pd.read_html('https://www.cnyes.com/twstock/index2real.aspx?stockType=T&groupId=22&stitle=%e7%94%9f%e6%8a%80')
print(dfs[0])