import threading
from model.topic import Topic

class TopicHandler:

    def __init__(self):
        self.__topics_map = {}
    
    def publish(self, topic_id, message):
        topic = self.__topics_map[topic_id]
        topic.add_message(message)
        topic_subscribers = topic.get_topic_subscribers()
        for topic_subscriber in topic_subscribers:
            threading.Thread(target=self.start_subscriber_worker(topic_subscriber)).start()

    def add_topic(self, topic: Topic):
        self.__topics_map[topic.get_id()] = topic