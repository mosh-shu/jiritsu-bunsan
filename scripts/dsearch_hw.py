#
# Basic Distributed Search ver. 0.01
# サンプル版 using Threads and Queue
# created by hxt for adc2019s
#
import logging
import threading
import time
import queue
import random

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

#
# process body
#


def proc(id, card, n, resultq):
    find = 0
    logging.debug('start')
    # 探すべきnがcard[]内にあるかをチェック
    for i in range(10):
        if (card[i] == n):
            logging.debug(i)
            logging.debug('find!!!')
            find += 1
    resultq.put(find)
    logging.debug('endloop')


#
# main()
#
if __name__ == '__main__':
    #
    # 100枚のcardを作成し、任意の整数（0..1000)を記入
    #
    card = [0 for i in range(100)]
    print("card all 0 clear:", card)
    for i in range(100):
        card[i] = random.randint(1, 1000)
    #
    # use this section to test multiple cards
    #
    # for i in range(5):
    #     card[i] = 100
    # card[32] = 100
    # card[91] = 100

    print("card=", card)

    #
    # 検索用の整数を入力
    #
    print("Give me a number (1..1000)?")
    num = int(input())
    print("looking for", num)
    #
    # 10個のスレッドと通信用Queueを生成、起動
    #　
    threadlist = list()
    resultq = queue.Queue()
    for i in range(10):
        card_t = card[i*10:i*10+10]
        t = threading.Thread(target=proc, args=(i, card_t, num, resultq, ))
        threadlist.append(t)
        t.start()
    #
    #　スレッドの終了を待ち、結果を印刷
    #
    print(threadlist)
    findnum = 0
    for thread in threadlist:
        thread.join()
        findnum += resultq.get()
    print("%d cards of num = %d was found" % (findnum, num))
    print("All thread is ended.")
