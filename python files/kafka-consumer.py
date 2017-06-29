from kafka import KafkaConsumer, KafkaProducer
import threading, logging, time
import multiprocessing

from sys import argv


class Consumer(multiprocessing.Process):
    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='134.168.38.237:9092',
                                 auto_offset_reset='earliest')
        consumer.subscribe(['user-data'])

        for message in consumer:
            print (message)

def main():
    tasks = [
        Consumer()
    ]
    for t in tasks:
        t.start()
    time.sleep(10)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()