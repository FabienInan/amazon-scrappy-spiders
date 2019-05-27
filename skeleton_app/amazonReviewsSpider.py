import scrapy

class AmazonReviewsSpider(scrapy.Spider):
    
    name = "amazonReviewsSpider"

    def __init__(self, *args, **kwargs):
        id = kwargs.pop('id', []) 
        if id:
            url = "https://www.amazon.ca/product-reviews/" + str(id) + "/?ie=UTF8&reviewerType=all_reviews&pageNumber="
            self.start_urls=[]
            for i in range(1,10):
                self.start_urls.append(url + str(i))
        super(AmazonReviewsSpider, self).__init__(*args, **kwargs)

    # Defining a Scrapy parser
    def parse(self, response):
        print(response)
        data = response.css('#cm_cr-review_list')
             
        # Collecting product star ratings
        star_rating = data.css('.review-rating')
             
        # Collecting user reviews
        comments = data.css('.review-text')
        count = 0
             
        # Combining the results
        for review in star_rating:
            self.results.append({
                'stars': ''.join(review.xpath('.//text()').extract()),
                'comment': ''.join(comments[count].xpath(".//text()").extract())
                })
            count=count+1

