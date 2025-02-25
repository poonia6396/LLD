from model.topic_subscriber import TopicSubscriber

class SubscriberWorker:

    def __init__(self, topic_subscriber: TopicSubscriber):
        self.__topic_subscriber = topic_subscriber

    def run(self):
        pass

    def wakeup_if_needed(self):
        with self.__topic_subscriber.get_lock():
            pass