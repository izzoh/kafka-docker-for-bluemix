from kafka import KafkaProducer
from kafka import KafkaConsumer, KafkaProducer
import threading, logging, time
import multiprocessing

class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='134.168.38.237:9092')

        while True:
            producer.send('first', b"I am Isaac ")
            # producer.send('test', b"\xc2Hola, mundo!")
            time.sleep(1)


def main():
    tasks = [
        Producer()
    ]
    for t in tasks:
        t.start()
    time.sleep(10)


if __name__ == "__main__":
    # logging.basicConfig(
    #     format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    #     level=logging.INFO
    # )
    main()