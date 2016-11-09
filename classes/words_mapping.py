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
        class constructor which read the text file in starter the mapper
        """
        self.read_file()
        self.build_map()

    def read_file(self):
        """
        open the text file and store it as a word list
        """
        file = open('CrawlerFile.txt', 'r')
        self.words = file.read().split()
        self.count_words = len(self.words)

    def build_map(self):
        """
        :return:
        """

        for index, word in enumerate(self.words):
            if word not in self.result:
                self.result[word] = []
            if index < (self.count_words - 1):
                next_word = self.words[index + 1]
                self.result[word].append(next_word)

    def get_previews_words(self, word):
        found_words = (key for key, vals in self.result.items() if word in vals)
        return found_words

    def print_results(self):
        """
        output the mapper result to the console
        :return:
        """
        print "The total words count is: {0}".format(self.count_words)
        print "The total key words count is: {0}".format(len(self.result))
        for key, value in self.result.iteritems():
            row = '['
            for word in self.get_previews_words(key):
                row += '{0}, '.format(word)
            row += '] <= {0} => ['.format(key)
            for word in value:
                row += '{0}, '.format(word)
            print row + "]"
