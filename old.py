from hashlib import md5
from threading import Thread


found = ''
aaa=0

def inc(string):
    index = 0
    for i in range(len(string) - 1, -1, -1):
        if string[i] != 'z':
            index = i
            break
    inc_str = string[:index] + chr(ord(string[index]) + 1) + 'a' * (len(string) - (index + 1))
    return inc_str


# def count(start, stop):
#     st=start
#     counter=0
#     while st!=stop:
#         counter+=1
#     return counter


def find_mid(start, stop):
    index = 0
    for i in range(len(start)):
        if start[i] != stop[i]:
            index = i
            break
    dif = ord(stop[index]) - ord(start[index])
    mid = start[:index] + chr(ord(start[index]) + dif / 2) + 'a' * (len(start) - (index + 1))
    return mid


def split(start, stop):
    mid = find_mid(start, stop)
    quarter1=find_mid(start, mid)
    quarter2=find_mid(inc(mid), stop)
    return start, quarter1, inc(quarter1), mid, inc(mid), quarter2, inc(quarter2), stop


def crack(start, stop, md5_code):
    global found
    global aaa
    st = start
    while st != stop and found=='':
        print st + '\n'
        aaa+=1
        if md5(st).hexdigest() == md5_code:
            found = st
        else:
            st = inc(st)


def main():
    global found
    global aaa
    start = 'aaaaaa'
    stop = 'aaaaab'
    md5_code = md5('azaccc').hexdigest()
    start_stop = split(start, stop)
    threads=[]
    for i in range(0, 7, 2):
        threads.append(Thread(target=crack, args=(start_stop[i], start_stop[i+1], md5_code, )))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    # print found
    print aaa
    print found

if __name__ == '__main__':
    # print crack('aaaaaa', 'azzzzz', md5('aaaccc').hexdigest())
    # for i in split('aaaaaa', 'azzzzz'):
    #     print i
      #main()
    # m1= find_mid('aaaaaa', 'azzzzz')
    # while m1!='aaaaaa':
    #     m1=find_mid('aaaaaa', m1)
    #     print m1
    # for x in split('aaaaaa', 'aaabcc'):
    #     print x
    m1='aaaaaa'
    c=0
    while m1!='aaadba':
        print m1
        m1=inc(m1)
        c+=1
    print c
