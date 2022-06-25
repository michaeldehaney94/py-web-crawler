# this application will be carrying out multiple task
import threading
from queue import Queue
from savedata import *
from spider import Spider
from domain import *
from demo import *

PROJECT_NAME = 'WebCrawler'
HOMEPAGE = 'https://michaeldehaney94.github.io/photographywebsite/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue.')
        create_jobs()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        crawl()


# creating multithreading workers that will process data
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.currentThread().name, url)
        queue.task_done()


# function calls to start crawling and multi-threading
create_workers()
crawl()
