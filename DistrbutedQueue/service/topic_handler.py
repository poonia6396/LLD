import threading
from model.topic import Topic
from model.topic_subscriber import TopicSubscriber

from service.subscriber_worker import SubscriberWorker

class TopicHandler:

    def __init__(self, topic: Topic):
        self.__topic = topic
        self.__subscriber_workers = {}
    
    def publish(self):
        topic_subscribers = self.__topic.get_topic_subscribers()
        for topic_subscriber in topic_subscribers:
            threading.Thread(target=self.start_subscriber_worker(topic_subscriber)).start()

    def start_subscriber_worker(self, topic_subscriber: TopicSubscriber):
        subscriber = topic_subscriber.get_subscriber()
        if not self.__subscriber_workers[subscriber]:
            self.__subscriber_workers[subscriber] = SubscriberWorker(topic_subscriber)
            self.__subscriber_workers[subscriber].run()
            
        self.__subscriber_workers[subscriber].wakeup_if_needed()

    def add_topic(self, topic: Topic):
        self.__topics_map[topic.get_id()] = topic