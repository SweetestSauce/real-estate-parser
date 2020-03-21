# RealEstateParser
A tool to parse FrankSalt website
## Getting started
Run ```scrapy crawl franksalt```.
It is also possible to pass a "url" argument to the spider:
```scrapy crawl -a url=<url> franksalt```
Output is written to "result.json" file inside the directory from where the spider is ran