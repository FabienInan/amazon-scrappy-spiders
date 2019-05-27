from flask import Flask, request, jsonify
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
#from amazonReviewsSpider import AmazonReviewsSpider
import subprocess
import os

import json

app = Flask(__name__)

results = []
@app.route('/reviews/')
def get_data():
        #runner = CrawlerRunner()
        #d = runner.crawl(AmazonReviewsSpider, id = id, results = results)
        #d.addBoth(lambda _: reactor.stop())
        #reactor.run()
        # return(json.dumps(results))
        id = request.args.get('id')
        os.system('rm output.json')
        os.system('touch output.json')
        print(id)
        subprocess.call(['scrapy', 'runspider', "/app/skeleton_app/amazonReviewsSpider.py", "-a", "id=" + id, "-o", "output.json"])
        with open("output.json") as items_file:
                return items_file.read()

if __name__ == '__main__':
    app.run(debug=True)
