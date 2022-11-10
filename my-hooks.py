def zap_pre_shutdown(zap):
  #for url in zap.spider.all_urls:
    #print(url)
  
  print(zap.stats.site_stats('https://demo.testfire.net'))
