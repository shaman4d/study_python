from bs4 import BeautifulSoup
import requests
import re
import urllib
import os
import logging
import time
import sys

MAX_TOPICS = 1000000
MAX_SEARCHING_SEQUENCES = 10
APP_LOG_PATH = 'app.log'
DATASET_PATH = 'i:/datasets/wikipages/'
BASE_WIKI_PATH = 'https://en.wikipedia.org/wiki/'

# ----------------------------------------------------------------------------

class TopicVO:
    def __init__(self, parentTopic, topicName):
        self.parent = parentTopic
        self.name = topicName

# ----------------------------------------------------------------------------
def getWikiTopic(topicName):
    topicFilename = os.path.join(DATASET_PATH, f"{topicName}.html")
    if os.path.exists(topicFilename):
        with open(topicFilename, 'rb') as f:
            return f.read()

    time.sleep(0.1)
    url = urllib.parse.urljoin(BASE_WIKI_PATH, topicName)
    print(f'...loading {url}...')
    response = requests.get(url, timeout=5)
    if response is None:
        print('Error: got nothing')
        return None
    if response.status_code != 200:
        print('Error: status code {}'.format(response.status_code))
        logging.error('url={} code:{}'.format(url, response.status_code))
        if response.status_code == 404:
            with open(topicFilename, 'wb') as f:
                f.write(b'')
        return None
    with open(topicFilename, 'wb') as f:
        f.write(response.content)
    return response.content


def processingTopic(topicVO):
    newTopics = []
    topicIdxFilename = os.path.join(DATASET_PATH, f"{topicVO.name}.idx")
    if os.path.exists(topicIdxFilename):
        with open(topicIdxFilename,'r') as f:
            topics = f.readline().split(',')
            for t in topics:
                newTopics.append(TopicVO(topicVO, t))
    else:
        print(f'........processing >>> {topicVO.name}')
        wikiContent = getWikiTopic(topicVO.name)
        if wikiContent is None or wikiContent == b'': return None
        bs = BeautifulSoup(wikiContent, features='html.parser')
        bodyContent= bs.find('div', {'id':'content'})
        contentLinks = bodyContent.findAll('a', href = re.compile("^(/wiki/)((?!(:|#)).)*$"))
        topics = []
        for a in contentLinks:
            if 'href' in a.attrs:
                if '#' in a.attrs['href']:
                    continue
                newTopicName = a.attrs['href'].split('/')[2]
                newTopics.append(TopicVO(topicVO,newTopicName))
                topics.append(newTopicName)
        with open(topicIdxFilename,'w') as f:
            f.write(','.join(topics))
    return newTopics

def startCrowling():
    print('Begin to work {} -> {}'.format(startTopicName, endTopicName))
    logging.info('Begin to work {} -> {}'.format(startTopicName, endTopicName))
    currentTopicNumber = 0
    processedTopics = []
    topics = [TopicVO(None,startTopicName)]
    while len(topics) and currentTopicNumber < MAX_TOPICS:
        currentTopic = topics.pop(0)
        newTopics = None
        if currentTopic.name not in processedTopics:
            newTopics = processingTopic(currentTopic)
            processedTopics.append(currentTopic.name)
        if newTopics is not None:
            currentTopicNumber += 1
            for topic in newTopics:
                if endTopicName == topic.name:
                    print(f'\nEnd topic {endTopicName} have been found. {currentTopicNumber} topics have beed processed for.')
                    topicRoute = []
                    backTopic = topic
                    while True:
                        topicRoute.append(backTopic.name)
                        if backTopic.parent is not None:
                            backTopic = backTopic.parent
                        else:
                            break
                    # global seqs
                    # seqs.append(topicRoute)
                    topicRoute.reverse()
                    print(' > '.join(topicRoute))
                    logging.info(' > '.join(topicRoute))
                    # return
            topics += newTopics

# ----------------------------------------------------------------------------


if os.path.exists(APP_LOG_PATH):
    os.remove(APP_LOG_PATH)

logging.basicConfig(filename=APP_LOG_PATH, filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

seqs = []

startTopicName = 'Lenin'
endTopicName = 'Burrito'

if len(sys.argv) > 1:
    startTopicName = sys.argv[1]
if len(sys.argv) > 2:
    endTopicName = sys.argv[2]

startTime = time.time()
startCrowling()
print('Operation has taken {} seconds'.format(time.time() - startTime))
