from hashlib import md5
from threading import Thread
from multiprocessing import Process
import os
from time import sleep
from Code import Code

from Network import Network

found = False
aaa = 0


def crack(start, stop, md5_code):
    # global found
    # global aaa
    st = start
    while not os.path.exists('found.txt') and st <= stop:
        #print str(aaa) + '\n'
        # aaa += 1
        #print st.string + '\n'
        if md5(st.string).hexdigest() == md5_code:
            print 'founded'
            with open('found.txt', 'w') as f:
                f.write(st.string)
                print 'create'
        else:
            st += 1


def split(start, stop):
    dif = stop - start
    quarter1 = Code(start) + dif / 4
    mid = Code(quarter1) + dif / 4
    quarter2 = Code(mid) + dif / 4
    return start, quarter1, Code(quarter1) + 1, mid, Code(mid) + 1, quarter2, Code(quarter2) + 1, stop


def first_connection():
    net = Network('10.30.57.200', 2212)
    net.send('name: Dvir')
    #start_stop = net.receive()
    #print start_stop
    # lst = start_stop.split(',')
    # lst2 = [x.split(':')[1] for x in lst]
    t_keep = Thread(target=keep_alive, args=(net,))
    t_keep.start()
    return net  # , lst2


def keep_alive(net):
    while not os.path.exists('found.txt'):
        net.send('keep-alive')
        #print 'keep-alive'
        sleep(1)


def send_found(net):
    # global found
    st = 'not found'
    if os.path.exists('found.txt'):
        with open('found.txt', 'r') as f:
            st = 'found:'+f.read()
    #print 'send'+st
    net.send(st)


def network_loop(net):
    while True:
        # print 'going to rec'
        received = net.receive()
        #print 'reced'
        if received == 'bye':
            # print received
            net.close()
            if not os.path.exists('found.txt'):
                open('found.txt', 'w')
                print 'open, not write'
            break
        elif received == 'You are the king':
            #print received
            pass
        else:
            lst = received.split(',')
            lst2 = [x.split(':')[1] for x in lst]
            print lst2
            start = Code(lst2[0])
            stop = Code(lst2[1])
            md5_code = lst2[2]
            start_stop = split(start, stop)
            threads = []
            for i in range(0, 7, 2):
                threads.append(Process(target=crack, args=(start_stop[i], start_stop[i + 1], md5_code,)))
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            send_found(net)


def main():
    # # global found
    # # global aaa
    # net, lst = first_connection()
    if os.path.exists('found.txt'):  # Delete file if it exists
        os.remove('found.txt')
    # start = Code(lst[0])
    # stop = Code(lst[1])
    # md5_code = lst[2]
    # start_stop = split(start, stop)
    # threads = []
    # for i in range(0, 7, 2):
    #     threads.append(Process(target=crack, args=(start_stop[i], start_stop[i + 1], md5_code,)))
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    # # print found
    # # print '...%s' % found
    # # print aaa
    # send_found(net)
    net = first_connection()
    network_loop(net)


if __name__ == '__main__':
    # # split(Code('aaaaaa'),Code('azaaaa'))
    # # main()
    # # main()
    # ###print os.path.exists('found.txt')
    # # print os.getcwd()
    # open('aa.txt', 'w')
    # print os.path.exists('aa.txt')
    # os.remove("aa.txt")
    # # os.chdir(os.path.realpath(__path__))
    # # open ('a.txt', 'w')
    # print os.path.exists('aa.txt')
    main()
