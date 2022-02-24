import re
import pymp
import time

listofFiles = ('shakespeare1.txt', 'shakespeare2.txt', 'shakespeare3.txt',
        'shakespeare4.txt', 'shakespeare5.txt', 'shakespeare6.txt',
        'shakespeare7.txt' ,'shakespeare8.txt')

listofWords = ('hate', 'love', 'death', 'night', 'sleep', 'time', 'henry', 'hamlet',
        'you', 'my', 'blood', 'poison', 'macbeth', 'king', 'heart', 'honest')



def countWords(word, filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += file.count(word)
    return count 



def mapreduce(thread):
    start_time = time.time()
    lock = p.lock
    maindict = pymp.shared.dict()
    

    for word in listofWords:
            maindict[word] = 0

    with pymp.Parallel(1) as p:
    
        threaddict = dict()
        for word in listofWords:
            threaddict[word] = 0

        for file in p.range(len(listofFiles)):
            for word in listofWords:
                threaddict[word] += countWords(word, listofFiles[file])
        
        for word in listofWords:
            lock.acquire()
            maindict[word] += threaddict[word]
            lock.release()

    end_time = time.time()
    print("Thread ", thread," Duration: ",end_time - start_time, "seconds")
    return(maindict)  



for i in range(1, 9):
    print(mapreduce(i))
    print('thread_num:', i)

