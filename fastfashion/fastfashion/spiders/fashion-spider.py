import re
import string
import scrapy
from fastfashion.items import FastfashionItem
from twisted.internet import reactor
from twisted.internet.defer import Deferred
import requests


class BaseSpider(scrapy.Spider):
    page = 1
    def create_item(self):
        item = FastfashionItem()
        return item 
        
    def parse(self, response):
        """This method should be overridden by subclasses to define how items are parsed"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def parse_item(self, response):
        """This method should be overridden by subclasses to define how items are parsed"""
        raise NotImplementedError("Subclasses must implement this method")
    
    '''
    def navigation_links(self, response):
        """Method for navigating the pages on the website"""
        raise NotImplementedError("Subclass must implement this method")
    '''
        

class JDSportSpider(BaseSpider):
    name = 'jdsport'
    start_urls = ['https://www.jdsports.co.uk/men/mens-footwear/','https://www.jdsports.co.uk/women/womens-footwear/']

    
    def parse(self, response):
        product_list = response.xpath('/html/body/div[1]/div[3]/div[3]/div[2]/div[1]/div/ul/li')
        for product in product_list:
            product = product.xpath('.//span/a/@href').get()
            link = f"https://www.jdsports.co.uk{product}"
            yield response.follow(link, callback=self.parse_item)
        yield from self.navigation_links(response)
        
        
    def navigation_links(self, response):
        page_links = response.xpath('//*[@id="productListPagination"]/div[1]/div[1]/a')
        print(page_links)
        for page in page_links:
            page_number = page.xpath('.//@href').get()
            link = f"https://www.jdsports.co.uk{page_number}"
            yield response.follow(link, callback=self.parse)
        
    
    def get_images(self, containers, img_element):
        images = []
        for idx, container in enumerate(containers):
            images.append(container.xpath(img_element).get().split(',')[2].strip()[:-3])
            #print('############################')
        return images
        
    def parse_item(self, response):
        item = self.create_item()
        name = response.xpath('//h1/text()').get()
        price = response.xpath('//*[@id="productItemTitle"]/div[1]/span/text()').get()
        imagescontainer = response.xpath('//*[@id="multiImageContainer"]/ul/li')
        images = self.get_images(imagescontainer, './/picture/source/@srcset')
        url = response.xpath('//*[@id="breads"]/div/span[5]/a/@href').get()
        url = f"https://www.jdsports.co.uk{url}"
        retailer = 'JD Sport'
        gender = response.xpath('//*[@id="breads"]/div/span[3]/a/span/text()').get()
        category = 'Footwear'
        brand = name.split()[0]
        item['name'] = name
        item['price'] = price
        item['url'] = url
        item['images'] = images
        item['retailer'] = retailer
        item['category'] = category
        item['gender'] = gender
        item['brand'] = brand
        yield item
        
        
class Kickgame(BaseSpider):
    name = 'kickgame'
    start_urls = ['https://www.kickgame.co.uk/collections/sneakers?page=1']
    def parse(self, response):
        product_list = response.xpath('//*[@id="product-grid"]/li')
        
        # If no products are found, stop pagination
        if not product_list:
            self.logger.info(f"No products found on page {self.page}. Stopping pagination.")
            return
        
        #If products are found then parse
        for product in product_list:
            yield self.parse_item(product)
    
        
        #navigate to next page
        self.page += 1
        next_page = self.start_urls[0][:-1] + str(self.page)
        yield from self.navigation_links(response, next_page)
        
    def navigation_links(self, response, next_page):
        # Generate a request for the next page and follow it
        if next_page:
            print(f"Following: {next_page}")
            yield scrapy.Request(next_page, callback=self.parse)
    
    def parse_item(self, response):
        name = response.xpath('.//h3/text()').get().strip()
        price = response.xpath('.//a/div/div[2]/div/div[1]/div[2]/span[2]/text()').get()
        retailer = 'Kick Game'
        category = 'Footwear'
        gender = 'Womens Footwear' if name.lower().__contains__('wmns') else 'Mens Footwear'
        url = 'https://www.kickgame.co.uk/collections/sneakers'+ response.xpath('.//a/@href').get()
        images = response.xpath('.//img/@src').get()
        item = self.create_item()
        brand = None
        
        item['name'] = name
        item['price'] = price
        item['url'] = url
        item['images'] = images
        item['retailer'] = retailer
        item['category'] = category
        item['gender'] = gender
        item['brand'] = brand
        
        return item
        


class SACSpider(scrapy.Spider):
    name = 'sac'
    start_urls = ['https://digital.nhs.uk/data-and-information/publications/statistical/safeguarding-adults']
    
    def parse(self, response):
        _ = response.xpath('//*[@id="callout-box-heading-interactive-grey-latest-publication"]/h3/a/@href').get()
        
        yield response.follow(_, callback=self.test)
    
    def test(self, response):
        url = response.xpath('//*[@id="resources"]/div/div[2]/div/a/@href').get()
        response = requests.get(url)
        with open('sacraw.csv', 'wb') as f:
            f.write(response.content)
        
    def save_file(self, response):
        with open('test', 'wb') as f:
            f.write(response.body)
        
        
        
        
    
