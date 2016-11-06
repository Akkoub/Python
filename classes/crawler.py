# coding=utf-8
# Crawler
import requests
from bs4 import BeautifulSoup
from urlparse import urljoin


class MyCrawler(object):
    # save new links found in page here
    links_to_crawl = []
    # save crawled links here
    crawled_links = []
    # save crawling text here
    data = ""

    def __init__(self, start_url):
        """
        class constructor which appends the start url to the crawler and start crawling
        :param start_url:
        """
        self.links_to_crawl.append(start_url)
        self.start_crawling()

    def start_crawling(self):
        """
        recurseive function ends when the links_to_crawl list is empty
        :return: True when the crawler finishes
        """
        if self.links_to_crawl:
            self.crawl_page(self.links_to_crawl.pop())
            return self.start_crawling()
        else:
            return True

    def crawl_page(self, link):
        """
        Start Crawling a single page
        :param link: url to be crawled
        :return:
        """
        print("crawling " + str(link))
        self.crawled_links.append(link)
        request = requests.get(link)
        soup = BeautifulSoup(request.content, 'html.parser')
        self.add_page_links(soup, link)
        self.add_page_data(soup)

    def add_page_links(self, soup, current_page_url):
        """
        search and append links found on the page to the links_to_crawl
        variable only if the link has not been crawled before
        :param soup:html parsed content from the request
        :param current_page_url: the current page we are crawling used to solve the relative uri's
        :return:
        """
        link_tds = soup.findAll("td", {"class": "تبويب"})
        for link_td in link_tds:
            for link in link_td.findAll("a"):
                link_url = urljoin(current_page_url, link.get("href"))
                if link_url not in self.links_to_crawl and link_url not in self.crawled_links:
                    print(link_url)
                    self.links_to_crawl.append(link_url)

    def add_page_data(self, soup):
        """
        search and append texts found on the page to the data string
        :param soup:html parsed content from the request
        :return:
        """
        data_divs = soup.findAll("div", {"class": "degrade"})
        for item in data_divs:
            self.data += item.text.encode('utf-8')

    def save__datato_file(self):
        """
        Save the crawler result to a text file
        :return:
        """
        file = open('CrawlerFile.txt', 'w')
        file.write(self.data)
        file.close()
