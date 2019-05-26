from flask import Flask, request, jsonify
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from amazonReviewsSpider import AmazonReviewsSpider

import json

app = Flask(__name__)

spiders = ['amazonReviewsSpider']
results = []
@app.route('/reviews/')
def get_data():
        id = request.args.get('id')
        runner = CrawlerRunner()
        d = runner.crawl(AmazonReviewsSpider, id = id, results = results)
        d.addBoth(lambda _: reactor.stop())
        reactor.run()
        print(results)
        return(json.dumps(results))

if __name__ == '__main__':
    app.run(debug=True)