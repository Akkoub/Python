import getopt, sys

from classes.crawler import MyCrawler
from classes.words_mapping import WordMapper


def main():
    try:
        arg = sys.argv[1]
        print arg
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    if arg == "crawl":
        my_crawler = MyCrawler(
            "https://ar.wikipedia.org/wiki/%D8%A8%D9%88%D8%A7%D8%A8%D8%A9:%D8%A7%D9%84%D8%A3%D8%AF%D9%8A%D8%A7%D9%86")
        my_crawler.save__datato_file()
    elif arg == "map":
        words_mapping = WordMapper()
        words_mapping.print_results()
    else:
        print "pass map or crawl"


if __name__ == "__main__": main()
