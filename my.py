import twint
 
# 获取所有蔡英文的推文
c = twint.Config()
c.Username = "iingwen"
c.Limit=3 # 最大获取
 
# 代理设置
c.Proxy_host='127.0.0.1'
c.Proxy_port=10808
c.Proxy_type='socks5'
 
c.Since = '2021-01-01'
c.Until = '2021-03-01'
 
c.Translate = True
c.TranslateDest = "zh-TW"
 
# 导出文件
c.Store_csv = True
c.Output='output/'+c.Username+'_zhTW.csv'
twint.run.Search(c)
