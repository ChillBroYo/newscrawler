scrapy crawl bbc -o ../bbc-news/bbc-processed/bbc.$(date "+%Y.%m.%d-%H.%M.%S").json
scrapy crawl bzfd -o ../bzfd-news/bzfd-processed/bzfd.$(date "+%Y.%m.%d-%H.%M.%S").json
scrapy crawl alj -o ../alj-news/alj-processed/alj.$(date "+%Y.%m.%d-%H.%M.%S").json
