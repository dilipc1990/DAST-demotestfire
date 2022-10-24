def zap_pre_shutdown(zap):
  print(zap.spider.all_urls)
  print(zap.stats.site_stats("https://demo.testfire.net/"))
  print(zap.stats.stats)
