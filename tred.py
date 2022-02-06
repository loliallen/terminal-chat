import threading
import time, random


def console(msg):
    time.sleep(random.choice([0.6, 1, 0.3, 2]))
    print(msg)


if __name__ == "__main__":
    msgs = [
        'Оля красава',
        'Оля кидало',
        'Оля самая красивая'
    ]

    threads = []

    for msg in msgs:
        threads.append(threading.Thread(target=console, args=(msg,)))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

