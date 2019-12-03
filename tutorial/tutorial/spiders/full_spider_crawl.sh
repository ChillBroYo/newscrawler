scrapy crawl bbc -o ../bbc-news/bbc-processed/bbc.$(date +"%Y.%m.%d" | sed "s/^0*//g; s/\.0*/./g").json
scrapy crawl bzfd -o ../bzfd-news/bzfd-processed/bzfd.$(date +"%Y.%m.%d" | sed "s/^0*//g; s/\.0*/./g").json
scrapy crawl alj -o ../alj-news/alj-processed/alj.$(date +"%Y.%m.%d" | sed "s/^0*//g; s/\.0*/./g").json
scrapy crawl alj -o ../fox-news/fox-processed/alj.$(date +"%Y.%m.%d" | sed "s/^0*//g; s/\.0*/./g").json
