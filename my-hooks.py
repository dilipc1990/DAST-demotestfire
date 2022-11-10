def zap_pre_shutdown(zap):
  for url in zap.spider.all_urls:
    print(url)
  
  print(zap.spider.state.loggedin('https://demo.testfire.net'))
