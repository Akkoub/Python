# coding=utf-8
# Crawler
import nltk
import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
from nltk import tokenize


class WordMapper(object):
    # save new links found in page here
    result = {}
    words = None
    count_words = 0

    def __init__(self):
        """
        class constructor which appends the start url to the crawler and start crawling
        :param start_url:
        """
        self.read_file()
        self.build_map()

    def read_file(self):
        """
        recurseive function ends when the links_to_crawl list is empty
        :return: True when the crawler finishes
        """
        file = open('CrawlerFile.txt', 'r')
        self.words = file.read().split()
        self.count_words = len(self.words)

    def build_map(self):

        for index, word in enumerate(self.words):
            if word not in self.result:
                self.result[word] = []
            if index < (self.count_words - 1):
                next_word = self.words[index + 1]
                self.result[word].append(next_word)

    def print_results(self):
        for key, value in self.result.iteritems():
            row =  '{0} => ['.format(key)
            for word in value:
                row +='{0}, '.format(word)
            print row + "]"
